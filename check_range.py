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

for p_num in [30, 50, 70, 90, 94]:
    if p_num <= len(urls):
        u = urls[p_num - 1]
        r = requests.get(u)
        print(f"Page {p_num}: len {len(r.text)}, keywords: {[k for k in ['minimal', 'Proq', 'Bakalavr', 'ixtisas', 'Qəbul', 'İmtahan'] if k in r.text]}")
