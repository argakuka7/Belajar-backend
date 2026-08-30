import re, sys, json
html = open(sys.argv[1]).read()
problems = []
for m in ['«', '»', '`']:
    # backtick diizinkan hanya di dalam <pre>
    c = html.count(m)
    if c:
        # hitung di luar pre
        outside = len(re.sub(r'<pre[^>]*>.*?</pre>', '', html, flags=re.S)) and 0
        outside = re.sub(r'<pre[^>]*>.*?</pre>', '', html, flags=re.S).count(m)
        if outside: problems.append(f"marker {m!r} di luar <pre>: {outside}")
star = re.sub(r'<pre[^>]*>.*?</pre>', '', html, flags=re.S).count('**')
if star: problems.append(f"'**' di luar <pre>: {star}")
for tag in ["div","p","h1","h2","h3","h4","li","tr","td","th","pre","code","strong","em","table","ul","ol","blockquote","span","a","i"]:
    o = len(re.findall(r'<'+tag+r'[\s>]', html)); c = len(re.findall(r'</'+tag+'>', html))
    if o != c: problems.append(f"tag {tag}: {o} vs {c}")
pres = re.findall(r'<pre[^>]*>.*?</pre>', html, re.S)
print("VERIFY", sys.argv[1], "| size:", len(html), "| pre:", len(pres), "|", "OK" if not problems else problems)
