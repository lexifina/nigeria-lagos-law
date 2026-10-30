# Lagos State: law history in git

The Laws of Lagos State (Nigeria) as a git history: one file per section, one paragraph per line, so `git blame`, `git log` and `git diff` work line by line. The text is the English text of the Laws as gazetted.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

**A first build: Laws as enacted.** The Lagos State Ministry of Justice publishes a small number of Laws as PDFs of their text in the Lagos State of Nigeria Official Gazette. Each Law here is one commit holding its text as enacted, dated by its commencement and credited to the Law itself. Amendments made since are not yet in this record.

| Folder | What |
| --- | --- |
| one folder per Law (e.g. `tenancy-law-2011/`) | the Law as gazetted: `000-title.md`, `001-enacting-formula.md`, one file per section |

The Laws are added in parts as each is verified. A PDF is left out until it can be read reliably: scans whose text layer is a poor OCR, and copies that are the Bill rather than the Law as passed (the Ministry's copy of the Criminal Law of Lagos State is the Bill, with its commencement day left blank) are not included.

Known gaps in the source: the Ministry's PDF of the Tenancy Law 2011 ends in the middle of section 49 and does not include the Schedule of forms.

## Source

[Lagos State Ministry of Justice](https://lagosstatemoj.org/legislation/): PDFs of the Laws as published in the Lagos State of Nigeria Official Gazette. Each PDF's sha256 is recorded with its version in `data/versions.json`.

## Dates

Each Law is dated by the day it came into force under its own commencement section, at noon in Lagos.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The text layer of each PDF (no OCR) becomes one file per section. The cover and the Arrangement of Sections are left out; each section's heading, from that Arrangement, stands as the first line of its file. Lines wrapped by the printer are joined, so each paragraph is one line. Typing errors in the gazette stay as printed.

## How it is checked

Every version is read back from git on the day it took effect and must match the corpus. A second, independent reading of every PDF (a different PDF engine) must contain every letter and digit of each Law in the same order, with nothing in the body left out. Results are in `REPRODUCE.md`.

## What "author" means

The author of each commit is the Law that made the change, with an e-mail address that cannot exist; the committer is always Lexifina.

## Limits

Only the Laws listed above, as enacted; later amendments are not applied. The Ministry's PDFs are not the authoritative text; the Lagos State of Nigeria Official Gazette is.

## Licence

See [LICENSE](LICENSE): official texts of a legislative nature are not eligible for copyright in Nigeria (Copyright Act, 2022, s. 3(b)). Source: Lagos State Ministry of Justice.
