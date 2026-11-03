# How this repository was made (Lagos State)

This file is written by the build on 2026-11-03, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Lagos State Ministry of Justice: Laws of Lagos State (gazetted texts, PDF) | <https://lagosstatemoj.org/legislation/> | 2026-10-30 | Laws of Lagos State as published in the Lagos State of Nigeria Official Gazette, from the copies the Lagos State Ministry of Justice publishes at lagosstatemoj.org. Official texts of a legislative nature are not eligible for copyright: Copyright Act, 2022 (Nigeria), s. 3(b). |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `tenancy-law-2011` | Tenancy Law 2011 (Law No. 14 of 2011) | 1 | 2011-08-24 to 2011-08-24 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-03.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 2 tags.

## Dates

Each commit is dated at noon (Africa/Lagos) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each Law here states its own commencement, and its version is dated by it; no general rule is applied. https://lagosstatemoj.org/legislation/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `02fd8b4df112996d979be80cd37d32612c870d1eaf279edc69bd618352190b9a` (43221 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `900da0d33bfd1ef455267fb4dcef7961fd5acc9c`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Tenancy Law 2011 is dated 2011-08-24: the day of assent ("Assented to at Ikeja this 24th day of August 2011"), the date under its long title, and the commencement day s. 49 gives ("24th day of August 20...", cut off in the PDF).
- Each Law is one version: the text as enacted and gazetted, credited to the Law itself (first_law) and dated by its commencement. Later amendments are not in this record.
- One file per section. The gazette title lines (Law number, long title, date, assent line) are "000-title" and the enacting formula is "001-enacting-formula". Section headings come from the Law's own Arrangement of Sections and stand as each file's first line.
- Lines wrapped by the printer are joined into one paragraph per line; a new paragraph starts at a section number, a bracketed (sub)paragraph letter or number, or a quoted definition. Typing errors in the source stay as printed.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: the text is the PDF text layer, parsed by rules; no model wrote or corrected legal text.
