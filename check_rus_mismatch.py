import json

with open('magistr_uygunluq.json', encoding='utf-8') as f:
    db = json.load(f)

# Find all mappings where code 050117 (Rus dili müəllimliyi) appears as bachelor
print("=== All mappings for 050117 ===")
for m in db['mappings']:
    for b in m.get('bachelorSpecialties', []):
        if b.get('code') == '050117':
            print(f"\nPage {m.get('sourcePage')}, Program #{m.get('programNumber')}")
            print(f"  Bachelor: {b.get('name')}")
            print(f"  All bachelors in this row: {[x.get('name') for x in m.get('bachelorSpecialties', [])]}")
            print(f"  University matches:")
            for u in m.get('universityMatches', []):
                print(f"    - {u['university']}: {u['specialty']}")

print("\n=== Searching for Azerbaycan Universiteti with azerbaycan edebiyyati ===")
for m in db['mappings']:
    for u in m.get('universityMatches', []):
        if 'azərbaycan' in u.get('university','').lower() and 'azərbaycan ədəbiyyatı' in u.get('specialty','').lower():
            print(f"\nPage {m.get('sourcePage')}, Program #{m.get('programNumber')}")
            print(f"  Bachelors: {[b.get('name') for b in m.get('bachelorSpecialties', [])]}")
            print(f"  University: {u['university']}, Specialty: {u['specialty']}")

