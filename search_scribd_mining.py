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

unique_urls = sorted(list(set(urls)), key=get_p)
target_urls = [(get_p(u), u) for u in unique_urls if 5 <= get_p(u) <= 52]

print("Searching across all 48 Scribd pages for 'mədən', 'dağ', etc...")

for p_num, u in target_urls:
    try:
        res = session.get(u, timeout=10)
        m = re.search(r'callback\(\s*(\[.*\])\s*\);?', res.text, re.DOTALL)
        if m:
            html = json.loads(m.group(1))[0]
            text = re.sub(r'<[^>]+>', ' ', html)
            # Normalize whitespace
            text = re.sub(r'\s+', ' ', text)
            
            # Search for mining words
            matches = re.findall(r'(\b\w{0,15}(?:mədən|meden|dağ|dag)\w{0,25}\b)', text, re.IGNORECASE)
            if matches:
                # Filter out pure "dağıdıcı" or "mədəniyyət"
                relevant = [w for w in matches if not any(x in w.lower() for x in ['mədəniyyət', 'mədəni', 'dağıdıcı', 'dağıl', 'qadağan'])]
                if relevant:
                    print(f"Page {p_num}: {relevant}")
    except Exception as e:
        pass

