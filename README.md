# Lagos State: law history in git

The Laws of Lagos State (Nigeria) as a git history: one file per section, one paragraph per line, so `git blame`, `git log` and `git diff` work line by line. The text is the English text of the Laws as gazetted.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

The Lagos State Ministry of Justice publishes a small number of Laws as PDFs of their text in the Lagos State of Nigeria Official Gazette. The versions here are the gazetted texts available from the Ministry, dated by each Law's commencement. Amendments made since are not yet represented.

| Folder | What |
| --- | --- |
| `tenancy-law-2011/` | Tenancy Law 2011 as gazetted: title, enacting formula and sections 1 to 49; the source PDF ends during section 49 |
| `road-traffic-law-2012/` | Road Traffic Law 2012 as gazetted on 3 August 2012, including Schedules and Regulations; one whole-text file preserves the source's page order |

The Laws are added in parts as each is verified. A PDF is left out until it can be read reliably: scans whose text layer is a poor OCR, and copies that are the Bill rather than the Law as passed (the Ministry's copy of the Criminal Law of Lagos State is the Bill, with its commencement day left blank) are not included.

Known gaps in the source: the Ministry's PDF of the Tenancy Law 2011 ends in the middle of section 49 and does not include the Schedule of forms. The Road Traffic Law PDF is the 2012 gazetted wording, not a later consolidation.

## Source

[Lagos State Ministry of Justice](https://lagosstatemoj.org/legislation/): PDFs of the Laws as published in the Lagos State of Nigeria Official Gazette. Each PDF's sha256 is recorded with its version in `data/versions.json`.

## Dates

Each Law is dated by the day it came into force under its own commencement section, at noon in Lagos.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The Tenancy Law has one file per section. The Road Traffic Law, its Schedules and Regulations are kept in one text file because their mixed section and table layout does not support a reliable split. Source printing errors remain.

## How it is checked

Every version is read back from git on the day it took effect and must match the corpus. A second, independent reading of every PDF (a different PDF engine) must contain every letter and digit of each Law in the same order, with nothing in the body left out. Results are in `REPRODUCE.md`.

## What "author" means

The author of each commit is the Law that made the change, with an e-mail address that cannot exist; the committer is always Lexifina.

## Limits

Only the gazetted versions listed above are represented; later amendments are not applied. The Ministry's PDFs are not the authoritative text; the Lagos State of Nigeria Official Gazette is.

## Licence

See [LICENSE](LICENSE): official texts of a legislative nature are not eligible for copyright in Nigeria (Copyright Act, 2022, s. 3(b)). Source: Lagos State Ministry of Justice.
