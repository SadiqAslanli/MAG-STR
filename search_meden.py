import json

with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)

print('--- Searching magistr_uygunluq.json ---')
found_b = []
for m in db['mappings']:
    for b in m.get('bachelorSpecialties', []):
        name = b.get('name') or ''
        code = b.get('code') or ''
        if 'mədən' in name.lower() or 'meden' in name.lower():
            found_b.append((code, name, m.get('programNumber'), m.get('sourcePage')))

print(f'Total bachelor matches: {len(found_b)}')
for f in set(found_b):
    print(f)

print('\n--- Searching eligibleMasterPrograms ---')
for m in db['mappings']:
    for emp in m.get('eligibleMasterPrograms', []):
        txt = (emp.get('name') or '') + ' ' + (emp.get('specializationsText') or '')
        if 'mədən' in txt.lower() or 'meden' in txt.lower():
            print(f"Prog {m.get('programNumber')} Page {m.get('sourcePage')}: {txt[:100]}")

print('\n--- Searching data.json ---')
with open('data.json', encoding='utf-8') as f:
    dj = json.load(f)

for u in dj['universities']:
    for s in u['specialties']:
        if 'mədən' in s['name'].lower() or 'meden' in s['name'].lower():
            print(f"{u['name']} -> {s['name']} (Ödənişli: {s.get('paidScore')}, Pulsuz: {s.get('freeScore')})")

