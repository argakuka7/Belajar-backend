#!/usr/bin/env python3
"""apply.py <blocks.json> <translations.json> <notes.html>
Terapkan terjemahan (id -> teks marked) ke notes.html via splice offset eksak.
Sel kosong tabel di-split dengan ' | '. Konversi marker: «..»=code, **..**=strong, _.._=em, [url|txt]=link."""
import json, re, sys

def from_marked(s):
    out = s
    def repl_link(m):
        url, txt = m.group(1), m.group(2)
        return '<a href="' + url + '">' + txt + '</a>' if url else txt
    out = re.sub(r'\[([^\]|]*)\|([^\]]*)\]', repl_link, out)
    parts = re.split(r'(«.*?»)', out)
    out_parts = []
    for part in parts:
        if part.startswith('«') and part.endswith('»'):
            out_parts.append('<code>' + part[1:-1] + '</code>')
        else:
            out_parts.append(part)
    out = ''.join(out_parts)
    def wrap(pattern, open_t, close_t):
        nonlocal out
        res, i = [], 0
        while i < len(out):
            m = re.compile(pattern).search(out, i)
            if not m:
                res.append(out[i:]); break
            res.append(out[i:m.start()]); res.append(open_t + m.group(1) + close_t)
            i = m.end()
        out = ''.join(res)
    wrap(r'\*\*(.+?)\*\*', '<strong>', '</strong>')
    wrap(r'_(.+?)_', '<em>', '</em>')
    return out

blocks = json.load(open(sys.argv[1]))
tr = json.load(open(sys.argv[2]))
path = sys.argv[3]
html = open(path).read()

edits = []
for b in blocks:
    if b['skip'] or str(b['id']) not in tr:
        continue
    translation = tr[str(b['id'])]
    if b['tag'] == 'tr':
        parts = [p for p in translation.split(' | ')]
        cells = b['cells']
        if len(parts) != len(cells):
            print(f"  !! tr {b['id']}: {len(parts)} bagian vs {len(cells)} sel -> fallback")
            parts = [' | '.join(parts)] + [''] * (len(cells) - 1)
        for cell, part in zip(cells, parts):
            close_tag = '</' + cell['cell_open'].strip('<>').split()[0] + '>'
            s = b['inner_start'] + cell['cell_start']
            e = b['inner_start'] + cell['cell_end']
            edits.append((s, e, cell['cell_open'] + from_marked(part) + close_tag))
    else:
        edits.append((b['inner_start'], b['inner_end'], from_marked(translation)))

edits.sort(key=lambda x: x[0], reverse=True)
for s, e, repl in edits:
    html = html[:s] + repl + html[e:]
open(path, "w").write(html)
print("applied", len(edits), "edits ->", path)
