# Stage 8 — Automated Regression Gates

## Scope

This stage converts the audit invariants established in Stages 1–7 into dependency-free automated checks. It does not change student teaching content, commit the work, publish the site or replace manual semantic review.

## New gates

- Validate the locked `audit/source-manifest.csv` schema.
- Require all 18 audited Cambridge source IDs.
- Validate source-ID/code consistency, document type, official Cambridge URL, unique SHA-256 value, audit date, authority level, scope and limitations.
- Reject PDF files stored in the repository; official documents remain external and are represented by URL and SHA-256 evidence.
- Validate the Stage 5, 6 and 7 semantic-audit CSV schemas.
- Require their 133 IGCSE, 178 AS and 83 A2 objective rows to match the order and IDs in `coverage.md`.
- Require every semantic-audit row to finish with `final_status=verified`, use registered source IDs and retain its page/finding/repair evidence.
- Reject unsupported official/scoring phrases and official/MS-aligned labels without a registered source ID.
- Require two-argument IGCSE `ROUND(value, places)` calls.
- Reject 9618 `RAND(x)` inside IGCSE pseudocode and IGCSE `RANDOM()` inside AS/A2 content.

## Negative controls

`scripts/test_check_site_negative.py` now also proves rejection of:

- duplicate, missing or malformed source records;
- unsupported Cambridge claims and unregistered official labels;
- current-version regression;
- one-argument `ROUND` and cross-syllabus random-routine regressions;
- collapsed IGCSE Paper 2 language scope;
- missing, unverified or unknown-source semantic-audit rows.

The suite retains one deliberate passing control showing that structurally valid but semantically diluted prose can still pass. Official-source human review therefore remains mandatory for meaning and correctness.

## Result

- `python3 scripts/check_site.py`: passed.
- `python3 scripts/test_check_site_negative.py`: 29 rejection controls passed; the documented semantic blind-spot control behaved as expected.
- `git diff --check`: passed.
