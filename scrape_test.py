import requests
import re
import json

url = 'https://www.scribd.com/document/733759124/2-5341821482265756298'
r = requests.get(url)
print('Status:', r.status_code)
print('Len:', len(r.text))

title = re.findall(r'<title>(.*?)</title>', r.text)
print('Title:', title)

with open('scribd_page.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
print('Saved scribd_page.html')
