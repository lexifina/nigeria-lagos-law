"""Independent letters-and-digits check of a part against the source PDFs, read by a second engine (pypdf).

    python -X utf8 check_letters.py corpus.d/10-laws-01.json [...]

Private. For each act, its units (heading lines left out) reduced to letters and digits must be found, in order and
contiguous, in the PDF's text reduced the same way. A stretch of source text may be passed over only where it crosses
a page break (running heads, page numbers). Anything else is a mismatch. Also reports how much of the source body
after the record's first words is not in the record (should be only what the README says is left out).
"""
import json
import re
import sys
from pathlib import Path

import pypdf

HERE = Path(__file__).resolve().parent
FF = '\x0c'


def ld(s):
    return ''.join(ch for ch in s if ch.isalnum() or ch == FF)


def source(pdf):
    r = pypdf.PdfReader(str(pdf))
    return ld(FF.join((p.extract_text() or '') for p in r.pages))


def record(act):
    v = act['versions'][-1]
    out = []
    for k in sorted(v['units']):
        for line in v['units'][k]['text'].split('\n'):
            if not line.startswith('# '):
                out.append(line)
    return ld('\n'.join(out))


def align(U, S):
    m = S.find(U[:40])
    if m < 0:
        return False, f'record start not found: {U[:60]!r}', 0
    i, j, skips = 0, m, 0
    while i < len(U):
        if j < len(S) and S[j] == FF:
            j += 1
            continue
        if j < len(S) and S[j] == U[i]:
            i += 1
            j += 1
            continue
        pos = S.find(U[i:i + 24], j)
        gap = S[j:pos] if pos >= 0 else ''
        if pos >= 0 and FF in gap and len(gap) < 400:
            j = pos
            skips += 1
            continue
        return False, f'mismatch at record {i}: record {U[i:i + 50]!r} / source {S[j:j + 50]!r}', skips
    tail = S[j:].replace(FF, '')
    return True, f'ok, {skips} page-break skips, {len(tail)} source characters after the record', skips


def main():
    bad = 0
    for part in sys.argv[1:]:
        d = json.loads(Path(part).read_text(encoding='utf-8'))
        for a in d['acts']:
            name = a['versions'][-1]['source_url'].rsplit('/', 1)[1]
            ok, msg, _ = align(record(a), source(HERE / '.cache' / 'pdf' / name))
            print(('OK  ' if ok else 'BAD ') + a['slug'] + ': ' + msg)
            bad += not ok
    print('mismatches:', bad)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
