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

for p_num in range(5, 15):
    u = urls[p_num - 1]
    r = requests.get(u)
    if 'Geologiya' in r.text or '050611' in r.text:
        print(f"Page {p_num} has Geologiya / 050611!")
        break
