# How this repository was made (Lagos State)

This file is written by the build on 2026-11-05, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Lagos State Ministry of Justice: Laws of Lagos State (gazetted texts, PDF) | <https://lagosstatemoj.org/legislation/> | 2026-10-30 | Laws of Lagos State as published in the Lagos State of Nigeria Official Gazette, from the copies the Lagos State Ministry of Justice publishes at lagosstatemoj.org. Official texts of a legislative nature are not eligible for copyright: Copyright Act, 2022 (Nigeria), s. 3(b). |
| Lagos State Ministry of Justice: Lagos State Road Traffic Law 2012 (Official Gazette PDF) | <https://lagosstatemoj.org/wp-content/uploads/2020/12/Lagos-State-Road-Traffic-Law.pdf> | 2026-11-03 | Official text of a legislative nature is not eligible for copyright under Nigeria's Copyright Act 2022, section 3(b); source: Lagos State Ministry of Justice. |
| Lagos State Ministry of Justice: Lagos State Arbitration Law 2009 | <https://lagosstatemoj.org/wp-content/uploads/2025/04/Lagos-State-Arbitration-Law-2009.pdf> | 2026-11-05 | Laws of Lagos State as published in the Lagos State of Nigeria Official Gazette, from the copies the Lagos State Ministry of Justice publishes at lagosstatemoj.org. Official texts of a legislative nature are not eligible for copyright: Copyright Act, 2022 (Nigeria), s. 3(b). |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `tenancy-law-2011` | Tenancy Law 2011 (Law No. 14 of 2011) | 1 | 2011-08-24 to 2011-08-24 |
| `road-traffic-law-2012` | Lagos State Road Traffic Law 2012, with Schedules and Regulations | 1 | 2012-08-02 to 2012-08-02 |
| `arbitration-law-2009` | Lagos State Arbitration Law 2009 | 1 | 2009-05-18 to 2009-05-18 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-05.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (Africa/Lagos) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each Law here states its own commencement, and its version is dated by it; no general rule is applied. https://lagosstatemoj.org/legislation/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `8807e3c3eff6c7f42bccc2e87feb062ee0b5d526e078d5846b106e7459d6f74c` (253941 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `35388bee5aa05369f7da68f5a8fa015ea8d442b8`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

3 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Tenancy Law 2011 is dated 2011-08-24: the day of assent ("Assented to at Ikeja this 24th day of August 2011"), the date under its long title, and the commencement day s. 49 gives ("24th day of August 20...", cut off in the PDF).
- Each Law is one version: the text as enacted and gazetted, credited to the Law itself (first_law) and dated by its commencement. Later amendments are not in this record.
- One file per section. The gazette title lines (Law number, long title, date, assent line) are "000-title" and the enacting formula is "001-enacting-formula". Section headings come from the Law's own Arrangement of Sections and stand as each file's first line.
- Lines wrapped by the printer are joined into one paragraph per line; a new paragraph starts at a section number, a bracketed (sub)paragraph letter or number, or a quoted definition. Typing errors in the source stay as printed.
- Section 43 dates the Road Traffic Law's commencement to 2 August 2012; the Gazette cover is dated 3 August 2012.
- The Ministry PDF supplies a historical Gazette text rather than a current consolidation. The first version is labelled oldest version available and has no inferred later amendments.
- The source combines the Law, Schedules and Road Traffic Regulations in one PDF. Its text layer is kept as one unit, in PDF reading order, because the source's section and table layout does not support a reliable split.
- Whitespace and Unicode presentation forms are normalised; letters, digits, wording, and source printing errors are preserved. PDF page 1 is a cover notice, not the Law.
- Lagos State Arbitration Law 2009: In-force basis is section 64, official PDF page 27: “shall come into force on the 18th day of May 2009”; the source states no later amendment date.
- Arbitration is one complete-text unit, including all 33 PDF pages and the Schedule; line wraps are joined within printed paragraph blocks and all source words and punctuation remain unchanged.
- The Ministry copy is recorded as the oldest version available (first_law null); no historical reconstruction or later consolidation is asserted.
- The five embedded bitmap fragments on pages 29, 31 and 32 show scan edges and blank paper; they carry no normative text. All law text is visible PDF text, including source spelling errors.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: the text is the PDF text layer, parsed by rules; no model wrote or corrected legal text.
- No model wrote or corrected the legal text; it is extracted from the official PDF text layer.
- A model inspected source page layouts, source dates and five bitmap fragments; no model wrote or corrected law text. No OCR engine output is used.
