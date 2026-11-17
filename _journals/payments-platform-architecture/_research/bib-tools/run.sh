#!/bin/sh
# Rebuild the bibliography of *SETTLED: Architecting Payments and Revenue Infrastructure* (posts/bibliography/index.md)
# from every page's "## Sources and Evidence" section.
# Usage, from anywhere:  sh _journals/payments-platform-architecture/_research/bib-tools/run.sh
# R-numbers stay stable through ids.json; see the header of gen.py. Read the audit lines fix.py prints
# (no date, DATE CONFLICT, TITLE VARIANTS, SAME TITLE, AGE) and the UNPARSED lines gen.py prints after every run.
# Link check (separate, slow, needs the network):  python3 linkcheck.py   -> link-check.md
set -e
cd "$(dirname "$0")"
python3 gen.py
python3 classify.py > classify-review.txt   # full topic/type listing, for review
python3 fix.py
python3 render.py
rm -f srcs2.json srcs3.json srcs4.json   # intermediates; ids.json is the only state to keep
