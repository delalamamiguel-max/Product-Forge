#!/usr/bin/env python3
"""Traceability and completeness validator for a Product Forge packet.

Usage: python3 scripts/pf-validate.py products/<slug>/product-packet.yaml
Exit 0 = PASS, 1 = FAIL. Intended to run in CI as a handoff gate.
"""
import sys, re
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required: pip install pyyaml")

GENERIC = {"b2b saas", "saas", "software", "tech", "general", "various", "healthcare",
           "finance", "retail", "education", "generic b2b saas"}
PLACEHOLDER = re.compile(r"\bTBD\b|lorem ipsum|\{\{|XXX|FIXME", re.I)
CLARIFY = re.compile(r"NEEDS CLARIFICATION", re.I)
HAS_NUMBER = re.compile(r"\d")

class Report:
    def __init__(self): self.rows = []
    def check(self, name, ok, ids=None, fix=""):
        self.rows.append((name, ok, ids or [], fix))
    def render(self):
        fails = [r for r in self.rows if not r[1]]
        for name, ok, ids, fix in self.rows:
            mark = "PASS" if ok else "FAIL"
            print(f"[{mark}] {name}")
            if not ok:
                if ids: print(f"       offending: {', '.join(map(str, ids[:12]))}")
                if fix: print(f"       fix: {fix}")
        print(f"\n{len(self.rows)-len(fails)}/{len(self.rows)} checks passed")
        return 1 if fails else 0

def ids_of(items, key="id"):
    return [i.get(key) for i in (items or []) if isinstance(i, dict) and i.get(key)]

