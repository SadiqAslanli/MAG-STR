import json

with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)

engineering_codes = set()
for m in db['mappings']:
    for b in m.get('bachelorSpecialties', []):
        c = b.get('code') or ''
        if c.startswith('0506'):
            engineering_codes.add((c, b.get('name'), m.get('programNumber'), m.get('sourcePage')))

for c in sorted(list(engineering_codes)):
    print(c)

