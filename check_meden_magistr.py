import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

print("=== Magistr proqramı kimi 'meden/dag' olan ixtisaslar ===")
unis = data if isinstance(data, list) else data.get('universities', [])
for uni in unis:
    for sp in uni.get('specialties', []):
        name = sp.get('name', '')
        if 'mədən' in name.lower() or 'dağ-mədən' in name.lower() or 'dag-meden' in name.lower():
            print(f"  {uni.get('name')}: {name}")
            print(f"    -> Ödənişli: {sp.get('paidScore')}, Pulsuz: {sp.get('freeScore')}")

print()
print("=== magistr_uygunluq.json-da master program olaraq 'meden' ===")
with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)

for m in db['mappings']:
    mp = m.get('masterProgram', {}) or {}
    name = mp.get('name', '') or ''
    if 'mədən' in name.lower():
        print(f"  Master: {name}")
        print(f"  Bachelors: {[b.get('name') for b in m.get('bachelorSpecialties', [])]}")

    # Also check universityMatches specialty names
    for u in m.get('universityMatches', []):
        sp = u.get('specialty', '') or ''
        if 'mədən' in sp.lower() or 'dağ' in sp.lower():
            print(f"  UniMatch: {u.get('university')} -> {sp}")
            print(f"    Bachelors: {[b.get('name') for b in m.get('bachelorSpecialties', [])]}")

