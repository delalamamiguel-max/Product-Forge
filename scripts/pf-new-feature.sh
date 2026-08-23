#!/usr/bin/env bash
# Add a feature workstream to an existing product without restarting discovery.
set -euo pipefail
SLUG="${1:-}"; FEATURE="${2:-}"
if [[ -z "$SLUG" || -z "$FEATURE" ]]; then
  echo "usage: ./scripts/pf-new-feature.sh <product-slug> <feature-slug>" >&2; exit 1
fi
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/products/$SLUG"
[[ -d "$SRC" ]] || { echo "error: no product at $SRC" >&2; exit 1; }
DST="$SRC/features/$FEATURE"
mkdir -p "$DST/handoff"
for base in 02-benchmark-report.md 03-prd.md 04-design-system.md 06-backlog.md; do
  sed "s/{{PRODUCT_NAME}}/$SLUG — $FEATURE/g; s/{{DATE}}/$(date +%Y-%m-%d)/g" \
    "$ROOT/templates/$base" > "$DST/$base"
done
echo "Created $DST"
echo "Constitution and domain brief are inherited from the parent product."
echo "Start at /pf.benchmark — re-benchmark only for this feature's interaction problem."
