#!/usr/bin/env bash
# Initialize a new product workspace and mirror agent command files.
set -euo pipefail

SLUG="${1:-}"
AGENT="${2:-all}"

if [[ -z "$SLUG" ]]; then
  echo "usage: ./scripts/pf-init.sh <product-slug> [claude|codex|cursor|copilot|gemini|all]" >&2
  exit 1
fi
if [[ ! "$SLUG" =~ ^[a-z0-9-]+$ ]]; then
  echo "error: slug must be kebab-case (a-z, 0-9, -)" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIR="$ROOT/products/$SLUG"

if [[ -d "$DIR" ]]; then
  echo "error: $DIR already exists" >&2
  exit 1
fi

mkdir -p "$DIR/handoff"

for f in "$ROOT"/templates/*.md; do
  base="$(basename "$f")"
  sed "s/{{PRODUCT_NAME}}/$SLUG/g; s/{{DATE}}/$(date +%Y-%m-%d)/g" "$f" > "$DIR/$base"
done

cat > "$DIR/product-packet.yaml" <<EOF
\$schema: "product-forge/v1"
product:
  slug: $SLUG
  name: $SLUG
  created: $(date +%Y-%m-%d)
  phase: constitution
constitution:
  principles: []
  non_goals: []
domain: {}
benchmarks: []
feature_candidates: []
requirements: []
nfrs: []
design: {}
architecture: {}
adrs: []
epics: []
stories: []
risks: []
metrics:
  kpis: []
roadmap: []
decisions: []
audit:
  status: fail
EOF

echo "PF_SLUG=$SLUG" > "$ROOT/.pf-active"

mirror() {
  local dest="$1" ext="$2"
  mkdir -p "$dest"
  for c in "$ROOT"/.claude/commands/*.md; do
    cp "$c" "$dest/$(basename "${c%.md}")$ext"
  done
}

case "$AGENT" in
  copilot|all) mirror "$ROOT/.github/prompts" ".prompt.md" ;;&
  codex|all)   mirror "$ROOT/.codex/prompts" ".md" ;;&
  cursor|all)  mirror "$ROOT/.cursor/rules" ".mdc" ;;&
  gemini|all)  mirror "$ROOT/.gemini/commands" ".md" ;;&
  claude)      : ;;
esac

echo "Created products/$SLUG"
echo "Active product set in .pf-active"
echo
echo "Next: run /pf.constitution in your agent."
