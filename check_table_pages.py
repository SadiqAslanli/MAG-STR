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
print(f"Total pages: {len(urls)}")

# Check pages for table header or content
# Table header has 'ixtisasın şifri' or 'minimal bal' or 'Proqram'
table_pages = []
for u in urls[:25]: # check first 25
    p_num = get_page_num(u)
    r = requests.get(u)
    if 'minimal' in r.text or 'Proq' in r.text or 'Bakalavr' in r.text or 'ixtisas' in r.text:
        table_pages.append(p_num)

print(f"Pages with keywords in first 25: {table_pages}")
