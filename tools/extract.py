import re, json, sys

def to_marked(inner):
    out = inner
    out = re.sub(r'<code>(.*?)</code>', lambda m: '\x01' + m.group(1) + '\x02', out, flags=re.S)
    out = re.sub(r'<strong>(.*?)</strong>', lambda m: '**' + m.group(1) + '**', out, flags=re.S)
    out = re.sub(r'<em>(.*?)</em>', lambda m: '_' + m.group(1) + '_', out, flags=re.S)
    out = re.sub(r'<i>(.*?)</i>', lambda m: '/' + m.group(1) + '/', out, flags=re.S)
    out = re.sub(r'<a\b[^>]*href="(?P<url>[^"]*)"[^>]*>(?P<txt>.*?)</a>', lambda m: '[' + (m.group('url') or '') + '|' + m.group('txt') + ']', out, flags=re.S)
    out = re.sub(r'<[^>]+>', '', out)
    out = re.sub(r'[ \t]*\n[ \t]*', '\n', out)
    out = re.sub(r'\n{3,}', '\n\n', out)
    out = out.strip()
    out = out.replace('\x01', '«').replace('\x02', '»')
    return out

def find_block_end(html, open_pos, tag, close):
    """cari posisi close tag yang cocok, sadar nesting untuk tag yang sama."""
    pos = open_pos + len(close)  # skip open tag (assumed same length as close for these tags: <li> vs </li>, <p> vs </p> dll)
    open_len = len(close)
    depth = 1
    # scan untuk '<tag' dan '</tag>' occurrences
    pat = re.compile(r'<(' + tag + r'[\s>]|/' + tag + r'>)')
    for m in pat.finditer(html, pos):
        tok = m.group(1)
        if tok.startswith('/'):
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
    return -1

html = open(sys.argv[1]).read()
blocks = []
pat = re.compile(r'<(h[1-4]|p|li|tr|blockquote|pre)\b[^>]*>')
for m in pat.finditer(html):
    tag = m.group(1)
    open_raw = m.group(0)
    close = '</'+tag+'>'
    inner_start = m.start() + len(open_raw)
    inner_end = html.find(close, inner_start)  # naive fallback
    if tag in ('li', 'p', 'blockquote', 'tr', 'h1', 'h2', 'h3', 'h4'):
        e = find_block_end(html, m.start(), tag, close)
        if e != -1:
            inner_end = e - len(close)
    if inner_end < inner_start:
        continue
    inner = html[inner_start:inner_end]
    entry = {'id': len(blocks), 'tag': tag, 'open': open_raw,
             'inner_start': inner_start, 'inner_end': inner_end, 'inner': inner}
    if tag == 'tr':
        cells = []
        for cm in re.finditer(r'<(td|th)\b[^>]*>(.*?)</\1>', inner, flags=re.S):
            cells.append({'cell_start': cm.start(), 'cell_end': cm.end(),
                          'cell_open': cm.group(0).split('>')[0] + '>',
                          'inner': cm.group(2), 'marked': to_marked(cm.group(2))})
        entry['cells'] = cells
        entry['skip'] = False
        entry['marked'] = ' | '.join(c['marked'] for c in cells)
    elif tag == 'pre':
        entry['skip'] = True
        entry['marked'] = ''
    else:
        entry['marked'] = to_marked(inner)
        structural = len(re.findall(r'<(span|a|div|svg|img|path|circle|rect|line|polyline)\b', inner))
        entry['skip'] = (structural >= 4) or (len(entry['marked']) > 0 and entry['marked'].count('\n') * 40 > len(entry['marked']))
    blocks.append(entry)

json.dump(blocks, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
prose = [b for b in blocks if not b['skip']]
print(f"{sys.argv[1]}: total={len(blocks)} prosa={len(prose)} skip={len(blocks)-len(prose)} chars_prosa={sum(len(b['marked']) for b in prose)}")
