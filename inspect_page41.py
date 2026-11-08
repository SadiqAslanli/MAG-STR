import requests
import re
import json

session = requests.Session()
url = 'https://www.scribd.com/document/733759124/2-5341821482265756298'
r = session.get(url, timeout=15)
urls = re.findall(r'https?://html\.scribdassets\.com/[^\s"\'<>]+\.jsonp', r.text)

def get_p(u):
    m = re.search(r'/pages/(\d+)-', u)
    return int(m.group(1)) if m else 9999

page41_url = [u for u in set(urls) if get_p(u) == 41][0]
res = session.get(page41_url)
m = re.search(r'callback\(\s*(\[.*\])\s*\);?', res.text, re.DOTALL)
html = json.loads(m.group(1))[0]

pattern = re.compile(r'style="([^"]*left:([0-9.]+)px;top:([0-9.]+)px[^"]*)"[^>]*>(.*?)</span>', re.DOTALL)
elements = []
for match in pattern.finditer(html):
    style, left_s, top_s, text = match.groups()
    cl = re.sub(r'<[^>]+>', '', text).strip()
    if cl:
        elements.append({'top': float(top_s), 'left': float(left_s), 'text': cl})

elements.sort(key=lambda e: (e['top'], e['left']))

lines = []
curr = []
for e in elements:
    if not curr:
        curr = [e]
    elif abs(e['top'] - curr[0]['top']) < 18:
        curr.append(e)
    else:
        curr.sort(key=lambda x: x['left'])
        lines.append(curr)
        curr = [e]
if curr:
    curr.sort(key=lambda x: x['left'])
    lines.append(curr)

for line in lines:
    b_parts = [x['text'] for x in line if x['left'] < 1350]
    m_parts = [x['text'] for x in line if 1350 <= x['left'] < 3450]
    p_parts = [x['text'] for x in line if x['left'] >= 3450]
    if b_parts or m_parts or p_parts:
        print(f"Y={line[0]['top']:4.0f} | B: {' '.join(b_parts):<30} | M: {' '.join(m_parts):<55} | P: {' '.join(p_parts)}")

