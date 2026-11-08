import json
import os
import re

with open('magistr_uygunluq.json', 'r', encoding='utf-8') as f:
    magistr_data = json.load(f)

mappings = magistr_data.get('mappings', [])

# Also load university catalog from data.json if available
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        uni_data = json.load(f)
except Exception:
    uni_data = {}

md_lines = []
md_lines.append("# Magistratura Səviyyəsi Üzrə İxtisaslaşma Seçimi Cədvəli (DİM)\n")
md_lines.append("> **Mənbə:** Dövlət İmtahan Mərkəzi (DİM) — Magistr xüsusi buraxılışı / Scribd Sənədi (`733759124/2-5341821482265756298`)  ")
md_lines.append(f"> **Məlumat:** {len(mappings)} uyğunluq bloku, 40-dan çox qəbul proqramı, bakalavriat və magistratura ixtisaslaşmaları, minimal bal tələbləri və universitet keçid balları.\n")

md_lines.append("## 1. Scribd Saytından Data Scraping Metodu (Necə Çəkilir?)\n")
md_lines.append("Scribd sənədləri standart veb səhifələrdən fərqli olaraq mətnləri birbaşa tək HTML teqi daxilində saxlamır. Məlumatı çəkmək üçün aşağıdakı arxitektura istifadə olunur:\n")
md_lines.append("1. **CDN / JSONP Arxitekturası:** Scribd sənədin hər səhifəsini `https://html.scribdassets.com/{doc_id}/pages/{page_num}-{hash}.jsonp` formatında saxlayır.")
md_lines.append("2. **Səhifə Linklərinin Çıxarılması:** Əsas sənəd səhifəsindən (`https://www.scribd.com/document/733759124/...`) HTML endirilir və içərisindəki bütün `html.scribdassets.com` jsonp ünvanları regex vasitəsilə aşkarlanır.")
md_lines.append("3. **JSONP-dən HTML-ə Keçid:** Hər bir JSONP faylı `window.pageN_callback([\"<html content>\"])` şəklində gəlir. Python vasitəsilə JSON hissəsi ayrılır və səhifənin HTML DOM-u əldə edilir.")
md_lines.append("4. **Koordinat Əsaslı Cədvəl Bərpası:** Hər bir mətn elementi (span) `top` (şaquli) və `left` (üfüqi) pikselləri ilə yerləşdirilib. 4 əsas sütun (Bakalavr ixtisası, Magistratura ixtisaslaşması, Proqram №, Minimal bal) X və Y koordinatlarına görə qruplaşdırılaraq tam cədvələ çevrilir.\n")

md_lines.append("```python")
md_lines.append("# Nümunə: Scribd JSONP səhifəsindən mətn və koordinatların çəkilməsi")
md_lines.append("import requests, re, json")
md_lines.append("")
md_lines.append("url = 'https://html.scribdassets.com/eoh9xur0gchwezt/pages/5-c40328b208.jsonp'")
md_lines.append("res = requests.get(url)")
md_lines.append("match = re.search(r'callback\\(\\s*(\\[.*\\])\\s*\\);?', res.text, re.DOTALL)")
md_lines.append("if match:")
md_lines.append("    html_content = json.loads(match.group(1))[0]")
md_lines.append("    # Cədvəl elementlərinin koordinatlarla oxunması...")
md_lines.append("```\n")

md_lines.append("## 2. Ümumi Qeydlər və Tələblər\n")
md_lines.append("- **`*` İxtisaslar:** Əvvəlki illərin təsnifatına uyğun ixtisas kodları.")
md_lines.append("- **`**` İxtisaslar:** Cari bakalavriat təsnifatı üzrə ixtisaslar.")
md_lines.append("- **Minimal Bal:** Bakalavrın müvafiq proqram üzrə ixtisaslaşma seçiminə buraxılması üçün magistratura qəbul imtahanında (və ya qabiliyyət imtahanında) toplamalı olduğu ən aşağı bal həddidir.\n")

md_lines.append("## 3. İxtisaslaşma Seçimi və Uyğunluq Cədvəli\n")

# Group mappings by Program Number
programs_map = {}
for m in mappings:
    prog = m.get('programNumber')
    prog_key = f"Proqram № {prog}" if prog is not None else "Ümumi / Digər Proqramlar"
    if prog_key not in programs_map:
        programs_map[prog_key] = []
    programs_map[prog_key].append(m)

# Sort program keys naturally
def sort_key(k):
    m = re.search(r'(\d+)', k)
    return int(m.group(1)) if m else 9999

sorted_prog_keys = sorted(programs_map.keys(), key=sort_key)

for prog_key in sorted_prog_keys:
    items = programs_map[prog_key]
    md_lines.append(f"### {prog_key}\n")
    
    for idx, item in enumerate(items, 1):
        min_score = item.get('minimumScore', 'Göstərilməyib')
        page = item.get('sourcePage', '-')
        
        md_lines.append(f"#### Blok {idx} (Minimal bal: `{min_score}`, Səhifə: {page})\n")
        
        # Bachelor specialties table
        md_lines.append("**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**\n")
        md_lines.append("| Kod / Şifr | Bakalavr İxtisasının Adı |")
        md_lines.append("| :--- | :--- |")
        b_specs = item.get('bachelorSpecialties', [])
        if b_specs:
            for b in b_specs:
                code = b.get('code') or '-'
                name = b.get('name') or b.get('sourceText', '-')
                md_lines.append(f"| `{code}` | {name} |")
        else:
            md_lines.append("| - | Göstərilməyib |")
        md_lines.append("")
        
        # Eligible master programs
        md_lines.append("**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**\n")
        m_specs = item.get('eligibleMasterPrograms', [])
        if m_specs:
            for mp in m_specs:
                m_code = mp.get('code') or ''
                m_name = mp.get('name') or ''
                spec_text = mp.get('specializationsText') or ''
                code_str = f" `{m_code}`" if m_code else ""
                md_lines.append(f"- **{code_str} {m_name}**".strip())
                if spec_text:
                    sub_lines = [s.strip() for s in spec_text.split('\n') if s.strip()]
                    for sub in sub_lines:
                        # don't repeat the header if it matches
                        if sub.lower() != m_name.lower():
                            md_lines.append(f"  - {sub}")
        else:
            md_lines.append("- Uyğun ixtisaslaşmalar qeyd olunub.")
        md_lines.append("")
        
        # University matches if any
        uni_matches = item.get('universityMatches', [])
        if uni_matches:
            md_lines.append("<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>\n")
            md_lines.append("| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |")
            md_lines.append("| :--- | :--- | :--- | :--- |")
            for u in uni_matches[:15]: # show up to 15
                u_name = u.get('university', '-')
                u_spec = u.get('specialty', '-')
                free = u.get('freeScore', '-')
                paid = u.get('paidScore', '-')
                md_lines.append(f"| {u_name} | {u_spec} | {free} | {paid} |")
            if len(uni_matches) > 15:
                md_lines.append(f"| *... və daha {len(uni_matches) - 15} təhsil müəssisəsi* | | | |")
            md_lines.append("\n</details>\n")
        
        md_lines.append("---\n")

content = "\n".join(md_lines)
with open('data.md', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"data.md generated successfully! Size: {len(content)} characters, {len(md_lines)} lines.")
