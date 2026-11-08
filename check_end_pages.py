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

for p_num in [52, 53, 54]:
    u = urls[p_num - 1]
    r = requests.get(u)
    # extract title/headers
    print(f"=== PAGE {p_num} ===")
    matches = re.findall(r'<span[^>]*>(.*?)</span>', r.text)
    clean = " ".join([re.sub(r'<[^>]+>', '', m).strip() for m in matches if m.strip()])
    print(clean[:300])
