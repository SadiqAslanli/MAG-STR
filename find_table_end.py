import requests
import re
import json

with open('scribd_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

urls = re.findall(r'https?://html\.scribdassets\.com/[^\s"\'<>]+\.jsonp', html)
def get_page_num(url):
    m = re.search(r'/pages/(\d+)-', url)
    return int(m.group(1)) if m else 9999

urls = sorted(list(set(urls)), key=get_page_num)

for p_num in range(50, 75):
    u = urls[p_num - 1]
    r = requests.get(u)
    has_min = 'minimal' in r.text or 'Proq' in r.text
    print(f"Page {p_num}: has table header/min: {has_min}")
    if not has_min:
        print(f"--> Table might end around page {p_num}")
        break
