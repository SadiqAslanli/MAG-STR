import requests
import re
import json

def fetch_page_elements(url):
    r = requests.get(url)
    m = re.search(r'callback\(\[\s*"(.*)"\s*\]\)', r.text, re.DOTALL)
    if not m:
        return []
    try:
        html = m.group(1).encode('utf-8').decode('unicode_escape')
    except Exception:
        html = m.group(1)
    
    elements = []
    for match in re.finditer(r'<span[^>]*style="([^"]*)"[^>]*>(.*?)</span>', html, re.DOTALL):
        style = match.group(1)
        raw_text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        if not raw_text:
            continue
        top_m = re.search(r'top:([0-9.]+)px', style)
        left_m = re.search(r'left:([0-9.]+)px', style)
        if top_m and left_m:
            elements.append({
                'top': float(top_m.group(1)),
                'left': float(left_m.group(1)),
                'text': raw_text
            })
    return elements

# Page 6
u6 = 'https://html.scribdassets.com/eoh9xur0gchwezt/pages/6-37b97513e7.jsonp'
elems = fetch_page_elements(u6)
print(f"Page 6 elements: {len(elems)}")

# Column ranges typically:
# Col 1 (Bakalavr): left ~ 300 to 1400
# Col 2 (Magistr): left ~ 1400 to 3500
# Col 3 (Program): left ~ 3500 to 3800
# Col 4 (Min score): left ~ 3800 to 4200

# Let's see some samples in each col
for col_name, (min_x, max_x) in [
    ('Col 1 (Bakalavr)', (300, 1400)),
    ('Col 2 (Magistr)', (1400, 3500)),
    ('Col 3 (Proqram)', (3500, 3850)),
    ('Col 4 (Min bal)', (3850, 4300))
]:
    col_items = [e['text'] for e in elems if min_x <= e['left'] < max_x and e['top'] > 700]
    print(f"{col_name}: sample ({len(col_items)} items): {' '.join(col_items[:20])}")
