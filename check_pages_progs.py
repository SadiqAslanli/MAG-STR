import json

with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)

for p in range(5, 26):
    mappings = [m for m in db['mappings'] if m.get('sourcePage') == p]
    progs = [m.get('programNumber') for m in mappings]
    print(f"Page {p:2d}: Programs = {progs}")

