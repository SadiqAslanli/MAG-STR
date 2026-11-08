import requests
import re
import json

# Let's inspect page 3 or 4
for p in [2, 3, 4, 5]:
    # Find url for page p from scribd_page.html
    pass

with open('scribd_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

urls = re.findall(r'https?://html\.scribdassets\.com/[^\s"\'<>]+\.jsonp', html)
print('Total jsonp urls found:', len(urls))

# Sort by page number
def get_page_num(url):
    m = re.search(r'/pages/(\d+)-', url)
    return int(m.group(1)) if m else 9999

urls = sorted(urls, key=get_page_num)

for u in urls[:5]:
    print(u)