def main(path):
    p = Path(path)
    if not p.exists(): sys.exit(f"not found: {path}")
    d = yaml.safe_load(p.read_text()) or {}
    r = Report()

    # --- domain specificity -------------------------------------------------
    dom = d.get("domain") or {}
    sub = (dom.get("sub_vertical") or "").strip().lower()
    r.check("domain.sub_vertical is specific", bool(sub) and sub not in GENERIC,
            [sub or "<empty>"], "name the sub-vertical, e.g. 'outpatient dermatology, 1-5 providers'")
    r.check("domain regulatory answered explicitly", bool(dom.get("regulatory")),
            fix="record frameworks, or an explicit 'none identified' entry")
    r.check("domain glossary present", len(dom.get("glossary") or []) >= 5,
            fix="10-20 terms an outsider would get wrong")

    # --- benchmark ----------------------------------------------------------
    bms = d.get("benchmarks") or []
    r.check("at least 3 benchmark references", len(bms) >= 3,
            fix="3-5 direct, 1-2 category leaders, 1 cross-industry outlier")
    r.check("benchmark set includes an outlier",
            any(b.get("type") == "outlier" for b in bms),
            fix="add one cross-industry reference solving the same interaction problem")
    uncited = [b.get("id") for b in bms
               for ax in ("functionality","usability","visual","ux_craft")
               if not ((b.get("scores") or {}).get(ax) or {}).get("source")]
    r.check("every benchmark score cites a source", not uncited, sorted(set(uncited)),
            "add a URL per axis per reference; uncited scores are deleted")

    # --- feature decisions --------------------------------------------------
    fc = d.get("feature_candidates") or []
    undecided = [f.get("feature") for f in fc if f.get("decision") not in ("IN","OUT","LATER")]
    r.check("every feature candidate is decided", not undecided, undecided,
            "mark each IN / OUT / LATER with a reason")
    in_no_fr = [f.get("feature") for f in fc if f.get("decision") == "IN" and not f.get("becomes")]
    r.check("every IN feature maps to an FR", not in_no_fr, in_no_fr,
            "create the FR and set becomes: FR-nnn")

    # --- requirements -------------------------------------------------------
    reqs = d.get("requirements") or []
    fr_ids = set(ids_of(reqs))
    dom_ids = {j.get("id") for j in (dom.get("jtbd") or [])} | {c.get("id") for c in (dom.get("constraints") or [])}
    bm_ids = set(ids_of(bms))
    orphan_up = [q["id"] for q in reqs if not (set(q.get("traces_to") or []) & (dom_ids | bm_ids))
                 and "original_bet" not in (q.get("traces_to") or [])]
    r.check("every FR traces up to DOM/BM/bet", not orphan_up, orphan_up,
            "add traces_to, or flag as original_bet with a hypothesis")
    bet_no_hyp = [q["id"] for q in reqs
                  if "original_bet" in (q.get("traces_to") or []) and not q.get("hypothesis")]
    r.check("original bets state a hypothesis", not bet_no_hyp, bet_no_hyp,
            "state the bet and how you'd know it was wrong")
    no_verify = [q["id"] for q in reqs if not q.get("verification")]
    r.check("every FR states a verification method", not no_verify, no_verify)
    bad_rule = [rr.get("id") for q in reqs for rr in (q.get("rules") or [])
                if not str(rr.get("id", "")).startswith("RULE-" + str(q["id"]).replace("-", ""))]
    r.check("business rules name their parent FR", not bad_rule, bad_rule,
            "use RULE-FRnnn-nn scoped to the parent")

    # --- NFRs ---------------------------------------------------------------
    nfrs = d.get("nfrs") or []
    unnumbered = [n["id"] for n in nfrs if not HAS_NUMBER.search(str(n.get("requirement","")))]
    r.check("every NFR carries a number", not unnumbered, unnumbered,
            "'fast' is not a requirement; give a threshold")
    unmeasured = [n["id"] for n in nfrs if not n.get("measurement")]
    r.check("every NFR states how it is measured", not unmeasured, unmeasured)

    prins = ids_of((d.get("constitution") or {}).get("principles"))
    enforced = {t for n in nfrs for t in (n.get("traces_to") or [])} | \
               {a.get("enforces") for a in (d.get("adrs") or [])}
    unenforced = [p for p in prins if p not in enforced]
    r.check("every constitution principle is enforced", not unenforced, unenforced,
            "each PRIN needs an NFR or ADR enforcing it")

    # --- design -------------------------------------------------------------
    des = d.get("design") or {}
    NINE = {"default","hover","focus_visible","active","disabled","loading","empty","error","overflow"}
    incomplete = [c["id"] for c in (des.get("components") or [])
                  if not NINE.issubset(set(c.get("states") or []))]
    r.check("every component defines all nine states", not incomplete, incomplete,
            "missing empty/loading/error states get invented inconsistently by the agent")
    noflow = [f.get("id") for f in (des.get("flows") or []) if not f.get("failure_branches")]
    r.check("every UX flow defines failure branches", not noflow, noflow)

    # --- stories ------------------------------------------------------------
    stories = d.get("stories") or []
    st_ids = set(ids_of(stories))
    covered_frs = {t for s in stories for t in (s.get("traces_to") or [])}
    fr_no_story = sorted(fr_ids - covered_frs)
    r.check("every FR has at least one story", not fr_no_story, fr_no_story)
    orphan_stories = [s["id"] for s in stories
                      if not (set(s.get("traces_to") or []) & fr_ids)]
    r.check("no orphan stories", not orphan_stories, orphan_stories,
            "an orphan story is scope creep; find its FR or delete it")
    missing_paths = [s["id"] for s in stories
                     if {"happy","edge","failure"} - {a.get("type") for a in (s.get("acceptance_criteria") or [])}]
    r.check("stories cover happy, edge, and failure", not missing_paths, missing_paths)
    oversized = [s["id"] for s in stories if len(s.get("acceptance_criteria") or []) > 8]
    r.check("stories are agent-session sized", not oversized, oversized,
            ">8 acceptance criteria: split the story")

    used_cmp = {t for s in stories for t in (s.get("traces_to") or [])}
    unused = [c["id"] for c in (des.get("components") or []) if c["id"] not in used_cmp] + \
             [f["id"] for f in (des.get("flows") or []) if f["id"] not in used_cmp]
    r.check("every component and flow is used by a story", not unused, unused)

    # --- risks & metrics ----------------------------------------------------
    risks = d.get("risks") or []
    weak = [x["id"] for x in risks if not (x.get("owner") and x.get("trigger") and x.get("mitigation"))]
    r.check("every risk has owner, trigger, mitigation", not weak, weak,
            "a risk without an observable trigger is a worry")
    kpis = ((d.get("metrics") or {}).get("kpis")) or []
    incomplete_kpi = [k["id"] for k in kpis
                      if not all(k.get(f) for f in ("baseline","target","window","instrumentation"))]
    r.check("every KPI has baseline, target, window, instrumentation", not incomplete_kpi, incomplete_kpi)

    # --- roadmap ------------------------------------------------------------
    rm = d.get("roadmap") or []
    if rm:
        s1 = rm[0]
        outcome = str(s1.get("outcome","")).lower()
        r.check("slice 1 is a user-facing vertical",
                bool(outcome) and not any(w in outcome for w in ("foundation","infrastructure","setup","scaffold")),
                [outcome], "slice 1 must be one complete user journey, however narrow")
    incomplete_slices = [s.get("slice") for s in rm if not (s.get("entry_criteria") and s.get("exit_criteria"))]
    r.check("every slice has entry and exit criteria", not incomplete_slices, incomplete_slices)

    # --- integrity ----------------------------------------------------------
    all_ids = ids_of(reqs)+ids_of(nfrs)+ids_of(stories)+ids_of(risks)+ids_of(kpis)+ids_of(bms)+ids_of(d.get("adrs"))
    dupes = sorted({i for i in all_ids if all_ids.count(i) > 1})
    r.check("no duplicate IDs", not dupes, dupes)

    # --- phase completeness (prevents vacuous passes on empty sections) -----
    PHASES = ["constitution","discover","benchmark","specify","clarify",
              "design","plan","stories","audit","handoff"]
    phase = (d.get("product") or {}).get("phase", "constitution")
    idx = PHASES.index(phase) if phase in PHASES else 0
    def required_by(stage, label, populated):
        if idx >= PHASES.index(stage):
            r.check(f"{label} populated by phase '{stage}'", bool(populated),
                    fix=f"phase is '{phase}' but {label} is empty — run /pf.{stage}")
    required_by("constitution", "constitution.principles", prins)
    required_by("discover", "domain.jtbd", dom.get("jtbd"))
    required_by("benchmark", "benchmarks", bms)
    required_by("benchmark", "feature_candidates", fc)
    required_by("specify", "requirements", reqs)
    required_by("specify", "nfrs", nfrs)
    required_by("design", "design.components", des.get("components"))
    required_by("design", "design.flows", des.get("flows"))
    required_by("plan", "architecture.stack", (d.get("architecture") or {}).get("stack"))
    required_by("stories", "epics", d.get("epics"))
    required_by("stories", "stories", stories)
    required_by("stories", "roadmap", rm)
    required_by("audit", "risks", risks)
    required_by("audit", "metrics.kpis", kpis)

    # --- artifact text sweep ------------------------------------------------
    art_dir = p.parent
    clar, place = [], []
    for md in sorted(art_dir.glob("*.md")):
        txt = md.read_text(errors="ignore")
        if CLARIFY.search(txt): clar.append(md.name)
        if PLACEHOLDER.search(txt): place.append(md.name)
    r.check("zero [NEEDS CLARIFICATION] markers", not clar, clar, "run /pf.clarify")
    r.check("zero placeholders or unfilled template tokens", not place, place)

    print()
    return r.render()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: pf-validate.py products/<slug>/product-packet.yaml")
    sys.exit(main(sys.argv[1]))
