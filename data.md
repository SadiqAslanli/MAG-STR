# Magistratura Səviyyəsi Üzrə İxtisaslaşma Seçimi Cədvəli (DİM)

> **Mənbə:** Dövlət İmtahan Mərkəzi (DİM) — Magistr xüsusi buraxılışı / Scribd Sənədi (`733759124/2-5341821482265756298`)  
> **Məlumat:** 384 uyğunluq bloku, 40-dan çox qəbul proqramı, bakalavriat və magistratura ixtisaslaşmaları, minimal bal tələbləri və universitet keçid balları.

## 1. Scribd Saytından Data Scraping Metodu (Necə Çəkilir?)

Scribd sənədləri standart veb səhifələrdən fərqli olaraq mətnləri birbaşa tək HTML teqi daxilində saxlamır. Məlumatı çəkmək üçün aşağıdakı arxitektura istifadə olunur:

1. **CDN / JSONP Arxitekturası:** Scribd sənədin hər səhifəsini `https://html.scribdassets.com/{doc_id}/pages/{page_num}-{hash}.jsonp` formatında saxlayır.
2. **Səhifə Linklərinin Çıxarılması:** Əsas sənəd səhifəsindən (`https://www.scribd.com/document/733759124/...`) HTML endirilir və içərisindəki bütün `html.scribdassets.com` jsonp ünvanları regex vasitəsilə aşkarlanır.
3. **JSONP-dən HTML-ə Keçid:** Hər bir JSONP faylı `window.pageN_callback(["<html content>"])` şəklində gəlir. Python vasitəsilə JSON hissəsi ayrılır və səhifənin HTML DOM-u əldə edilir.
4. **Koordinat Əsaslı Cədvəl Bərpası:** Hər bir mətn elementi (span) `top` (şaquli) və `left` (üfüqi) pikselləri ilə yerləşdirilib. 4 əsas sütun (Bakalavr ixtisası, Magistratura ixtisaslaşması, Proqram №, Minimal bal) X və Y koordinatlarına görə qruplaşdırılaraq tam cədvələ çevrilir.

```python
# Nümunə: Scribd JSONP səhifəsindən mətn və koordinatların çəkilməsi
import requests, re, json

url = 'https://html.scribdassets.com/eoh9xur0gchwezt/pages/5-c40328b208.jsonp'
res = requests.get(url)
match = re.search(r'callback\(\s*(\[.*\])\s*\);?', res.text, re.DOTALL)
if match:
    html_content = json.loads(match.group(1))[0]
    # Cədvəl elementlərinin koordinatlarla oxunması...
```

## 2. Ümumi Qeydlər və Tələblər

- **`*` İxtisaslar:** Əvvəlki illərin təsnifatına uyğun ixtisas kodları.
- **`**` İxtisaslar:** Cari bakalavriat təsnifatı üzrə ixtisaslar.
- **Minimal Bal:** Bakalavrın müvafiq proqram üzrə ixtisaslaşma seçiminə buraxılması üçün magistratura qəbul imtahanında (və ya qabiliyyət imtahanında) toplamalı olduğu ən aşağı bal həddidir.

## 3. İxtisaslaşma Seçimi və Uyğunluq Cədvəli

### Proqram № 1

#### Blok 1 (Minimal bal: `45`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050506` | Geologiya |
| `050508` | Geologiya |
| `TE 090100` | Geologiya |
| `T 010600` | Tə tbiqi geokimya, petrologiya, mineralogiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Geokimya
  - niz və okean dibinin geologiyası
  - Regional geologiya
  - Paleontologiya və stratiqrafiya
  - Petrologiya
  - Mineralogiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Dəniz və okean dibinin geologiyası | None | 45 |
| Bakı Dövlət Universiteti | Mineralogiya | 51 | 51 |

</details>

---

### Proqram № 3

#### Blok 1 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050607` | Elektrik və elektronika mühəndisliyi |
| `050608` | Energetika mühəndisliyi |
| `050608` | Elektroenergetika mühəndisliyi |
| `050626` | Elektrik mühəndisliyi |
| `T 030100` | Elektrik stansiyaları |
| `T 030200` | Elektroenergetika lə ri |
| `T 120100` | Elektrik aparatları |
| `T 120200` | Elektroizolyasiya, kabel və kondensator texnikası naye qurğularının və texnoloji komplekslərin avtomatikası və elektrik intiqalı |
| `T 120400` | Elektrotexnoloji və ular və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060608` Elektroenergetika mühəndisliyi**
  - Elektroenergetika
  - Elektrik tə chizatı rüzrə )
  - sistemlə ri
  - Elektrik stansiyalarının elektrik hissə si
- ** `060626` Elektrik mühəndisliyi**
  - keçiricilə rin fizikası və texnikası
  - İzolyasiya materiallarının fizikası və texnikası
  - lə rinin elektrik avadanlığ ı və elektronikası(nə qliyyat
  - riüzrə )
  - Elektrik aparatları
  - riyyə si
  - naye qurğ uları texnoloji komplekslə rin avtomatikası və elektrik
  - intiqalı
  - Avtomatlaşdırılmı sistemlə r
  - rginliklə r texnikası və fiz ikası
  - Elektrik nə qliyyatı
  - Elektrik tə chizatının optimallaşdırılması dirilmə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Elektroenergetika | 44 | 44 |
| Azərbaycan Texniki Universiteti | Elektroenergetika | 51 | 51 |
| Bakı Mühəndislik Universiteti | Elektroenergetika | 41.5 | 40 |
| Milli Aviasiya Akademiyası | Elektroenergetika | 46 | 46 |
| Naxçıvan Dövlət Universiteti | Elektroenergetika | 43 | 40 |
| Mingəçevir Dövlət Universiteti | Elektroenergetika | 42 | 40 |
| Azərbaycan Texniki Universiteti | Davamlı elektroenergetika sistemləri | 47.5 | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Elektroenergetika (tədris Azərbaycan dilində) | None | 40 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Sumqayıt Dövlət Universiteti | Elektrik təchizatı (sahələr üzrə) | 44 | 40 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| *... və daha 119 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | rin avtomatlaşdırma elektroenerji sistemləri milə rin elektrik avadanlıqları və avtomatikası |
| `050604` | Cihaz mühəndisliyi |
| `050636` | Radiotexnika və telekommunikasiya mühəndisliyi |
| `050624` | Cihazqayırma mühəndisliyi |
| `050627` | Elektronika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060626` Elektrik mühəndisliyi**
  - rin elektroenerji sistemlə ri
- ** `060624` Cihazqayırma mühəndisliyi**
  - Kompüterli informasiya-ölçmə texnologiyaları
  - Aviasiya cihazları
  - sistemlə ri
  - radiotexnika mühəndisliyi
  - r və televiziya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Kompüter sistemləri və şəbəkələri | 69 | 69 |
| *... və daha 64 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `AT 060200` | Aqrar istehsalatın dirilmə si |
| `AT 060300` | Aqrar istehsalatın si və avtomatlaş d r lmas |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060706` Aqromühə ndislik**
  - Aqrar istehsalatı avtomatlaşdırılması
  - Aqrar istehsalatın avtomatlaşdırılması lə rinin istismarı miri və
  - servis xidmə ti

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060608` Elektroenergetika mühəndisliyi**
  - Elektrik tə chizatı rüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Elektroenergetika | 44 | 44 |
| Azərbaycan Texniki Universiteti | Elektroenergetika | 51 | 51 |
| Bakı Mühəndislik Universiteti | Elektroenergetika | 41.5 | 40 |
| Milli Aviasiya Akademiyası | Elektroenergetika | 46 | 46 |
| Naxçıvan Dövlət Universiteti | Elektroenergetika | 43 | 40 |
| Mingəçevir Dövlət Universiteti | Elektroenergetika | 42 | 40 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Sumqayıt Dövlət Universiteti | Elektrik təchizatı (sahələr üzrə) | 44 | 40 |

</details>

---

### Proqram № 4

#### Blok 1 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050609` | İstilik energetikası mühəndisliyi |
| `050610` | Enerji maşınqayırması mühəndisliyi |
| `T 040100` | İstilik elektrik stansiyaları |
| `T 040200` | İstilik elektrik stansiyalarında yanacaq və su texnologiyası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - İstilik elektrik stansiyaları
  - lə ri
  - Sə naye istilik energetikası
  - n proseslə rin istilik fizikası
- ** `060610` Enerji maşınqayırmasımühəndisliyi**
  - ri və onların texniki istismarı
  - Enerji maşınlarının istehsalı
  - Soyuducu maşı qurğ ular
  - Kompressor maş qurğ ular

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Elektrik stansiyaları | 45.5 | 45.5 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diferensial tənliklər İngilis dilində | 77 | 55.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk xalqları dilləri üzrə) | 65.5 | 57.5 |
| Bakı Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 75 | 75 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Asiya və Afrika ölkələrinin tarixi | 61 | 61 |
| Bakı Dövlət Universiteti | Slavyan ölkələri tarixi | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Qafqaz ölkələri üzrə) | None | 50 |
| *... və daha 210 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı ı
  - Enerji menecmenti
  - etmə
- ** `060609` İstilik energetikasımühəndisliyi**
  - lə ri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 67 | 67 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Optimallaşdırma və optimal idarəetmə | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Bakı Dövlət Universiteti | Nəşriyyat işi və redaktəetmə | None | 50 |
| Bakı Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | 68 | 60.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texniki sistemlərdə idarəetmə | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ümumi idarəetmə | None | 54.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ümumi idarəetmə İngilis dilində | None | 53.5 |
| Azərbaycan Texniki Universiteti | Texniki sistemlərdə idarəetmə | 59 | 59 |
| Azərbaycan Texniki Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 64 | 64 |
| *... və daha 258 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Elektrokimya
  - Bə rk cisim kimyası
  - lə r kimyası
  - Neft kimyası
  - Nanomateriallar kimyası
  - Kimyə vi ekspertiza
- ** `060609` İstilik energetikasımühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Elektrokimya | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Təbii və fizioloji fəal maddələr kimyası | 64 | 64 |
| Bakı Dövlət Universiteti | Polimer kimyası | 66.5 | 66.5 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| Bakı Dövlət Universiteti | Neft kimyası İngilis dilində | 64.5 | 55 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-kimya sintezinin texnologiyası | 64 | 64 |
| Sumqayıt Dövlət Universiteti | Neft kimyası | 51 | 51 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Materiallar kimyası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Kimyəvi ekspertiza | 73.5 | 73.5 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | texnologiyası lə rin texnologiyası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060609` İstilik energetikasımühəndisliyi**
  - ləri
  - n proseslə rin istilik fizikası
  - XTM 060004Çoxkanall troposfer rabitə sinin yerüstü aparatlar n n

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diferensial tənliklər İngilis dilində | 77 | 55.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk xalqları dilləri üzrə) | 65.5 | 57.5 |
| Bakı Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 75 | 75 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Asiya və Afrika ölkələrinin tarixi | 61 | 61 |
| Bakı Dövlət Universiteti | Slavyan ölkələri tarixi | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Qafqaz ölkələri üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Amerika ölkələri üzrə) İngilis dilində | None | 50 |
| *... və daha 207 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 5

#### Blok 1 (Minimal bal: `40`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050627` | Metallurgiya mühəndisliyi |
| `050611` | Metallurgiya mühəndisliyi |
| `T 050100` | Qara metalların metallurgiyası |
| `T 050200` | Ə lvan metalların metallurgiyası |
| `T 050300` | Faydalıqazıntıların dirilmə si ə lvan metalların üsulu ilə istehsalı |
| `T 050600` | Metalşünaslıq və metalların termiki emalı |
| `T 050700` | Qaynaqının metallurgiyası, texnologiyası və avadanlığ ı |
| `T 050800` | Kompozisiya və ovuntu materialları, örtüklər |
| `T 050900` | Metalları zyiqlə emalı |
| `T 051000` | Metallurji proseslə rin fiziki- vi tə dqiqatüsulları rin və materialların fiziki-kimyə vi tə dqiqatüsulları rüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060611` Metallurgiya mühəndisliyi**
  - Qara metalların metallurgiyası
  - lvan və nadir metalların metallurgiyası
  - Metalları rin tökmə istehsalı
  - Qaynaq istehsalımetallurgiyası, texnologiyası və avadanlığ ı
  - Ovuntu metallurgiyası, kompozisiya materialları örtükləri
  - Metalşünaslıq və metalların termiki emalı
  - Metalların tə zyiq altında emalı
- ** `060601` Materialşünaslıq mühəndisliyi**
  - Materialşünaslıq və materiallar texnologiyası
  - Maşınqayırma materialşünaslığ ı
  - Kompozisiya materialları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Əlvan və nadir metalların metallurgiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Azərbaycan Texniki Universiteti | Metalşünaslıq və metalların termiki emalı | 53.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq Alman dilində | None | 40 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | artırılmasıtexnologiyası və avadanlığ ı |
| `T 060700` | Texnoloji komplekslərin ndirilmə si |
| `T 060800` | Hidravlik maşınlar, hidrointiqallar və hidropnevmoavtomatika |
| `T 110100` | Texnoloji maşınlar və avadanlı rüzrə ) |
| `T 110200` | Poliqrafiya maşınları və avtomatlaşdırılmışş kompleksləri |
| `T 110300` | Qaldırıcınəqliyyat maşınları və avadanlıqları lərinin avtomatlaşdırılmışşşistehsalatları |
| `TT 100100` | Maşınları mliyi və dinamikası |
| `TT 180100` | Tribotexnika |
| `TT 200100` | Maddi istehsal |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060645` Poliqrafiya mühəndisliyi**
  - Poliqrafiya maşınları avtomatlaşdırılmı komplekslə r
- ** `060706` Aqromühə ndislik**
  - Heyvandarlığ ı r və aparatlar
  - Aqrar istehsalatın texniki tə minatı
  - Aqrar istehsalatı dirilməsi
- ** `060610` Enerji maşınqayırmasımühəndisliyi**
  - n qurğ ularının hidravlik sistemlə ri
- ** `060612` Maşın mühəndisliyi**
  - Maşınqayırma texnologiyası
  - Maşınqayırmada kompüter texnologiyaları
  - və qaynaq istehsalının maşın və avadanlıqları
  - Maşınqayı lərinin renovasiyası
  - Maşınların tə mir texnologiyası və servisi
  - Maşın istehsalıavadanlığ ı tlə r
  - li emal proseslə rinin texnologiyası ə maşınları
  - ndirilmə si
  - zgah sistemlə ri
  - bə rpa texnologiyalarımühəndisliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Poliqrafiya maşınları | 46 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası Alman dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları | 44.5 | 44.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları İngilis dilində | 51.5 | 40 |
| Bakı Mühəndislik Universiteti | Tökmə və qaynaq istehsalının maşın və avadanlıqları | None | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Maşınların təmir texnologiyası və servisi | 53 | 53 |
| Bakı Mühəndislik Universiteti | Maşınların təmir texnologiyası və servisi | 51 | 51 |
| Azərbaycan Texniki Universiteti | Yüksək səmərəli emal proseslərinin texnologiyası və maşınları | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Texnoloji komplekslərin layihələndirilməsi | 41 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası | 66.5 | 66.5 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası Türk dilində | 64 | 64 |
| Azərbaycan Dövlət İqtisad Universiteti | Mülkiyyət obyektlərinin qiymətləndirilməsi | 64 | 45 |
| *... və daha 3 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050623` | Materiallar mühəndisliyi |
| `050601` | Materialşünaslıq mühəndisliyi |
| `TT 170100` | Materialşünaslıq və yeni materiallar texnologiyas |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060611` Metallurgiya mühəndisliyi**
  - Qara metalların metallurgiyası
  - lvan və nadir metalların metallurgiyası
  - Metalları rin tökmə istehsalı
  - Qaynaq istehsalımetallurgiyası, texnologiyası və avadanlığ ı
  - Ovuntu metallurgiyası, kompozisiya materialları örtüklə ri
  - Metalşünaslıq və metalların termiki emalı
  - Metalların tə zyiq altında emalı
- ** `060601` Materialşünaslıq mühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Əlvan və nadir metalların metallurgiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Azərbaycan Texniki Universiteti | Metalşünaslıq və metalların termiki emalı | 53.5 | 40 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | silah sistemləri mühəndisliyi XTB |
| `050001` | Silah və silah sistemlərinin istehsal texnologiyası XTB |
| `050007` | Xüsusi tə yinatlıtexnika sistemlər XTB |
| `050101` | Silah və silah |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - və qaynaq istehsalının maşın və avadanlıqları
  - Maşınqayı lərinin renovasiyası
  - Maşınların tə mir texnologiyası və servisi
  - Maşın istehsalıavadanlığ ı tlə r
  - li emal proseslə rinin texnologiyası ə maşınları
  - ndirilmə si
  - bə rpa texnologiyalarımühəndisliyi
  - Metallurji tullantıların tə krar emal texnologiyaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Mühəndislik Universiteti | Tökmə və qaynaq istehsalının maşın və avadanlıqları | None | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Maşınların təmir texnologiyası və servisi | 53 | 53 |
| Bakı Mühəndislik Universiteti | Maşınların təmir texnologiyası və servisi | 51 | 51 |
| Azərbaycan Texniki Universiteti | Yüksək səmərəli emal proseslərinin texnologiyası və maşınları | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Texnoloji komplekslərin layihələndirilməsi | 41 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası | 66.5 | 66.5 |
| Azərbaycan Texniki Universiteti | Kompüter texnikasının layihələndirilməsi texnologiyası Türk dilində | 64 | 64 |
| Azərbaycan Dövlət İqtisad Universiteti | Mülkiyyət obyektlərinin qiymətləndirilməsi | 64 | 45 |
| Bakı Ali Neft Məktəbi | Yatağın qiymətləndirilməsi və idarə olunması İngilis dilində | 70 | 70 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimyəvi xidmət və keyfiyyətin qiymətləndirilməsi (tədris Azərbaycan dilində) | 38 | 30 |
| Azərbaycan Əmək və Sosial Münasibətlər Akademiyası | Mülkiyyət obyektlərinin qiymətləndirilməsi | None | 45 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | tə yinatlımə mulatların si və istehsalı XTB |
| `050105` | Kompozisiya materiallarından müdafiə tə yinatlımə mulatların si və istehsalı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Qara metalların metallurgiyası
  - lvan və nadir metalların metallurgiyası
  - Metalları rin tökmə istehsalı
  - Qaynaq istehsalımetallurgiyası, texnologiyası və avadanlığ ı
  - Ovuntu metallurgiyası, kompozisiya materialları örtüklə ri
  - Metalşünaslıq və metalların termiki emalı
  - Metalların tə zyiq altında emalı
- ** `060601` Materialşünaslıq mühəndisliyi**
  - Materialşünaslıq və materiallar texnologiyası
  - Maşınqayırma materialşünaslığ ı
- ** `060649` Ekologiya mühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Əlvan və nadir metalların metallurgiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Azərbaycan Texniki Universiteti | Metalşünaslıq və metalların termiki emalı | 53.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq Alman dilində | None | 40 |

</details>

---

### Proqram № 6

#### Blok 1 (Minimal bal: `40`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050622` | Maşın mühəndisliyi |
| `050628` | Mexanika mühəndisliyi |
| `050610` | Enerji maşınqayırması mühəndisliyi |
| `050612` | Maşın mühəndisliyi |
| `050625` | Texnoloji maşın və avadanlıqlar mühəndisliyi |
| `050630` | Mexanika mühəndisliyi |
| `050645` | Poliqrafiya mühəndisliyi bərpa texnologiyaları |
| `T 060100` | Maşınqayırma texnologiyası rüzrə ) |
| `T 060200` | Maşınqayırmada kompüter texnologiyası |
| `T 060300` | Tökmə istehsalının texnologiyası ə maşınları |
| `T 060400` | Texnoloji avadanlıqların si və istismarı |
| `T 060500` | Maşı lərinin bərpası möhkə mliyinin |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060625` Texnoloji maşın və avadanlıqlar mühəndisliyi**
  - Neft-qaz istehsalının maşın və avadanlıqları
  - Neft emalıvə kimya istehsalının maşın və avadanlıqları
  - şaat yol maşınlarıvə avadanlıqları
  - Yükqaldırıcımaşınlar və avadanlıqlar
  - tlə r
  - ə tinin texnoloji maşın və avadanlıqları
  - ətinin texnoloji maşın və avadanlıqları
  - və rezin emalının maşın və avadanlıqları
  - Texnoloji maşın və avadanlıqların istehsalı texniki xidmət
  - texnologiyası
- ** `060630` Mexanika mühəndisliyi**
  - əhidravlik maşınlar
  - Hidravlik maşınlar, hidrointiqrallar və hidropnevmoavtomatika
  - Maşı riyyəsi
  - Maye və qazların nəqli avadanlıqları
  - Tribotexnika
  - Maşınları mliyi və dinamikası
  - də n avadanlıqlarını xüsusi qurğ uların dinamikası möhkəmliyi
  - Yükqaldırıcımaşınların dinamikası möhkəmliyi
  - Maşınşünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Mühəndislik Universiteti | Tökmə və qaynaq istehsalının maşın və avadanlıqları | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-kimya maşın və avadanlıqları | 40.5 | 40 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya | 71 | 55 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | 68.5 | 51.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Azərbaycan Texniki Universiteti | Liftlər və eskalatorlar | None | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Mülkiyyət obyektlərinin qiymətləndirilməsi | 64 | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər və diplomatiya | 72 | 54 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 57 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | None | 50 |
| Bakı Mühəndislik Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 50 |
| *... və daha 75 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ndisliyi (dəmiryol nəqliyyatıüzrə ) |
| `T 100100` | Avtomobil və traktorlar lərinin texniki istismar |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Avtomobillə r
- ** `060706` Aqromühə ndislik**
  - Aqrar istehsalatı dirilmə si
  - ə qliyyatda daşınmaları kili mühəndisliyi

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 140400` | Mikroelektronika və yarımkeçirici cihazları |
| `T 140600` | Fiziki qurğuların elektronikası və avtomatikası |
| `T 140800` | İntroskopiyanın fizikiüsul və cihazları |
| `T 350100` | Elektron hesablayıcı rin konstruksiya edilmə si və texnologiyası |
| `T 150100` | Radiotexnika lə ri və televiziya |
| `T 150300` | nəqliyyat radioavadanlıqlarının texniki istismarı işə t radioelektron aparatları |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Sə naye elektronikası
  - Nə qliyyat radioavadanlıqlarının texniki istismarı
  - Elektronika və avtomatika
  - Güc elektronikası
  - Kommunikasi ya sistemlə ri
- ** `060624` Cihazqayırma mühəndisliyi**
  - Cihazqayırma texnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Sənaye elektronikası | 42 | 40 |
| Sumqayıt Dövlət Universiteti | Sənaye elektronikası | 69 | 40 |
| Azərbaycan Texniki Universiteti | Güc elektronikası | 43 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Güc elektronikası | 43.5 | 40 |
| Xəzər Universiteti | Güc elektronikası İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Texniki Universiteti | Çoxkanalh telekommunikasiya sistemləri | 52.5 | 52.5 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərində informasiya texnologiyaları | 67.5 | 67.5 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərində informasiya texnologiyaları İngilis dilində | 71 | 71 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Aerokosmik telekommunikasiyaasistemləri | 52 | 52 |
| Naxçıvan Dövlət Universiteti | Telekommunikasiya sistemlərində informasiya texnologiyaları | 57 | 57 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Telekommunikasiya sistemlərində informasiya texnologiyaları | 51 | 51 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050102` | Optotexnika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060624` Cihazqayırma mühəndisliyi**
  - Cihazqayırma texnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050602` | Aqromühəndisliyi |
| `050706` | Aqromühəndisliyi |
| `AT 060100` | Aqrar istehsalatın texnologiyası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060706` Aqromühə ndislik**
  - Heyvandarlığ ı r və aparatlar
  - Aqrar istehsalatın texniki tə minatı
  - Aqrar istehsalatı dirilmə si

---

### Proqram № 7

#### Blok 1 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050610` | gəmiqayı mi təmiri mühəndisliyi |
| `050618` | gəmiqayı mi təmiri mühəndisliyi |
| `T 080100` | gəmiqayı gəmi təmiri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060618` Də niz texnikası və texnologiyasımühəndisliyi**
  - Gə miqayırma
  - mi tə miri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmiqayırma | 48.5 | 48.5 |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmi təmiri | 45.5 | 45.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050605` | Də niz naviqasiyası mühəndisliyi |
| `050620` | Də niz naviqasiyası mühəndisliyi milə rin edilmə si |
| `050609` | gəmi energetik |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - edilmə si
  - edilmə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Su ehtiyatlarının inteqrasiyalı idarə edilməsi | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnologiyalar və əməliyyatların idarə edilməsi | 62.5 | 62.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya texnologiyalarının idarə edilməsi | None | 60 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya texnologiyalarının idarə edilməsi İngilis dilində | None | 58.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Əməliyyatların idarə edilməsi | None | 47.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Əməliyyatların idarə edilməsi İngilis dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyat əməliyyatlarının intellektual idarə edilməsi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Texniki Universiteti | Energetika sistemlərinin avtomatik idarə edilməsi | 54.5 | 40 |
| Azərbaycan Texniki Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Texniki Universiteti | Logistika əməliyyatlarının idarə edilməsi | None | 45 |
| Azərbaycan Texniki Universiteti | Logistika əməliyyatlarının idarə edilməsi Türk dilində | None | 45 |
| *... və daha 85 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | qurğularının istismarı mühəndisliyi mi energetik qurğularının istismarımühəndisliyi mi energetik qurğuları və onların istismarı ə mi maşın və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060619` Də niz texnikası və avadanlıqlarının istismarımühəndisliyi**
  - mi energetik qurğ uları və onların istismarı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Dəniz Akademiyası | Gəmi energetik qurğuları və onların istismarı | 46.5 | 40 |

</details>

---

### Proqram № 8

#### Blok 1 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | mexanizmlə ri qliyyat mühəndisliyi miryol nəqliyyatı və təsərrüfatımühəndisliyi ə qliyyatda daşımaların və nin təşkili ndisliyi (dəmiryol |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - miryol nə qliyyatı sə rrüfatımühəndisliyi
  - sə rrüfatı və onun istismarı
  - sə rrüfatı
  - ə mir yolu maşınlarının istehsalı texniki xidmə t texnologiyalar
  - sə rrüfatı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Dəmiryolu təsərrüfatı və onun istismarı | 54.5 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Dəmiryolu təsərrüfatı və onun istismarı | None | 40 |
| Azərbaycan Texniki Universiteti | Lokomotiv və vaqon təsərrüfatı | None | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin genetikası (tədris Azərbaycan dilində) | 39.5 | 39.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı heyvanlarının yetişdirilməsi, genetikası və seleksiyası (tədris Azərbaycan dilində) | 33.5 | 33.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu | 33.5 | 30 |
| Azərbaycan Texniki Universiteti | Texnoloji maşın və avadanlıqların istehsalı, təmiri və texniki xidmət texnologiyaları | 44.5 | 40 |

</details>

---

### Proqram № 9

#### Blok 1 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | qliyyat mühəndisliyi |
| `050622` | Yerüstü nəqliyyat rinin mühəndisliyi ə qliyyatda daşımaların və nin təşkili |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rinin mühəndisliyi
  - hlükə sizliyi
  - lə rinin avtotexniki ekspertizası
  - Avtomobil nə qliyyatının istismarı
  - t kompleksinin sertifikatlaşdırılması lisenziyalaşdırılması
  - mə liyyatlarını edilmə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 61.5 | 61.5 |
| Bakı Mühəndislik Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| *... və daha 17 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 10

#### Blok 1 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nəqliyyatıüzrə ) təsərrüfatı, onun istismarı |
| `T 090200` | Lokomotiv və vaqon təsərrüfatı ə qliyyatda daşımaların və kili (dəmiryol nəqliyyatüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ə qliyyatda daşınmaları kili mühəndisliyi
  - ə qliyyatda daşımalar və menecment
  - Nə qliyyat logistikası
  - tinin təş kili
  - nə qliyyat (SABAH)
  - ə lxalq avtomobil daşımaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Bakı Mühəndislik Universiteti | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 55.5 | 51.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 57 | 44.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Nəqliyyat logistikası | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyat logistikası | 55.5 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nəqliyyat logistikası | 56 | 56 |
| Milli Aviasiya Akademiyası | Nəqliyyat logistikası | 65 | 65 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası | None | 44 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Şəhər nəqliyyat şəbəkəsi və nəqliyyat xidmətinin təşkili | 59 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Naxçıvan Dövlət Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 58.5 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Yol hərəkətinin təşkili və təhlükəsizliyi | 51.5 | 40 |
| *... və daha 1 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | tinin təşkili ə qliyyatda daşımaların və nin təşkili (avtomobil nəqliyyatıüzrə ) |
| `050613` | Hava nəqliyyatının kə tinin təşkili nəqliyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ə qliyyatda daşı menecment (avtomobil nə qliyyatıüzrə )
  - Nə qliyyat logistikası
  - tinin təş kili
  - ə lxalq avtomobil daşımaları
  - nə qliyyat (SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Nəqliyyat logistikası | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyat logistikası | 55.5 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nəqliyyat logistikası | 56 | 56 |
| Milli Aviasiya Akademiyası | Nəqliyyat logistikası | 65 | 65 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası | None | 44 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Şəhər nəqliyyat şəbəkəsi və nəqliyyat xidmətinin təşkili | 59 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Naxçıvan Dövlət Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 58.5 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Yol hərəkətinin təşkili və təhlükəsizliyi | 51.5 | 40 |
| Mingəçevir Dövlət Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | None | 40 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 7)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | texnologiyalarımühəndisliyi |
| `050613` | Avianəqliyyat istehsalatının kili mühəndisliyi nəqliyyat texnologiyalarımühəndisliyi |
| `T 072400` | Avianəqliyyat istehsalatının təşD kili M - 2024 ə qliyyatda daşımaların və nin təşkili (hava nəqliyyatıüzrə ) ə qliyyatda daşımaların və nin təşkili (su nəqliyyatıüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ə qliyyatda daşınmaları kili mühəndisliyi
  - ə qliyyatda daşımalar və menecment
  - Nə qliyyat logistikası
  - tinin təş kili
  - nə qliyyat (SABAH)
  - edilmə si
  - ə lxalq avtomobil daşımaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Bakı Mühəndislik Universiteti | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 55.5 | 51.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 57 | 44.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Nəqliyyat logistikası | 57.5 | 57.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyat logistikası | 55.5 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Nəqliyyat logistikası | 56 | 56 |
| Milli Aviasiya Akademiyası | Nəqliyyat logistikası | 65 | 65 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası | None | 44 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyat logistikası İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Şəhər nəqliyyat şəbəkəsi və nəqliyyat xidmətinin təşkili | 59 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Naxçıvan Dövlət Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 58.5 | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Yol hərəkətinin təşkili və təhlükəsizliyi | 51.5 | 40 |
| *... və daha 101 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 22)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050407` | Marketinq |
| `050408` | Menecment naye mühəndisliyi idarə olunması |
| `050407` | Menecment |
| `050408` | Marketinq edilmə si edilmə si |
| `050403` | Davamlıinkişafın idarə edilmə si |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ə qliyyatda daşınmaları kili mühəndisliyi
  - nə qliyyat (SABAH)

---

### Proqram № 11

#### Blok 1 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | telekommunikasiya və radiotexnika mühəndisliyi |
| `T 130100` | Cihazqayırma t və diaqnostikaüsul və cihazları |
| `T 130300` | Aviasiya cihazları ölçmə - hesablama kompleksləri |
| `T 130900` | Kompüterli informasiya- ölçmə texnikası və texnologiyası |
| `T 131000` | Aerokosmik monitorinq |
| `T 131100` | Gömrük idxal-ixrac sistemləri |
| `T 140100` | Elektron texnikasının materialları komponentlə ri qurğuları |
| `T 140300` | Sə naye elektronikası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Radiotexnika
  - Radioelektron sistemlə r
  - işə t radioelektron aparatları
  - sistemlə ri
  - lə ri
  - qovşaqları kommutasiya sistemlə ri
  - Çoxkanallıtelekommunikasiya sistemlə ri
  - ri və informasiyanın paylanması
  - lə ri
  - Elektronika və avtomatika
  - k tezlikli texnika və texnologiya
  - hlükə sizliyi
  - Optik rabitə fizikası və texnikası
  - poçt rabitə si
  - qurğ ular

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Radiotexnika | 50 | 50 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| *... və daha 237 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | si və servis xidməti |
| `T 350200` | Radioelektronika lərinin konstruksiya si və texnologiyası |
| `TT 150100` | Optik rabitə fizikası ı və texnikasDı M - 2024 |
| `050604` | Cihaz mühəndisliyi |
| `050624` | Cihazqayırma mühəndisliyi |
| `050647` | Metrologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060624` Cihazqayırma mühəndisliyi**
  - Kompüterli informasiya-ölçmə texnologiyaları
- ** `060648` Biotibbi texnika mühəndisliyi**
  - sistemlə r

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diskret sistemlər | 61 | 61 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| *... və daha 86 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050629` | Mexatronika və robototexnika mühəndisliyi |
| `050634` | Proseslə rin avtomatlaş dırılması mühəndisliyi |
| `050628` | Proseslə rin avtomatlaşdırılması mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060624` Cihazqayırma mühəndisliyi**
  - Cihazqayırma texnologiyası
  - sistemlə ri
  - Kompüterli informasiya-ölçmə texnologiyaları
  - Aviasiya cihazları
  - radiotexnika mühəndisliyi
  - r və televiziya
  - Radiotexnika
  - Radioelektron sistemlə r
  - işə t radioelektron aparatları
  - sistemlə ri
  - lə ri
  - qovşaqları kommutasiya sistemlə ri
  - Çoxkanallıtelekommunikasiya sistemlə ri
  - ri və informasiyanın paylanması
  - lə ri
  - hlükə sizliyi
  - Optik rabitə fizikası və texnikası
  - poçt rabitə si
  - qurğ ular
  - Sə naye elektronikas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| *... və daha 242 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050604` | Cihaz mühəndisliyi |
| `050648` | Biotibbi texnologiya mühəndisliyi |
| `T 290300` | Biotexniki və tibbi aparat rin quraşdırılması, texniki istismarı və servis xidməti |
| `T 360100` | Biotexniki və tibbi sistemlər |
| `T 360200` | Bioloji-tibbi praktikada ndis işi |
| `T 360300` | Tibbi informasiya sistemləri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060624` Cihazqayırma mühəndisliyi**
  - Kompüterli informasiya-ölçmə texnologiyaları
  - Aviasiya cihazları
  - sistemlə ri
  - radiotexnika mühəndisliyi
  - r və televiziya
  - Radiotexnika
  - Radioelektron sistemlə r
  - işə t radioelektron aparatları
  - sistemlə ri
  - lə ri
  - qovşaqları kommutasiya sistemlə ri
  - Çoxkanallıtelekommunikasiya sistemlə ri
  - ri və informasiyanın paylanması
  - lə ri
  - Elektronika və avtomatika
  - k tezlikli texnika və texnologiya
  - hlükə sizliyi
  - Optik rabitə fizikası və texnikası
  - poçt rabitə si
  - qurğ ular
  - Sə naye elektronikası
  - Nə qliyyat radioavadanl qlar n n texniki istismar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Kompüter sistemləri və şəbəkələri | 69 | 69 |
| *... və daha 240 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | onları rriklərinin texniki istismarı |
| `T 071000` | Aviasiya rinin və pilotaj- naviqasiya komplekslərinin texniki istismarı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060624` Cihazqayırma mühəndisliyi**
  - Aviasiya cihazları

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050653` | Kosmik texnika mühəndisliyi etmə ri mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060624` Cihazqayırma mühəndisliyi**
  - Aviasiya cihazları
- ** `060631` Kompüter mühəndisliyi**
  - Dinamiki arxitekturalı lə ri
  - Kompüter texnikasını konstruksiya edilmə si
  - si sistemlə ri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `XTB 050004` | Çoxkanallıradiorele və troposfer rabitə sinin yerüstü aparatlarının hazırlanması, istismarı təmiri |
| `XTB 050104` | Çoxkanallıradiorele və troposfer rabitə sinin yerüstüİ aparatlarDının hazırlanması, M - 2024 istismarı təmiri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Radioelektron sistemlər
  - işə t radioelektron aparatları
  - sistemlə ri
  - lə ri
  - qovşaqları kommutasiya sistemlə ri
  - Çoxkanallıtelekommunikasiya sistemlə ri
  - ri və informasiyanın paylanması
  - ləri
  - hlükə sizliyi
  - Optik rabitə fizikasıvə texnikası
  - poçt rabitə si
  - qurğ ular
  - Sə naye elektronikası
  - Nəqliyyat radioavadanlıqlarının texniki istismarı
  - Elektronika və avtomatika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Kompüter sistemləri və şəbəkələri | 69 | 69 |
| *... və daha 238 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | qrafikası və reklam) |
| `050607` | Elektrik və elektronika mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - radiotexnika mühəndisliyi
  - Nə qliyyat radioavadanlıqlarının texniki istismarı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Radiotexnika | 50 | 50 |

</details>

---

#### Blok 9 (Minimal bal: `40`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050630` | Mühə ndis fizikası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060624` Cihazqayırma mühəndisliyi**
  - Aviasiya cihazları
  - sistemlə r

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diskret sistemlər | 61 | 61 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| *... və daha 86 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 12

#### Blok 1 (Minimal bal: `40`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050507` | Hidrometeorologiya |
| `050507` | Hidrometeorologiya |
| `TE 070300` | Meteorologiya və iqlimşünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Sosial pedaqogika
  - və monitorinq
- ** `060507` Hidrometeorologiya**
  - Aviasiya meteorologiyası
  - qlimşünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Aviasiya meteorologiyası | 46 | 46 |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050507` | Hidrometeorologiya |
| `050507` | Hidrometeorologiya |
| `TE 070100` | Okeanologiya |
| `TE 070400` | Hidrologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Hidrologiya
- ** `060507` Hidrometeorologiya**
  - Su ehtiyatlarının inteqrasiyalı edilmə si
  - Fiziki okeanologiya
- ** `060508` Geologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Hidrologiya və su ehtiyatları | None | 45 |
| Bakı Dövlət Universiteti | Su ehtiyatlarının inteqrasiyalı idarə edilməsi | None | 45 |
| Bakı Dövlət Universiteti | Dəniz və okean dibinin geologiyası | None | 45 |
| Bakı Dövlət Universiteti | Faydalı qazıntı yataqlarının hidrogeologiyası və mühəndis geologiyası | 43 | 43 |
| Bakı Dövlət Universiteti | Geomorfologiya | 56 | 56 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-qaz-mədən geologiyası | 42 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Faydalı qazıntı yataqlarının hidrogeologiyası və mühəndis geologiyası | None | 40 |

</details>

---

### Proqram № 13

#### Blok 1 (Minimal bal: `30`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 120600` | Elektrik nəqliyyatı lərinin elektronikası və elektrik avadanlığ ı |
| `T 121200` | Zavoddaxili elektrik avadanlıqları lər üzrə ) gəgərginliklər texnikası və fizikası |
| `TT 140200` | Elektrotexnoloji sistemlər |
| `T 030400` | Elektrik təchizatı lər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rin elektroenerji sistemlə ri
- ** `060706` Aqromühə ndislik**
  - Aqrar istehsalatı avtomatlaşdırılması
  - Aqrar istehsalatı lə rinin istismarı miri və
  - servis xidmə ti
  - rin avtomatlaş dırılmasımühəndisliyi
  - Enerji menecmenti

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | informasiya texnikası(Tempus proqramı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ri və texnologiyaları(SABAH)
  - robototexnika mühəndisliyi
  - robototexniki sistemlə r
  - Süni intellekt (SABAH)
  - Mexatronika
  - inteqrallaşdırılmışistehsalat
  - rin avtomatlaş dırılmasımühəndisliyi
  - rin və istehsalatın avtomatlaşdırılması
  - mir yolu nə qliyyatı rabitə
  - edilmə si
  - rin avtomatlaşd r lmas edilmə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Robotlar və robototexniki sistemlər | 62.5 | 62.5 |
| Azərbaycan Texniki Universiteti | Robotlar və robototexniki sistemlər | 64 | 64 |
| Azərbaycan Texniki Universiteti | Robotlar və robototexniki sistemlər İngilis dilində | 68 | 68 |
| Azərbaycan Texniki Universiteti | Süni intellekt | 73.5 | 73.5 |
| Azərbaycan Texniki Universiteti | Mexatronika | 63 | 63 |
| Bakı Dövlət Universiteti | Su ehtiyatlarının inteqrasiyalı idarə edilməsi | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnologiyalar və əməliyyatların idarə edilməsi | 62.5 | 62.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya texnologiyalarının idarə edilməsi | None | 60 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya texnologiyalarının idarə edilməsi İngilis dilində | None | 58.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Əməliyyatların idarə edilməsi | None | 47.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Əməliyyatların idarə edilməsi İngilis dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyat əməliyyatlarının intellektual idarə edilməsi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| *... və daha 90 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nmə sinin etmə nin avtomatlaşdırılmışş sistemləri |
| `T 180400` | avtomatlaşdırılmışşş rin və hesablama texnikasının proqram tə minatı |
| `T 180500` | Mə lumatların mühafizəsinin texnologiyası və təşkili tətəhlükəsizliyi nformasiya sistemləri riüzrə ) |
| `TE 100100` | Tə tbiqi riyaziyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - etmə nin informasiya texnologiyaları
  - informasiya tə minatı
  - dirmə
  - Sistem proqramlaşdırılması
  - rinin proqram tə minatı
  - İnformatika
  - Tə tbiqi riyaziyyat
  - etmə nin riyazi-iqtisadiüsulları
  - hlükə sizliyi
  - msal hökumə t
  - tbiqlə rin hazırlanması və oyun dizaynı
  - ri və texnologiyaları(SABAH)
  - rin tə hlili (Data analitikas )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya texnologiyalarının idarə edilməsi | None | 60 |
| Azərbaycan Texniki Universiteti | Logistikada informasiya texnologiyaları | 64.5 | 64.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnformasiya texnologiyalarının idarə edilməsi | None | 58.5 |
| “Odlar Yurdu” Universiteti | İnformasiya texnologiyalarının idarə edilməsi | None | 47.5 |
| Bakı Dövlət Universiteti | Riyazi modelləşdirmə | 64 | 64 |
| Bakı Dövlət Universiteti | İqtisadi-riyazi modelləşdirmə | 64 | 55 |
| Bakı Dövlət Universiteti | Təhsildə monitorinq və qiymətləndirmə | 80 | 80 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 66 | 66 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə İngilis dilində | None | 55.5 |
| Bakı Dövlət Universiteti | Stoxastik modelləşdirmə | 61 | 61 |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi Türk dilində | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Riyazi modelləşdirmə | 62.5 | 62.5 |
| *... və daha 53 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 14

#### Blok 1 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 170400` | Energetika sistemlərinin edilmə si |
| `T 170900` | Uçuşlara avtomatlaşdırılmışş zarə t sistemlərinin istismarı |
| `T 171000` | avtomatlaşdırılmışşş sistemlərin informasiya tətəhlükəsizliyinin kompleks tə minatı |
| `T 180700` | avtomatlaşdırma və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Dinamiki arxitekturalı lə ri
  - Kompüter texnikasını konstruksiya edilmə si
  - si sistemlə ri
  - hlükə sizliyi
  - lə ri
- ** `060632` İnformasiya texnologiyaları ri mühəndisliyi**
  - İnformasiya texnologiyaları telekommunikasiya sistemlə ri
  - informasiya sistemlə ri
  - nin avtomatlaşdırılmı sistemlə ri
  - tbiqi proqram tə minatı
  - Aerokosmik informasiya sistemlə ri
  - İqtisadi informatika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 61.5 | 61.5 |
| *... və daha 222 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050509` | Kompüter elmlə ri tətəhlükəsizliyi |
| `050616` | İnformasiya texnologiyaları |
| `050620` | Kompüter mühəndisliyi |
| `050509` | Kompüter elmlə ri |
| `050631` | Kompüter mühəndisliyi |
| `050632` | İnformasiya texnologiyaları sistemləri mühəndisliyi |
| `050655` | İnformasiya texnologiyaları |
| `050656` | Sistem mühəndisliyi |
| `T 180100` | Hesablama maşınları, ri və lə ri |
| `T 180200` | avtomatlaşdırılmışşş sistemləri rüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060631` Kompüter mühəndisliyi**
  - Dinamiki arxitekturalı lə ri
  - Kompüter texnikasını konstruksiya edilmə si
  - si sistemlə ri
  - hlükə sizliyi
  - lə ri
- ** `060632` İnformasiya texnologiyaları ri mühəndisliyi**
  - hlükə sizliyi
  - İnformasiya texnologiyaları telekommunikasiya sistemlə ri
  - informasiya sistemlə ri
  - nin avtomatlaşdırılmı sistemlə ri
  - tbiqi proqram tə minatı
  - Aerokosmik informasiya sistemlə ri
  - İqtisadi informatika
  - hlükə sizlik (SABAH)
  - hlükə sizliyi
  - Mə lumatları sinin təş kili
- ** `060509` Kompüter elmlə ri**
  - ntellektual sistemlə r
  - rin idarə olunması
  - nformasiya sistemlə ri
  - qtisadi informasiya sistemlə ri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 61.5 | 61.5 |
| *... və daha 228 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - hlükə sizliyi
  - lə ri
- ** `060632` İnformasiya texnologiyaları ri mühəndisliyi**
  - hlükə sizliyi
  - İnformasiya texnologiyaları telekommunikasiya sistemlə ri
  - informasiya sistemlə ri
  - nin avtomatlaşdırılmı sistemlə ri
  - tbiqi proqram tə minatı
  - Aerokosmik informasiya sistemlə ri
  - İqtisadi informatika
- ** `060509` Kompüter elmlə ri**
  - ntellektual sistemlə r
  - rin idarə olunması
  - nformasiya sistemlə ri
  - qtisadi informasiya sistemlə ri
  - etmə nin informasiya texnologiyaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 61.5 | 61.5 |
| Bakı Mühəndislik Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| *... və daha 231 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `45`, Səhifə: 23)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nformatika müəllimliyi |
| `TE 010100` | Riyaziyyat |
| `TE 010200` | Tə tbiqi riyaziyyat |
| `TE 100100` | Tə tbiqi riyaziyyat |
| `TE 100200` | İnformatika |
| `M 010200` | Riyaziyyat və informatika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - informasiya tə minatı
  - dirmə
  - Sistem proqramlaşdırılması
  - rinin proqram tə minatı
  - etmə nin riyazi-iqtisadiüsulları
  - İnformatika
  - Tə tbiqi riyaziyyat
  - hlükə sizliyi
  - msal hökumə t
  - tbiqlə rin hazırlanması və oyun dizaynı
  - nformatika mü ə llimliyi
  - nninin tə drisi metodikası və metodologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Riyazi modelləşdirmə | 64 | 64 |
| Bakı Dövlət Universiteti | İqtisadi-riyazi modelləşdirmə | 64 | 55 |
| Bakı Dövlət Universiteti | Təhsildə monitorinq və qiymətləndirmə | 80 | 80 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 66 | 66 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə İngilis dilində | None | 55.5 |
| Bakı Dövlət Universiteti | Stoxastik modelləşdirmə | 61 | 61 |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi Türk dilində | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Riyazi modelləşdirmə | 62.5 | 62.5 |
| Azərbaycan Texniki Universiteti | İqtisadi-riyazi modelləşdirmə | 65.5 | 46 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsildə monitorinq və qiymətləndirmə | 68.5 | 68.5 |
| Azərbaycan Dillər Universiteti | Təhsildə monitorinq və qiymətləndirmə | 73.5 | 73.5 |
| Naxçıvan Dövlət Universiteti | Kompüter modelləşdirməsi | 55 | 55 |
| *... və daha 49 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 15

#### Blok 1 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050633` | Memarlıq hə rsalma |
| `T 190100` | Memarlıq |
| `T 190200` | MemarlD q mühitinin M - 2024 dizaynı |
| `T 190300` | Memarlı lərinin bərpası yenidə n qurulması landşaft quruculuğ u |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060633` Memarlıq**
  - qurğ uların memarlığ ı
  - hə rsalma
  - Memarlı rinin bə rpası yenidə n qurulması
  - Landşaft memarlığ ı
  - Memarlıq mühitinin dizaynı
  - hə rsalma
  - Dayanıqlı region planlaşdırılması

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq mühitinin dizaynı | 43.5 | 43.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası | 46 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası İngilis dilində | 56 | 56 |
| Bakı Mühəndislik Universiteti | Memarlıq mühitinin dizaynı | 49 | 49 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Memarlıq abidələrinin mühafizəsi və bərpası | 51.5 | 40 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Naxçıvan Dövlət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 64.5 | 43 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Bina və qurğuların memarlığı | 41 | 41 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Bina və qurğuların memarlığı İngilis dilində | 58.5 | 58.5 |
| Bakı Mühəndislik Universiteti | Bina və qurğuların memarlığı | 41 | 41 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 55.5 | 55.5 |
| Naxçıvan Dövlət Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 58 | 58 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Landşaft memarlığı | 40 | 40 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 19)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | u və torpaq ttişliyi |
| `AT 050200` | Torpaq kadastrı hə r kadastrı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Torpaq kadastrı
  - hə r kadastrı
  - hə rsalma

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 55.5 | 55.5 |
| Naxçıvan Dövlət Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 58 | 58 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 22)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050405` | İqtisadiyyat |
| `050408` | Menecment aat mühəndisliyi hə rsalma |
| `050404` | İqtisadiyyat diyyə etmə si ə daşınmaz ə mlakın kadastrı |
| `050407` | Menecment edilmə si |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - hə rsalma
  - Dayanıqlı region planlaşdırılması(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 55.5 | 55.5 |
| Naxçıvan Dövlət Universiteti | Dayanıqlı şəhərsalma və regionların planlaşdırılması | 58 | 58 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060633` Memarlıq**
  - Memarlı rinin bə rpası yenidə n qurulması
  - Memarlıq mühitinin dizaynı
- ** `060321` Dizayn**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq mühitinin dizaynı | 43.5 | 43.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası | 46 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası İngilis dilində | 56 | 56 |
| Bakı Mühəndislik Universiteti | Memarlıq mühitinin dizaynı | 49 | 49 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Memarlıq abidələrinin mühafizəsi və bərpası | 51.5 | 40 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Naxçıvan Dövlət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 64.5 | 43 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnteryer dizaynı | 52 | 44.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Qrafik dizayn | 52.5 | 37 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Vizual dizayn | 52 | 30 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texniki dizayn | None | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | Geyim dizaynı | None | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | İnteryer dizaynı | 52.5 | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | Qrafik dizayn | 52.5 | 46 |
| *... və daha 16 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050321` | Dizayn |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060633` Memarlıq**
  - Memarlıq mühitinin dizaynı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq mühitinin dizaynı | 43.5 | 43.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası | 46 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası İngilis dilində | 56 | 56 |
| Bakı Mühəndislik Universiteti | Memarlıq mühitinin dizaynı | 49 | 49 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Memarlıq abidələrinin mühafizəsi və bərpası | 51.5 | 40 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Naxçıvan Dövlət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 64.5 | 43 |

</details>

---

### Proqram № 16

#### Blok 1 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 030500` | Elektroenergetika siüzrə ) |
| `050607` | Elektrik və elektronika mühəndisliyi |
| `050608` | Energetika mühəndisliyi |
| `050608` | Elektroenergetika mühəndisliyi |
| `050609` | İstilik energetikası mühəndisliyi |
| `050626` | Elektrik mühəndisliyi |
| `050608` | Energetika mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - qurğ ularının tikintisi mühəndisliyi
  - hə r infrastrukturunda smart teı
- ** `060609` İstilik energetikas mü hə ndisliyi**

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 5)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 040300` | Sə naye istilik energetikasİ ı |
| `T 040400` | İstilik texnologiyasının energetikası rriklə ri |
| `T 041000` | bərpaolunan enerji lə ri |
| `T 041200` | Soyuducu maşın və qurğular, havanın |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı
  - rin avtomatlaş dırılmasımühəndisliyi
  - Enerji menecmenti

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 9)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050629` | Mexatronika və robototexnika mühəndisliyi miryol nəqliyyatında avtomatika, telemexanika və rabitə rdə və informatika rin və istehsalatların avtomatlaşdırılması lər üzrə ) |
| `T 170300` | Robotlar və robototexniki |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Nə qliyyat radioavadanlıqlarının texniki istismarı
  - Elektronika və avtomatika
  - Güc elektronikası
  - k tezlikli texnika və texnologiya
  - rin avtomatlaş dırılmasımühəndisliyi
  - Enerji menecmenti
  - qurğ ularının tikintisi mühəndisliyi
  - hə r infrastrukturunda smart texnologiyaları
- ** `060631` Kompüter mühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Güc elektronikası | 43 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Güc elektronikası | 43.5 | 40 |
| Xəzər Universiteti | Güc elektronikası İngilis dilində | None | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Şəhər infrastrukturunda ağıllı texnologiyalar | None | 44.5 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050632` | İnformasiya texnologiyaları sistemləri mühəndisliyi |
| `050626` | Memarlıq hə rsalma |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - qurğ ularının tikintisi mühəndisliyi
  - hə r infrastrukturunda smart texnologiyaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Şəhər infrastrukturunda ağıllı texnologiyalar | None | 44.5 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | aat mühəndisliyi |
| `050625` | Meliorasiya mühəndisliyi aat mühəndisliyi |
| `050637` | Meliorasiya və su təsərrüfatıtikintisi mühəndisliyi naye və mülki tikinti |
| `T 200200` | Hidrotexniki tikinti diyyə tikintisi təsərrüfatı |
| `T 200400` | Meliorasiya mühə ndis sistemlərinin tikintisi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - aat mühəndisliyi
  - naye və mülki tikinti
  - qurğ uları kili və texnologiyası
  - Daşınmazə mlakın idarə olunması və ekspertizası
  - qurğ uların dinamikası yə davamlılığ ı
  - özüllə rin tikintisi
  - riyyə si
  - Metal konstruksiyaları
  - aat mühəndisliyi
  - sə rrüfatıtikintisi mühəndisliyi
  - Hidrotexniki tikinti
  - ri tikintisi və istismarı
- ** `060628` Proseslə rin a vtomatlaş dırılmasımühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Sənaye və mülki tikinti | 60.5 | 60.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Sənaye və mülki tikinti İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Bina və qurğuların tikintisinin təşkili və texnologiyası | 56.5 | 56.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Daşınmaz əmlakın ekspertizası | 55.5 | 55.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Bina və qurğuların dinamikası və zəlzələyə davamlılığı | 54 | 54 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| *... və daha 30 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `45`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 380100` | Daşınmazə mlakın idarə si və ekspertizası |
| `050619` | Kommunikasiya ri mühəndisliyi rinin və qurğularının tikintisi mühəndisliyi stilik-qaz təchizatı və ventilyasiya |
| `T 210200` | Su təchizatı və suayırma |
| `T 210300` | Xüsusi mühə ndis qurğular n n |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Enerji menecmenti
  - idarə olunması
  - nin idarə olunması
  - qurğ ularının tikintisi mühəndisliyi
  - lə ri
  - hə r infrastrukturunda smart texnologiyaları
  - Su tə chizatı
  - qurğ uları n sistemlə r
  - Çirkab sularını narlaşdırılması nmə si
  - stilik-qaz tə chizatı
  - rin avtomatlaş dırılmasımühəndisliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 51 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması | None | 54 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi İngilis dilində | 58.5 | 54 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Fövqəladə halların idarə olunması | 51 | 42 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnsan resurslarının idarə olunması | None | 55 |
| Azərbaycan Dövlət İqtisad Universiteti | Brendin idarə olunması | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 58 |
| Bakı Mühəndislik Universiteti | İnsan resurslarının idarə olunması | None | 49.5 |
| Milli Aviasiya Akademiyası | Aviasiya təhlükəsizliyinin idarə olunması | 62.5 | 48.5 |
| Milli Aviasiya Akademiyası | Hava nəqliyyatı hərəkətinin idarə olunması İngilis dilində | None | 40 |
| *... və daha 237 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050633` | nəqliyyat tikintisi mühəndisliyi |
| `050636` | nəqliyyat tikintisi mühəndisliyi mir yolu tikintisi və təsərrüfatı |
| `T 220200` | Avtomobil yolları və aerodromların tikintisi nəqliyyat tunellərinin tikintisi |
| `050623` | Materiallar mühəndisliyi |
| `050638` | Tikinti materialları və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Enerji menecmenti
  - qliyyat tikintisi mühəndisliyi
  - Avtomobil yolları və aerodromların tikintisi
  - qliyyat qurğ ularının tikintisi
  - Də mir yollarını sə rrüfatı
  - qurğ ularını ə ndi sliyi
  - hə r infrastrukturunda smart texnologiyaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Avtomobil yolları və aerodromlar | 40 | 40 |
| Bakı Mühəndislik Universiteti | Avtomobil yolları və aerodromlar | None | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Şəhər infrastrukturunda ağıllı texnologiyalar | None | 44.5 |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 11)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | mə mulatlarının texnologiyası mühəndisliyi |
| `050639` | Meşə materiallarının və ağ ac emalının texnologiyası mühəndisliyi |
| `T 230100` | Tikinti materialları, mə mulatları və konstruksiyalarıistehsalı riyə n qeyri-metal və silikat materiallar texnologiyası |
| `T 260300` | Ağ ac emalıtexnologiyası |
| `T 281400` | Çini-saxsı ü şə mə mulatlar texnologiyas |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060601` Materialşünaslıq mühəndisliyi**
  - Materialşünaslıq və materiallar texnologiyası
- ** `060638` Tikinti materialları mə mulatlarının texnologiyasımühəndisliyi**
  - Tikinti materialları və konstruksiyalarının texnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |

</details>

---

#### Blok 9 (Minimal bal: `40`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Materialşünaslıq və materiallar texnologiyası
  - Maşınqayırma materialşünaslığ ı
- ** `060601` Materialşünaslıq mühəndisliyi**
  - Materialşünaslıq və materiallar texnologiyası(inşaat materiallarıüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Materialşünaslıq və materiallar texnologiyası | 41 | 40 |
| Bakı Mühəndislik Universiteti | Materialşünaslıq və materiallar texnologiyası | None | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada materialşünaslıq Alman dilində | None | 40 |

</details>

---

#### Blok 10 (Minimal bal: `40`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | edilmə si diyyə etmə si |
| `050405` | Dİqtisadiyyat M - 2024 |
| `050404` | İqtisadiyyat edilmə si diyyə etmə si |
| `050412` | Davamlıinkişafın idarə |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - aat mühəndisliyi
  - Daşınmazə mlakın idarə olunması və ekspertizası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Daşınmaz əmlakın ekspertizası | 55.5 | 55.5 |

</details>

---

### Proqram № 17

#### Blok 1 (Minimal bal: `40`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050612` | Geomatika və geodeziya mühəndisliyi ritə çilik mühəndisliyi |
| `T 240100` | Tə tbiqi geodeziya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - çilik mühəndisliyi
  - Tə tbiqi geodeziya
  - ritə çilik
  - Geomatika
  - hə r kadastrı
  - ttişliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tətbiqi geodeziya | 47 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tətbiqi geodeziya | 44 | 40 |
| Bakı Dövlət Universiteti | Geomatika | 44 | 40 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 19)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `AT 040100` | Baytarlıq |
| `AT 040200` | Baytarlıqə czaç ılığ ı ə daşınmaz ə mlakın kadastrı u, torpaq və hə r kadastrı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - liklə r
  - Mamalıq, ginekologiya və süni mayalanma
  - Baytarlı rrahiyyə si
  - Baytar-sanitar ekspertizası
  - Baytarlıqə czaç ılığ ı
  - çilik mühəndisliyi
  - Tə tbiqi geodeziya
  - Geomatika
  - hə r kadastrı
  - ttişliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Diferensial tənliklər | 69 | 69 |
| Bakı Dövlət Universiteti | Diferensial tənliklər İngilis dilində | 77 | 55.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Yüksək gərginliklər texnikası | 43.5 | 43.5 |
| Azərbaycan Texniki Universiteti | Yüksək gərginliklər texnikası | 43.5 | 40 |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Heyvanların yoluxmayan daxili xəstəlikləri (tədris Azərbaycan dilində) | 43.5 | 43.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Heyvanların yoluxucu xəstəlikləri və profilaktikası (tədris Azərbaycan dilində) | 37 | 37 |
| Gəncə Dövlət Universiteti | Diferensial tənliklər | 52 | 45 |
| Sumqayıt Dövlət Universiteti | Diferensial tənliklər | 53.5 | 53.5 |
| Lənkəran Dövlət Universiteti | Baytarlıq təbabətində mamalıq- ginekologiya və süni mayalanma | None | 30 |
| Naxçıvan Dövlət Universiteti | Baytarlıq cərrahiyyəsi | 43 | 30 |
| Lənkəran Dövlət Universiteti | Baytarlıq sanitariya-ekspertizası | 37 | 30 |
| Bakı Dövlət Universiteti | Tətbiqi geodeziya | 47 | 47 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tətbiqi geodeziya | 44 | 40 |
| Bakı Dövlət Universiteti | Geomatika | 44 | 40 |

</details>

---

### Proqram № 18

#### Blok 1 (Minimal bal: `30`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Torpaq kadastrı
  - hə r kadastrı
- ** `060641` Kimya mühəndisliyi**
  - Neft-kimyaı
  - Ə sasüzvi sintezin kimyası və texnologiyası
  - lə rin istehsal texnologiyası
  - Neft emalıtexnologiyası
  - Karbohidrogen qazların emalıtexnologiyası
  - rin kimyə vi texnologiyası
  - rin və kompozisiya materiallarının emalıtexnologiyası
  - Kimya texnologiyasının proses və aparatları
  - Neft-kimya proseslə rinin kibernetikası
  - dirilmə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar | 57.5 | 57.5 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar İngilis dilində | 65 | 63.5 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| Sumqayıt Dövlət Universiteti | Neft kimyası | 51 | 51 |
| Bakı Mühəndislik Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | 59 | 54.5 |
| Bakı Mühəndislik Universiteti | Əsas üzvi sintezin kimyası və texnologiyası İngilis dilində | 70.5 | 40 |
| Sumqayıt Dövlət Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qeyri-üzvi maddələrin istehsal texnologiyası | 55.5 | 53.5 |
| Bakı Dövlət Universiteti | Neft emalı texnologiyası | 66.5 | 66.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft emalı texnologiyası | 68.5 | 68.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft emalı texnologiyası İngilis dilində | 69.5 | 69.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Karbohidrogen qazların emalı texnologiyası | 56 | 56 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Polimerlərin kimyəvi texnologiyası | 56.5 | 56.5 |
| Sumqayıt Dövlət Universiteti | Polimerlərin kimyəvi texnologiyası | 64 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Polimer əsaslı kompozit materialların emalı texnologiyası | 56.5 | 56.5 |
| *... və daha 13 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 25)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050109` | Kimya müəllimliyi |
| `050508` | Kimya |
| `050504` | Kimya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Kimyə vi ekspertiza
- ** `060110` Kimya mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası
- ** `060641` Kimya mühəndisliyi**
  - Neft-kimya sintezinin texnologiyası
  - Ə sasüzvi sintezin kimyası və texnologiyası
  - lə rin istehsal texnologiyası
  - Neft emalıtexnologiyası
  - rin kimyə vi texnologiyası
  - rin və kompozisiya materiallarının emalıtexnologiyası
  - Kimya texnologiyasının proses və aparatları
  - Neft-kimya proseslə rinin kibernetikası
  - dirilmə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi ekspertiza | 73.5 | 73.5 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar | 57.5 | 57.5 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar İngilis dilində | 65 | 63.5 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-kimya sintezinin texnologiyası | 64 | 64 |
| Sumqayıt Dövlət Universiteti | Neft kimyası | 51 | 51 |
| Bakı Mühəndislik Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | 59 | 54.5 |
| Bakı Mühəndislik Universiteti | Əsas üzvi sintezin kimyası və texnologiyası İngilis dilində | 70.5 | 40 |
| Sumqayıt Dövlət Universiteti | Əsas üzvi sintezin kimyası və texnologiyası | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qeyri-üzvi maddələrin istehsal texnologiyası | 55.5 | 53.5 |
| Bakı Dövlət Universiteti | Neft emalı texnologiyası | 66.5 | 66.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft emalı texnologiyası | 68.5 | 68.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft emalı texnologiyası İngilis dilində | 69.5 | 69.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Polimerlərin kimyəvi texnologiyası | 56.5 | 56.5 |
| Sumqayıt Dövlət Universiteti | Polimerlərin kimyəvi texnologiyası | 64 | 40 |
| *... və daha 14 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 19

#### Blok 1 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 150500` | Radioelektron sistemləri |
| `T 150600` | Radioelektron mübarizə lə ri qovşaqları və kommutasiya sistemləri poçt rabitə si |
| `T 160300` | Çoxkanallı telekommunikasiyaə ri sistemləri və informasiyanın paylanması tedə n obyekti olan lə ri |
| `T 160700` | sistemlərinin informasiya tətəhlükəsizliyi işə t radioelektron aparatlarına servis xidməti şə t maşın və cihazlarının |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060649` Ekologiya mühəndisliyi**
  - Aerokosmik monitorinq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050618` | Kimya mühəndisliyi |
| `050641` | Kimya mühəndisliyi rin kimyə vi texnologiyası lə rin kimyə vi texnologiyası |
| `T 250300` | Elektrokimyə vi istehsal texnologiyası |
| `T 250400` | Neft-qaz və alternativ enerji texnologiyası |
| `T 250500` | Yüksə kmolekullu rin kimyə vi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Neft və qaz texnologiyası
- ** `060649` Ekologiya mühəndisliyi**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizə si
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Aerokosmik monitorinq
  - Nə qliyyat ekologiyası
- ** `060510` Ekologiya**
  - traf mühitin mühafizə metodları bə rpası
  - tin mühafizə si
  - Bioekologiya
  - traf mühitin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Ali Neft Məktəbi | Neft və qaz texnologiyası İngilis dilində | 75 | 75 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| *... və daha 17 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060708` Meşə çilik**
  - quruluşu
  - Meşə taksasiyası
  - kinlə ri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Ümumi meşəçilik və meşələrin idarə olunması (tədris Azərbaycan dilində) | 41.5 | 41.5 |
| Lənkəran Dövlət Universiteti | Ümumi meşəçilik və meşələrin idarə olunması | 41 | 30 |
| Bakı Dövlət Universiteti | Yerquruluşu və landşaft planlaşdırılması | 43.5 | 43.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Yerquruluşu və landşaft planlaşdırılması (tədris Azərbaycan dilində) | 37.5 | 37.5 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050504` | Ekologiya |
| `050606` | Ekologiya mühəndisliyi |
| `050510` | Ekologiya |
| `050649` | Ekologiya mühəndisliyi |
| `ET 010100` | Ekologiya n istifadə |
| `ET 010300` | Bioekologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizə si
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Aerokosmik monitorinq
  - Nə qliyyat ekologiyası
  - Ekologiya mühəndisliyi
- ** `060510` Ekologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `ET 010500` | Aqroekologiya |
| `ET 010600` | Meliorasiya, rekultivasiya və torpaq mühafizəsi |
| `ET 010700` | Su ehtiyatlar n n |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizə si
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Nə qliyyat ekologiyası
  - Ekologiya mühəndisliyi
- ** `060510` Ekologiya**
  - traf mühitin mühafizə metodları bə rpası
  - tin mühafizə si
  - Bioekologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 19)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050710` | Bitki mühafizəsi |
| `050711` | Bağ çılı və zçilik |
| `AT 020100` | Aqronomluq zçilik və üzümçülük rin mühafizəsi pə kçilik təsərrüfatı bitkilərinin seleksiyası və genetikası |
| `TE 080100` | Torpaqşünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı
  - sə rrüfatı
- ** `060649` Ekologiya mühəndisliyi**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizə si
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Aerokosmik monitorinq
  - Nə qliyyat ekologiyası
- ** `060510` Ekologiya**
  - traf mühitin mühafizə metodları bə rpası
  - tin mühafizə si
  - Bioekologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Lokomotiv və vaqon təsərrüfatı | None | 40 |
| Azərbaycan Texniki Universiteti | Dəmiryolu təsərrüfatı və onun istismarı | 54.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin genetikası (tədris Azərbaycan dilində) | 39.5 | 39.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı heyvanlarının yetişdirilməsi, genetikası və seleksiyası (tədris Azərbaycan dilində) | 33.5 | 33.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Dəmiryolu təsərrüfatı və onun istismarı | None | 40 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu | 33.5 | 30 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| *... və daha 26 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `45`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050703` | balıqçılıq |
| `050707` | balıqçılıq və balıqçılıq təsərrüfatıişi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tin mühafizə si
  - Bioekologiya
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| *... və daha 68 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `45`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050708` | Su bioehtiyatları və akvakultura |
| `050709` | Su bioehtiyatları və akvabitkilər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - traf mühitin mühafizə metodları bə rpası
  - tin mühafizə si
  - Bioekologiya
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| *... və daha 74 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `40`, Səhifə: 25)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050111` | Kimya müəllimliyi |
| `TE 040100` | Kimya |
| `TE 040200` | Tə tbiqi kimya fizioloji fə al lər kimyası |
| `TE 040400` | Ekoloji kimya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060649` Ekologiya mühəndisliyi**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizə si
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Aerokosmik monitorinq
  - Nə qliyyat ekologiyası
- ** `060510` Ekologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 10 (Minimal bal: `40`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050102` | Biologiya müəllimliyi |
| `050501` | Biologiya |
| `050110` | Biologiya müəllimliyi |
| `050505` | Biologiya |
| `TE 050100` | Biologiya |
| `M 011100` | Biologiya və gigiyena |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizəsi
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Aerokosmik monitorinq
  - Nəqliyyat ekologiyası
  - Ekologiya mühəndisliyi
- ** `060510` Ekologiya**
  - traf mühitin mühafizəmetodları bə rpası
  - tin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 11 (Minimal bal: `40`, Səhifə: 27)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050502` | Biotexnologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - İxtiologiya
- ** `060649` Ekologiya mühəndisliyi**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizəsi
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Aerokosmik monitorinq
  - Nəqliyyat ekologiyası
- ** `060510` Ekologiya**
  - traf mühitin mühafizəmetodları bə rpası
  - tin mühafizə si
  - Bioekologiya
  - traf mühitin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Sənaye ixtiologiyası (tədris Azərbaycan dilində) | 40 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| *... və daha 17 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 12 (Minimal bal: `40`, Səhifə: 28)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - İxtiologiya
- ** `060649` Ekologiya mühəndisliyi**
  - Su ehtiyatlarını kompleks istifadəsi
  - torpaq mühafizəsi
  - Təbii ehtiyatların qorunması təkrar emalı
  - traf mühitin mühafizəsi
  - neft sənayesi
  - Bərk tullantıların emalıtexnologiyası
  - li istifadəolunması
  - Aerokosmik monitorinq
  - Nəqliyyat ekologiyası
- ** `060510` Ekologiya**
  - traf mühitin mühafizəmetodları bərpası
  - tin mühafizəsi
  - Bioekologiya
  - traf mühitin mühafizəsi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Sənaye ixtiologiyası (tədris Azərbaycan dilində) | 40 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| *... və daha 17 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 13 (Minimal bal: `40`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050506` | coğrafiya |
| `TE 060100` | coğrafiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ölkəş ünaslıq
- ** `060649` Ekologiya mühəndisliyi**
  - Su ehtiyatlarını kompleks istifadə si
  - li istifadə olunması

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |

</details>

---

#### Blok 14 (Minimal bal: `45`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Bioekologiya
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
- ** `060649` Ekologiya mühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| *... və daha 68 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 15 (Minimal bal: `40`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050612` | Geomatika və geodeziya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060649` Ekologiya mühəndisliyi**
  - Aerokosmik monitorinq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |

</details>

---

### Proqram № 20

#### Blok 1 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050635` | Qida mühəndisliyi |
| `050707` | Şə rabç ılıq |
| `050642` | Qida mə hsulları mühəndisliyi |
| `050712` | Şə rabç ılıq |
| `T 270100` | Taxıl və taxıl mə hsullarının saxlanması və emalıtexnologiyası |
| `T 270200` | Çörə k, makaron, unlu qə nnadımə mulatlarının və qida konsentratlarının texnologiyası kə rli mə hsullar texnologiyas |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060642` Qida mə hsullarımühəndisliyi**
  - mə hsullarının texnologiyası nin təş kili
  - hlükə sizliyi
  - Şə rabç ılıq və qıcqırtma istehsalının texnologiyası
  - Üzümün saxlanması və emalıtexnologiyası
  - dirmə texnologiyası
  - Konserv və qida konsentratlarının texnologiyası
  - z mə hsullarının saxlanması və emalıtexnologiyası
  - Bitkiçilik mə hsullarının saxlanması və emalıtexnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 61.5 | 61.5 |
| Bakı Mühəndislik Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| *... və daha 19 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Nanomateriallar kimyası
  - Kimyə vi ekspertiza
- ** `060642` Qida mə hsullarımühəndisliyi**
  - mə hsullarının texnologiyası nin təş kili
  - hlükə sizliyi
  - Şə rabç ılıq və qıcqırtma istehsalının texnologiyası
  - dirmə texnologiyası
  - Konserv və qidaının texnologiyası
  - z mə hsullarının saxlanması və emalıtexnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Materiallar kimyası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Kimyəvi ekspertiza | 73.5 | 73.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| *... və daha 24 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Nanomateriallar kimyası
  - Kimyə vi ekspertiza
- ** `060642` Qida mə hsullarımühəndisliyi**
  - mə hsullarının texnologiyası nin təş kili
  - hlükə sizliyi
  - Şə rabç ılıq və qıcqırtma istehsalının texnologiyası
  - dirmə texnologiyası
  - Konserv və qidaının texnologiyası
  - z mə hsullarının saxlanması və emalıtexnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Materiallar kimyası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Kimyəvi ekspertiza | 73.5 | 73.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| *... və daha 24 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 21

#### Blok 1 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 270400` | Şə rabç ılıq və qıcqırma istehsalatının texnologiyası |
| `T 270500` | Subtropik və tamlı mə hsullar texnologiyası |
| `T 270700` | Konserv və qida konsentratlarıtexnologiyası t mə hsulları texnologiyası |
| `T 270900` | Balıq və balıq mə hsulları texnologiyası süd mə hsulları texnologiyası mə hsulları texnologiyası |
| `T 271200` | bitkiçilik mə hsullarının saxlanılması və emalı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060644` İstehlak mallarının ekspertizası və marketinqi**
  - rzaq mə hsullarının ekspertizası və marketinqi

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 280300` | Ə yiricilik texnologiyası |
| `T 280400` | Toxuculuq texnologiyası mə mulatlarının konstruksiya edilmə si ri mə mulatlarının |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060644` İstehlak mallarının ekspertizası və marketinqi**
  - rzaq mə hsullarının ekspertizası və marketinqi

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050644` | İstehlak mallarının ekspertizası və marketinqi |
| `T 320100` | İstehlak mallarının keyfiyyə t ekspertizası rzaq mə hsullarının mtəəş ünaslığ ı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060644` İstehlak mallarının ekspertizası və marketinqi**
  - İstehlak mallarının keyfiyyə t ekspertizası
  - rzaq mə hsullarının ekspertizası və marketinqi
  - Gömrük ekspertizası

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050644` | İstehlak mallarının ekspertizası və marketinqi |
| `T 320100` | İstehlak mallarının keyfiyyə t ekspertizası |
| `T 320300` | Qeyri- ə rzaq mallarının mtəəş ünaslğ |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060644` İstehlak mallarının ekspertizası və marketinqi**
  - İstehlak mallarının keyfiyyə t ekspertizası
  - rzaq mə hsullarının ekspertizası və marketinqi
  - Gömrük ekspertizası

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 22)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050412` | Davamlıinkişafın idarə edilmə si aat mühəndisliyi hə rsalma |
| `T 190100` | Memarlıq |
| `İİ 030400` | Gömrük ekspertizası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060644` İstehlak mallarının ekspertizası və marketinqi**
  - Gömrük ekspertizası
  - idarə olunması

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 51 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması | None | 54 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi İngilis dilində | 58.5 | 54 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Fövqəladə halların idarə olunması | 51 | 42 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnsan resurslarının idarə olunması | None | 55 |
| Azərbaycan Dövlət İqtisad Universiteti | Brendin idarə olunması | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 58 |
| Bakı Mühəndislik Universiteti | İnsan resurslarının idarə olunması | None | 49.5 |
| Milli Aviasiya Akademiyası | Aviasiya təhlükəsizliyinin idarə olunması | 62.5 | 48.5 |
| Milli Aviasiya Akademiyası | Hava nəqliyyatı hərəkətinin idarə olunması İngilis dilində | None | 40 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 22

#### Blok 1 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050810` | Turizm və otelçilik də ni servis xidməti |
| `T 300200` | Turist, sanatoriya-kurort rinin servis və tibb tinin təşkili |
| `T 300300` | Turist və sanatoriya- tə bii |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - Otelçilik
  - lə dçisi
  - t agentliyi və turoperator
  - ni servis xidmə ti
  - ölkəş ünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |
| Azərbaycan Turizm və Menecment Universiteti | Hotelçilik | 51.5 | 46 |
| Gəncə Dövlət Universiteti | Hotelçilik | None | 43 |
| Lənkəran Dövlət Universiteti | Hotelçilik | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Hotelçilik (tədris Azərbaycan dilində) | None | 41.5 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050806` | nəqliyyatda servis riüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060803` Turizm və otelçilik**
  - t agentliyi və turoperator
  - ni servis xidmə ti

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | rafiya müəllimliyi |
| `050503` | coğrafiya rafiya müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rafiya mü ə llimliyi
  - nninin tə drisi metodikası və metodologiyası
- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 31)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - və monitorinq
  - kili və metodikası(SABAH)
- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rbaycanda siyasi proseslə r
  - Konfliktologiya
  - Dünya siyasi proseslə ri
- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünasl q

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycanda siyasi proseslər | None | 50 |
| Bakı Dövlət Universiteti | Konfliktologiya | None | 50 |
| Xəzər Universiteti | Konfliktologiya İngilis dilində | None | 50 |
| Xəzər Universiteti | Dünya siyasi prosesləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050211` | Regionşünaslıq (Türkiyə üzrə ) |
| `HS 120100` | Regionşünaslıq üzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünasl q

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050211` | Regionşünaslı rə b riüzrə ) |
| `HS 120100` | Regionşünaslı rə b riüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050211` | Regionşünaslı ranüzrə ) |
| `HS 120100` | Regionşünaslıq ( İran üzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 9 (Minimal bal: `40`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050211` | Regionşünaslıq ( İsrail üzrə ) |
| `HS 120100` | Regionşünaslıq ( İsrail üzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 10 (Minimal bal: `40`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | Regionşünaslıq (Koreya üzrə ) |
| `050211` | Regionşünaslıq (Koreya üzrə ) |
| `HS 120100` | Regionşünasl q (Koreya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünasl q

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

#### Blok 11 (Minimal bal: `40`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050211` | Regionşünaslıq (Pakistan üzrə ) |
| `HS 120100` | Regionşünaslıq (Pakistanüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünaslıq
- ** `060212` Hüquqş ünaslıq**
  - si və tarixi
  - Beynə lxalq hüquq
  - Dövlə t hüququ

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| *... və daha 9 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 12 (Minimal bal: `40`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Konfliktologiya
  - Dünya siyasi proseslə ri
- ** `060803` Turizm və otelçilik**
  - rin təş kili
  - Turizm işi
  - ni servis xidmə ti
  - ölkəş ünasl q

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Konfliktologiya | None | 50 |
| Xəzər Universiteti | Konfliktologiya İngilis dilində | None | 50 |
| Xəzər Universiteti | Dünya siyasi prosesləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili | None | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sosial xidmətlərin təşkili İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Turizm işi | 59 | 59 |
| Bakı Dövlət Universiteti | Turizm işi İngilis dilində | 58 | 58 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi | 50 | 48 |
| Azərbaycan Turizm və Menecment Universiteti | Turizm işi İngilis dilində | 51.5 | 41 |
| Mingəçevir Dövlət Universiteti | Turizm işi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Turizm işi (tədris Azərbaycan dilində) | None | 41.5 |
| Qərbi Kaspi Universiteti | Turizm işi | None | 42.5 |
| Xəzər Universiteti | Turizm işi İngilis dilində | 58 | 40 |

</details>

---

### Proqram № 23

#### Blok 1 (Minimal bal: `40`, Səhifə: 8)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | standartlaşdırma və sertifikasiya mühəndisliyi |
| `050648` | Biotibbi texnologiya mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060647` Metrologiya, standartlaşdı sertifikasiya mühəndisliyi**
  - metroloji tə minat
  - sistemlə r

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diskret sistemlər | 61 | 61 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050647` | Metrologiya, standartlaş dırma və sertifikasiya mühəndisliyi |
| `T 310100` | Standartlaşdırma və rüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060647` Metrologiya, standartlaşdı sertifikasiya mühəndisliyi**
  - metroloji tə minat
  - Standartlaşdı sertifikatlaşdı rüzrə )
  - sistemlə r

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |
| Azərbaycan Texniki Universiteti | Standartlaşdırma və sertifikatlaşdırma | 53.5 | 53.5 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diskret sistemlər | 61 | 61 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| *... və daha 89 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 24

#### Blok 1 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | hə yat tətəhlükəsizliyi mühəndisliyi D aliyyə tinin M - 2024 sizliyi (inşaatda) traf mühitin mühə ndis rüzrə ) traf mühitin və insanların radiasiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - hlükə sizliyi
  - mühəndisliyi
  - ladə halların idarə olunması
  - hlükə sizliyi
  - hlükə sizliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 61.5 | 61.5 |
| Bakı Mühəndislik Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| *... və daha 20 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 25

#### Blok 1 (Minimal bal: `40`, Səhifə: 6)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | lərinin renovasiyası rüzrə ) və avtomatlaşdı rüzrə ) hlükİ ə sizliyi |
| `050617` | Hava nəqliyyatında texnoloji D rin və istehsalat n M - 2024 sizliyi mühəndisliyi tətəhlükəsizliyinin təşkili və axtarış rinin təşkili |
| `T 340500` | İstehsalatların və texnoloji tətəhlükəsizliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Metallurji tullantıların tə krar emal texnologiyaları
  - Maşı yədavamlılığ ını bə rpası
  - texnologiyasıvə avadanlığ ı
  - Avadanlıqların bərpası möhkə mliyinin artırılması
- ** `060617` Hava nə qliyyatı rin və istehsalatı hlükə sizliyi**
  - mühəndisliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar | 57.5 | 57.5 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar İngilis dilində | 65 | 63.5 |

</details>

---

### Proqram № 26

#### Blok 1 (Minimal bal: `45`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Sə naye mikrobiologiyası
  - Biotexnologiya
- ** `060407` Menecment**
  - Menecment ( ə czaç ılı siüzrə)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya | None | 45 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| *... və daha 69 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 21)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | t və logistika edilməsi |
| `050403` | Davamlıinkişafı edilməsi etməsi |
| `050405` | İqtisadiyyat |
| `050406` | Maliyyə |
| `050407` | Marketinq |
| `050408` | Menecment |
| `050409` | Mühasibat |
| `050410` | Statistika |
| `050401` | Dünya iqtisadiyyatı |
| `050402` | Mühasibat uçotu və audit |
| `050403` | Maliyyə |
| `050404` | iqtisadiyyatıdarə olunması |
| `050406` | Statistika |
| `050407` | Menecment |
| `050408` | Marketinq edilməsi etməsi 0 50411 Kommersiya |
| `050412` | Davamlıinkişafı edilməsi tlə tlə (türk proqramı) |
| `010200` | Mühasibat uçotu və audit və kredit |
| `İİ 010800` | Statistika lxalq ticarət inin təşkili |
| `010400` | iqtisadiyyatı nməsi məyin iqtisadiyyatı və sosiologiyası n istifadənin iqtisadiyyatı dəni sahənin iqtisadiyyatı |
| `010900` | İqtisadi kibernetika lə lməsi riyyə r və vergitutma |
| `İİ 012200` | Sı inin təşkili qtisadi siyasət |
| `İİ 012400` | Dünya iqtisadiyyatında informasiyaı |
| `İİ 012500` | Milli hesablar sistemi |
| `012600` | İqtisadi resursların idarə olunması ndirmə ətli kağ ızlar lərinin iqtisadiyyatı edilməsi iüzrə) rüzrə) rüzrə) edilməsi edilməsi (türk proqramı) |
| `İİ 020500` | Aqrar istehsalatın iqtisadiyyatı edilməsi t və istehlak kooperasiyasının iqtisadiyyatı və edilməsi etməsi idarə olunması İ |
| `İİ 030400` | Gömrük ekspertizası |
| `030600` | Diqtisadiyyatın hüquqi M - 2024 nməsi idarə edilməsi mühəndisliyi etmə rüzrə) ti və fond bazarı |
| `040400` | Reklam işi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060401` Dünya iqtisadiyyatı**
  - tlə r
  - Gömrük işi
  - lxalq ticarət
  - Azə rbaycanı ləri
  - aliyyə t
  - tlə ri
- ** `060402` Mühasibat uçotu və audit**
  - İstehsal sferasında mühasibat uçotu və audit
  - Xidmə t sferasında mühasibat uçotu və audit
- ** `060403` Maliyyə**
  - Bank işi
  - Vergi və vergiqoyma
  - Sı inin təş kili
  - ti və audit
  - Maliyyə menecmenti
  - Maliyyə bazarları
- ** `060404` İqtisadiyyat**
  - İqtisadiyyatı nmə si
  - İqtisadiyyatı nmə si
  - ndirmə
  - Aqrar sahə nin iqtisadiyyatı
  - ni sahənin iqtisadiyyatı
  - Makroiqtisadi siyasə t
  - Turizmin iqtisadiyyatı
  - mə yin iqtisadiyyatı
  - İqtisadi kibernetika
  - dirmə
  - Ekonometriya
  - riyyə
  - Ə traf mühitin iqtisadiyyatı
  - idarə olunması
  - ssisə nin iqtisadiyyatı
  - lərinin iqtisadiyyatı rüzrə )
  - İnnovasiya strategiyasını nmə si
  - İnvestisiyanı ndirilməsi
  - nin idarə olunması
- ** `060406` Statistika**
  - lərin statistikası
- ** `060407` Menecment**
  - edilmə si
  - etmə
  - İnnovasiyaları rin idarəolunması
  - rüzrə)
  - Menecment (alman proqramı)
  - Menecment ( İdman menecmenti)
  - edilmə si
  - edilmə si
  - Biznes inzibatç ılığ ı
  - Aqrobiznes
  - etmə si
  - Dövlə t strukturlarında menecment
  - diyyə menecmenti
  - edilmə si
  - etmə
  - Dövlə t proqramlarını edilmə si
  - etmə
- ** `060412` Davamlıinkişafı edilmə si**
  - Davamlı afda təbii ehtiyatları edilmə si
  - Davamlıinkişafda insan potensialı
- ** `060408` Marketinq**
  - Logistika
  - rüzrə )
- ** `060411` Kommersiya**
  - aliyyə ti
  - Reklam işi
  - Bazar infrastrukturu
  - Elektron kommersiya (SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya | 71 | 55 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | 68.5 | 51.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Azərbaycan Texniki Universiteti | Liftlər və eskalatorlar | None | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Mülkiyyət obyektlərinin qiymətləndirilməsi | 64 | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər və diplomatiya | 72 | 54 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 57 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | None | 50 |
| Bakı Mühəndislik Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 50 |
| Bakı Mühəndislik Universiteti | Sərnişindaşıma xidmətlərinin təşkili və təhlükəsizliyi | 43.5 | 43.5 |
| Azərbaycan Respublikası Prezidenti yanında Dövlət İdarəçilik Akademiyası | Beynəlxalq münasibətlər və diplomatiya | 72 | 72 |
| *... və daha 574 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 22)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | naye mühəndisliyi naye mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ssisə nin iqtisadiyyatı
  - lə rinin iqtisadiyyatı lə r
  - üzrə )
  - İnnovasiya strategiyasını nmə si
  - İnvestisiyanı ndirilmə si
  - nin idarə olunmas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət İqtisad Universiteti | Təhsilin iqtisadiyyatı | 64 | 55 |
| Bakı Dövlət Universiteti | Turizmin iqtisadiyyatı | 64 | 45.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Xidmət sahələrinin iqtisadiyyatı | 64 | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Turizmin iqtisadiyyatı | 65.5 | 65.5 |
| Azərbaycan Turizm və Menecment Universiteti | Turizmin iqtisadiyyatı | 64 | 46.5 |
| Milli Aviasiya Akademiyası | Xidmət sahələrinin iqtisadiyyatı | None | 45 |
| Lənkəran Dövlət Universiteti | Xidmət sahələrinin iqtisadiyyatı | None | 45 |
| “Azərbaycan” Universiteti | Turizmin iqtisadiyyatı | None | 45 |
| Bakı Avrasiya Universiteti | Turizmin iqtisadiyyatı | None | 45 |
| Bakı Biznes Universiteti | Turizmin iqtisadiyyatı | None | 45 |
| Azərbaycan Əmək və Sosial Münasibətlər Akademiyası | Turizmin iqtisadiyyatı | None | 45 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk xalqları dilləri üzrə) | 65.5 | 57.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| *... və daha 104 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `45`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060407` Menecment**
  - İdman menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `45`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060404` İqtisadiyyat**
  - riyyə
- ** `060407` Menecment**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 67 | 67 |
| Bakı Dövlət Universiteti | İqtisadiyyatda intellektual texnologiyalar | 69 | 69 |
| Bakı Dövlət Universiteti | İqtisadiyyatın tənzimlənməsi | 64 | 54 |
| Bakı Dövlət Universiteti | Turizmin iqtisadiyyatı | 64 | 45.5 |
| Bakı Dövlət Universiteti | Beynəlxalq iqtisadiyyat | 64 | 55.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İqtisadiyyatın tənzimlənməsi | 64 | 48.5 |
| Azərbaycan Texniki Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 64 | 64 |
| Azərbaycan Texniki Universiteti | Beynəlxalq iqtisadiyyat | 63.5 | 52 |
| Azərbaycan Texniki Universiteti | Beynəlxalq iqtisadiyyat Türk dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İqtisadiyyatda intellektual texnologiyalar | 64.5 | 64.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Xidmət sahələrinin iqtisadiyyatı | 64 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Xidmət sahələrinin iqtisadiyyatı İngilis dilində | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 73 | 73 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda intellektual texnologiyalar | 75 | 75 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatın tənzimlənməsi | 68.5 | 68.5 |
| *... və daha 156 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `45`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - arxivşünaslıq
- ** `060404` İqtisadiyyat**
  - ni sahə nin iqtisadiyyatı
  - tşünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 67 | 67 |
| Bakı Dövlət Universiteti | İqtisadiyyatda intellektual texnologiyalar | 69 | 69 |
| Bakı Dövlət Universiteti | İqtisadiyyatın tənzimlənməsi | 64 | 54 |
| Bakı Dövlət Universiteti | Turizmin iqtisadiyyatı | 64 | 45.5 |
| Bakı Dövlət Universiteti | Beynəlxalq iqtisadiyyat | 64 | 55.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İqtisadiyyatın tənzimlənməsi | 64 | 48.5 |
| Azərbaycan Texniki Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 64 | 64 |
| Azərbaycan Texniki Universiteti | Beynəlxalq iqtisadiyyat | 63.5 | 52 |
| Azərbaycan Texniki Universiteti | Beynəlxalq iqtisadiyyat Türk dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İqtisadiyyatda intellektual texnologiyalar | 64.5 | 64.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Xidmət sahələrinin iqtisadiyyatı | 64 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Xidmət sahələrinin iqtisadiyyatı İngilis dilində | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 73 | 73 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda intellektual texnologiyalar | 75 | 75 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatın tənzimlənməsi | 68.5 | 68.5 |
| *... və daha 59 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `45`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 155400` | Musiqi meneceri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı ı ı
- ** `060404` İqtisadiyyat**
  - ni sahə nin iqtisadiyyatı
- ** `060211` Regionşünaslıq**
  - Ölkəş ünaslı rüzrə )
  - Regionşünaslıq (regionlarüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 67 | 67 |
| Bakı Dövlət Universiteti | İqtisadiyyatda intellektual texnologiyalar | 69 | 69 |
| Bakı Dövlət Universiteti | İqtisadiyyatın tənzimlənməsi | 64 | 54 |
| Bakı Dövlət Universiteti | Turizmin iqtisadiyyatı | 64 | 45.5 |
| Bakı Dövlət Universiteti | Beynəlxalq iqtisadiyyat | 64 | 55.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İqtisadiyyatın tənzimlənməsi | 64 | 48.5 |
| Azərbaycan Texniki Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 64 | 64 |
| Azərbaycan Texniki Universiteti | Beynəlxalq iqtisadiyyat | 63.5 | 52 |
| Azərbaycan Texniki Universiteti | Beynəlxalq iqtisadiyyat Türk dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İqtisadiyyatda intellektual texnologiyalar | 64.5 | 64.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Xidmət sahələrinin iqtisadiyyatı | 64 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Xidmət sahələrinin iqtisadiyyatı İngilis dilində | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 73 | 73 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatda intellektual texnologiyalar | 75 | 75 |
| Azərbaycan Dövlət İqtisad Universiteti | İqtisadiyyatın tənzimlənməsi | 68.5 | 68.5 |
| *... və daha 54 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ) mü ə llimliyi
  - ə çağ ırı də rki hazırlı nninin tə drisi metodikası və
  - metodologiyası
- ** `060407` Menecment**
  - Menecment (idman menecmenti)
- ** `060505` Biologiya**
  - Molekulyar biologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 76 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `45`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - yaşpsixologiyası
- ** `060407` Menecment**
  - siüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| Azərbaycan Dillər Universiteti | Təhsil psixologiyası | None | 50 |
| Bakı Slavyan Universiteti | Təhsil psixologiyası | None | 53 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil psixologiyası | None | 50 |
| Sumqayıt Dövlət Universiteti | Təhsil psixologiyası | None | 50 |
| “Azərbaycan” Universiteti | Təhsil psixologiyası | None | 50 |
| “Odlar Yurdu” Universiteti | Təhsil psixologiyası | None | 50 |
| “Odlar Yurdu” Universiteti | Ailə psixologiyası | None | 53.5 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| *... və daha 67 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 10 (Minimal bal: `45`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - yaşpsixologiyası
- ** `060407` Menecment**
  - siüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| Azərbaycan Dillər Universiteti | Təhsil psixologiyası | None | 50 |
| Bakı Slavyan Universiteti | Təhsil psixologiyası | None | 53 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil psixologiyası | None | 50 |
| Sumqayıt Dövlət Universiteti | Təhsil psixologiyası | None | 50 |
| “Azərbaycan” Universiteti | Təhsil psixologiyası | None | 50 |
| “Odlar Yurdu” Universiteti | Təhsil psixologiyası | None | 50 |
| “Odlar Yurdu” Universiteti | Ailə psixologiyası | None | 53.5 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| *... və daha 67 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 11 (Minimal bal: `45`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - siüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 12 (Minimal bal: `45`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Sə naye mikrobiologiyası
  - Biotexnologiya
- ** `060407` Menecment**
  - siüzrə )
- ** `060801` Ə czaç ılıq**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya | None | 45 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| *... və daha 72 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 13 (Minimal bal: `45`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - siüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 14 (Minimal bal: `45`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - siüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 15 (Minimal bal: `45`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050803` | Fizioterapiya və tibbi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - siüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 16 (Minimal bal: `45`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | si və idmanda reabilitasiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - Menecment ( İdman menecmenti)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 17 (Minimal bal: `45`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | dman menecmenti və kommunikasiya dman menecmenti və kommunikasiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - Menecment ( İdman menecmenti)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 27

#### Blok 1 (Minimal bal: `45`, Səhifə: 22)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050114` | Riyaziyyat mü İ ə llimliyi |
| `050115` | Riyaziyyat vDə informatika M - 2024 müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 24)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - idarə olunması)
- ** `060107` Texnologiya mü ə llimliyi**
  - nninin tə drisi metodikas və metodologiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 51 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması | None | 54 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi İngilis dilində | 58.5 | 54 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Fövqəladə halların idarə olunması | 51 | 42 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnsan resurslarının idarə olunması | None | 55 |
| Azərbaycan Dövlət İqtisad Universiteti | Brendin idarə olunması | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 58 |
| Bakı Mühəndislik Universiteti | İnsan resurslarının idarə olunması | None | 49.5 |
| Milli Aviasiya Akademiyası | Aviasiya təhlükəsizliyinin idarə olunması | 62.5 | 48.5 |
| Milli Aviasiya Akademiyası | Hava nəqliyyatı hərəkətinin idarə olunması İngilis dilində | None | 40 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 25)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Ekoloji biologiya
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 4 (Minimal bal: `45`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `45`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**
  - si və tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `45`, Səhifə: 30)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `45`, Səhifə: 31)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | çağ ırı də rki hazırlıq (qızlar rbiyə ) müəllimliyi və ə rinçağ ırı də rki hazırlığ ı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - və monitorinq
  - Sosial pedaqogika
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 9 (Minimal bal: `45`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | qtisadi biliklər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 51 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması | None | 54 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi İngilis dilində | 58.5 | 54 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Fövqəladə halların idarə olunması | 51 | 42 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnsan resurslarının idarə olunması | None | 55 |
| Azərbaycan Dövlət İqtisad Universiteti | Brendin idarə olunması | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 58 |
| Bakı Mühəndislik Universiteti | İnsan resurslarının idarə olunması | None | 49.5 |
| Milli Aviasiya Akademiyası | Aviasiya təhlükəsizliyinin idarə olunması | 62.5 | 48.5 |
| Milli Aviasiya Akademiyası | Hava nəqliyyatı hərəkətinin idarə olunması İngilis dilində | None | 40 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 10 (Minimal bal: `40`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050120` | Texnologiya müəllimliyi |
| `050108` | Texnologiya müəllimliyi təlimi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nninin tə drisi metodikası və metodologiyası
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 11 (Minimal bal: `40`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050113` | Musiqi müəllimliyi |
| `050109` | Musiqi müəllimliyi |
| `M 010900` | Musiqi təhsili |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nninin tə drisi metodikası və metodologiyası
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 12 (Minimal bal: `40`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikas (SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 13 (Minimal bal: `40`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | hsildə sosial-psixoloji xidmə t hsildə sosial-psixoloji xidmə t |
| `M 011300` | Pedaqogika və psixologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060116` Korreksiyaedici tə lim**
  - limin metodika və metodologiyası
  - rbiyə
  - nin metodika və metodologiyası
  - sosial-psixoloji xidmə t
  - sosial-psixoloji xidmə t
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Pedaqoji Universiteti | Fiziki tərbiyə və çağırışaqədərki hazırlığın tədrisi | None | 44 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | Fiziki tərbiyə və çağırışaqədərki hazırlığın tədrisi | 62.5 | 49 |
| Gəncə Dövlət Universiteti | Fiziki tərbiyə və çağınşaqədərki hazırlığın tədrisi | 69.5 | 44 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 14 (Minimal bal: `40`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | btidai sinif müəllimliyi |
| `050119` | Korreksiyaedici təlim lim və rbiyə r təhsilin pedaqogika və metodikası btidai təhsilin pedaqogika və metodikası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - limin metodika və metodologiyası
  - rbiyə
  - nin metodika və metodologiyası
  - sosial-psixoloji xidmə t
  - sosial-psixoloji xidmə t
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Pedaqoji Universiteti | Fiziki tərbiyə və çağırışaqədərki hazırlığın tədrisi | None | 44 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | Fiziki tərbiyə və çağırışaqədərki hazırlığın tədrisi | 62.5 | 49 |
| Gəncə Dövlət Universiteti | Fiziki tərbiyə və çağınşaqədərki hazırlığın tədrisi | 69.5 | 44 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 15 (Minimal bal: `40`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 16 (Minimal bal: `45`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nə t müəllimliyi nə t |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 17 (Minimal bal: `45`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyatı) AzəAzərbaycan dili və ədəbiyyatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Dilşünaslıq (ümumi dilçilik)
  - Dilşünaslıq (türkologiya)
  - Dilşünaslıq (Azə rbaycan dili)
- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Dilşünaslıq (ümumi dilçilik) | 65 | 56.5 |
| Azərbaycan Dillər Universiteti | Dilşünaslıq (ümumi dilçilik) | None | 50 |
| Bakı Avrasiya Universiteti | Dilşünaslıq (ümumi dilçilik) | None | 50 |
| Bakı Dövlət Universiteti | Azərbaycan dili | 66 | 66 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili | None | 53 |
| Bakı Slavyan Universiteti | Azərbaycan dili | None | 50.5 |
| Naxçıvan Dövlət Universiteti | Azərbaycan dili | 70 | 50 |
| Gəncə Dövlət Universiteti | Azərbaycan dili | 67.5 | 55 |
| “Azərbaycan” Universiteti | Azərbaycan dili | None | 52 |
| Xəzər Universiteti | Azərbaycan dili | None | 50 |
| Bakı Avrasiya Universiteti | Azərbaycan dili | None | 50 |
| “Odlar Yurdu” Universiteti | Azərbaycan dili | None | 50 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 18 (Minimal bal: `45`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050201` | Filologiya (rus dili və ədəbiyyatı) |
| `HS 020100` | Filologiya (rus dili və ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı
- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 19 (Minimal bal: `45`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyatı) rə b dili) ədəbiyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**
  - si və tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 20 (Minimal bal: `45`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050121` | Xarici dil müəllimliyi (fars dili) ədəbiyyat llimliyi (fars dili və ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 21 (Minimal bal: `45`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 020400` | Xarici dil (fars dili) ədəbiyyat llimliyi (türk dili və ədəbiyyatı) |
| `050121` | Xarici dil müəllimliyi (türk dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 22 (Minimal bal: `40`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (yapon dili və ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi (yapon dili) ədəbiyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 23 (Minimal bal: `40`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (urdu dili və ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi (urdu dili) ədəbiyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 24 (Minimal bal: `40`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (ibri dili və ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi (ibri dili) ədəbiyyat ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 25 (Minimal bal: `45`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050201` | Filologiya (ingilis dili və ədəbiyyatı) ədəbiyyat ədəbiyyatı) |
| `HS 020400` | Xarici dil (ingilis dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Yazılı rbaycan dili-ingilis diliüzrə )
- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**
  - si və tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 26 (Minimal bal: `45`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (ispan dili vİ ə ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 51 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması | None | 54 |
| Azərbaycan Texniki Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi | 58.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Su ehtiyatlarının idarə olunması və mühafizəsi İngilis dilində | 58.5 | 54 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Fövqəladə halların idarə olunması | 51 | 42 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnsan resurslarının idarə olunması | None | 55 |
| Azərbaycan Dövlət İqtisad Universiteti | Brendin idarə olunması | None | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması | None | 56.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İnsan resurslarının idarə olunması İngilis dilində | None | 58 |
| Bakı Mühəndislik Universiteti | İnsan resurslarının idarə olunması | None | 49.5 |
| Milli Aviasiya Akademiyası | Aviasiya təhlükəsizliyinin idarə olunması | 62.5 | 48.5 |
| Milli Aviasiya Akademiyası | Hava nəqliyyatı hərəkətinin idarə olunması İngilis dilində | None | 40 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 27 (Minimal bal: `45`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050201` | Filologiya (alman dili və ədəbiyyatı) ədəbiyyat ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 28 (Minimal bal: `45`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050201` | Filologiya (fransız dili və ədəbiyyatı) ədəbiyyat (fransı ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 29 (Minimal bal: `50`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 110100` | Sosiologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - etmə nin sosiologiyası
  - Sosioloji tə dqiqatların metodları və metodologiyası
  - sosial-psixoloji xidmə t
  - sosial-psixoloji xidmə t

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İdarəetmənin sosiologiyası | 64 | 63 |
| Azərbaycan İlahiyyat İnstitutu | Dinin sosiologiyası | 50 | None |
| Bakı Dövlət Universiteti | Sosioloji tədqiqatlar | 69 | 69 |

</details>

---

#### Blok 30 (Minimal bal: `50`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 110200` | Sosial iş |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Siyasə tin sosiologiyası
  - etmə nin sosiologiyası
  - Sosioloji tə dqiqatların metodları və metodologiyası
  - sosial-psixoloji xidmə t

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Azərbaycan İlahiyyat İnstitutu | Dinin sosiologiyası | 50 | None |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İdarəetmənin sosiologiyası | 64 | 63 |
| Bakı Dövlət Universiteti | Sosioloji tədqiqatlar | 69 | 69 |

</details>

---

#### Blok 31 (Minimal bal: `45`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - arxivşünaslıq
- ** `060407` Menecment**
  - idarə olunması)
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 32 (Minimal bal: `40`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 100100` | Psixologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - sosial-psixoloji xidmə t
  - sosial-psixoloji xidmə t
- ** `060119` Pedaqogika**
  - si və tarixi
  - Sosial pedaqogika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

### Proqram № 28

#### Blok 1 (Minimal bal: `45`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `TT 210100` | Kompüter riyaziyyatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - informasiya tə minatı
  - dirmə
  - Sistem proqramlaşdırılması
  - rinin proqram tə minatı
  - İnformatika
  - Tə tbiqi riyaziyyat
  - hlükə sizliyi
  - msal hökumə t
  - tbiqlə rin hazırlanması və oyun dizaynı
  - ri və texnologiyaları
- ** `060501` Riyaziyyat**
  - si və riyazi statistika
  - sistemli tə hlil
  - Riyazi kibernetika
  - Optimallaşdı etmə
  - Hesablama diaqnostikası
  - Riyazi fizika
  - Diskret sistemlə r
  - statistik metodlarla tə hlili
  - Aktuar riyaziyyat
- ** `060509` Kompüter elmlə ri**
  - informasiya tə minatı
  - dirmə
  - Tə tbiqi riyaziyyat

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Riyazi modelləşdirmə | 64 | 64 |
| Bakı Dövlət Universiteti | İqtisadi-riyazi modelləşdirmə | 64 | 55 |
| Bakı Dövlət Universiteti | Təhsildə monitorinq və qiymətləndirmə | 80 | 80 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 66 | 66 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə İngilis dilində | None | 55.5 |
| Bakı Dövlət Universiteti | Stoxastik modelləşdirmə | 61 | 61 |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi Türk dilində | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Riyazi modelləşdirmə | 62.5 | 62.5 |
| Azərbaycan Texniki Universiteti | İqtisadi-riyazi modelləşdirmə | 65.5 | 46 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsildə monitorinq və qiymətləndirmə | 68.5 | 68.5 |
| Azərbaycan Dillər Universiteti | Təhsildə monitorinq və qiymətləndirmə | 73.5 | 73.5 |
| Naxçıvan Dövlət Universiteti | Kompüter modelləşdirməsi | 55 | 55 |
| *... və daha 59 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 23)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060501` Riyaziyyat**
  - Riyazi analiz
  - Funksional analiz
  - nliklə r
  - br və topologiya
  - Hesablama riyaziyyatı
  - Optimallaşdı etmə
  - Hesablama diaqnostikası
  - Riyazi fizika
  - riyyə si
  - si və riyazi statistika
  - sistemli tə hlil
  - Riyazi kibernetika
  - Aktuar riyaziyyat
  - Diskret sistemlə r
  - statistik metodlarla tə hlili

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tətbiqi riyaziyyat | 66 | 66 |
| Bakı Dövlət Universiteti | Riyaziyyatın tədrisi | 78.5 | 78.5 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 66 | 66 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə İngilis dilində | None | 55.5 |
| Bakı Dövlət Universiteti | Aktuar riyaziyyat | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tətbiqi riyaziyyat | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Kompüter riyaziyyatı | 65 | 65 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Riyaziyyatın tədrisi | 62.5 | 60.5 |
| Naxçıvan Müəllimlər İnstitutu | Riyaziyyatın tədrisi | None | 42.5 |
| Gəncə Dövlət Universiteti | Riyaziyyatın tədrisi | None | 43 |
| Gəncə Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 53 | 53 |
| Sumqayıt Dövlət Universiteti | Riyaziyyatın tədrisi | 73 | 53 |
| Mingəçevir Dövlət Universiteti | Riyaziyyatın tədrisi | 69 | 41 |
| Lənkəran Dövlət Universiteti | Riyaziyyatın tədrisi | 66 | 40 |
| Bakı Dövlət Universiteti | Riyazi analiz | 72 | 72 |
| *... və daha 55 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 30)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060501` Riyaziyyat**
  - Riyazi analiz
  - Funksional analiz
  - nliklə r
  - ə sə
  - br və topologiya
  - Hesablama riyaziyyatı
  - Optimallaşdı ə etmə
  - Hesablama diaqnostikası
  - Riyazi fizika
  - riyyə si
  - si və riyazi statistika
  - sistemli tə hlil
  - Riyazi kibernetika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tətbiqi riyaziyyat | 66 | 66 |
| Bakı Dövlət Universiteti | Riyaziyyatın tədrisi | 78.5 | 78.5 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 66 | 66 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə İngilis dilində | None | 55.5 |
| Bakı Dövlət Universiteti | Aktuar riyaziyyat | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tətbiqi riyaziyyat | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Kompüter riyaziyyatı | 65 | 65 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Riyaziyyatın tədrisi | 62.5 | 60.5 |
| Naxçıvan Müəllimlər İnstitutu | Riyaziyyatın tədrisi | None | 42.5 |
| Gəncə Dövlət Universiteti | Riyaziyyatın tədrisi | None | 43 |
| Gəncə Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 53 | 53 |
| Sumqayıt Dövlət Universiteti | Riyaziyyatın tədrisi | 73 | 53 |
| Mingəçevir Dövlət Universiteti | Riyaziyyatın tədrisi | 69 | 41 |
| Lənkəran Dövlət Universiteti | Riyaziyyatın tədrisi | 66 | 40 |
| Bakı Dövlət Universiteti | Riyazi analiz | 72 | 72 |
| *... və daha 54 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 30

#### Blok 1 (Minimal bal: `45`, Səhifə: 24)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050510` | Mexanika |
| `050502` | Mexanika |
| `TE 020100` | Mexanika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060502` Mexanika**
  - Deformasiya olunan bə rk cisim mexanikası
  - Maye, qaz və plazma mexanikası
- ** `060503` Fizika**
  - ri və riyazi fizika
  - rk cisimlə r fizikası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Deformasiya olunan bərk cisim mexanikası | 51.5 | 45 |
| Bakı Dövlət Universiteti | Maye, qaz və plazma mexanikası | 51 | 51 |
| Azərbaycan Texniki Universiteti | Hidromexanika və hidravlik maşınlar | None | 40 |
| Azərbaycan Tibb Universiteti | Protez-ortez və biomexanika | None | 40 |
| Bakı Mühəndislik Universiteti | Hidromexanika və hidravlik maşınlar | 43 | 40 |
| Bakı Dövlət Universiteti | Riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Fizikanın tədrisi | 69 | 69 |
| Bakı Dövlət Universiteti | Nəzəri və riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bərk cisimlər fizikası | 64 | 64 |
| Bakı Dövlət Universiteti | Tətbiqi fizika (yarımkeçiricilər və dielektriklər fizikası) | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Tətbiqi fizika (yarımkeçiricilər və dielektriklər fizikası) İngilis dilində | 74 | 45 |
| Bakı Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Astrofizika | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Nanofizika və nanotexnologiyalar | 68.5 | 68.5 |
| *... və daha 14 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 31

#### Blok 1 (Minimal bal: `45`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050630` | Mühə ndis fizikası |
| `TT 090100` | Materiallar fizikası |
| `TT 120100` | Fiziki elektronika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Yarımkeçiricilə r fizikası
  - İstilik fizikası və molekulyar fizika
  - Kvant elektronikası
  - Astrofizika
  - Atom və molekul fizikası
  - Bioloji sistemlə r fizikası
  - Yarımkeçirici cihazlar və mikroelektronika
  - nü və fizikası
  - ciklə r fizikası
  - Bə rk cisim elektronikası
  - Qaz və plazma elektronikası
  - Optoelektronika
  - k enerjilə r fizikası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 59.5 | 59.5 |
| Sumqayıt Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 51.5 | 51.5 |
| Bakı Dövlət Universiteti | Kvant elektronikası | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Astrofizika | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Nüvə və elementar zərrəciklər fizikası | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Bərk cisim elektronikası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Optoelektronika | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Yüksək enerjilər fizikası | 61 | 61 |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 24)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050105` | Fizika müəllimliyi |
| `050505` | Fizika |
| `050104` | Fizika müəllimliyi |
| `050503` | Fizika |
| `TE 030100` | Fizika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Yarımkeçiricilə r fizikası
  - İstilik fizikası və molekulyar fizika
  - Kvant elektronikası
  - Astrofizika
  - Atom və molekul fizikası
  - Bioloji sistemlə r fizikası
  - Yarımkeçirici cihazlar və mikroelektronika
  - nü və fizikası
  - ciklə r fizikası
  - Bə rk cisim elektronikası
  - Qaz və plazma elektronikas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 59.5 | 59.5 |
| Sumqayıt Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 51.5 | 51.5 |
| Bakı Dövlət Universiteti | Kvant elektronikası | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Astrofizika | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Nüvə və elementar zərrəciklər fizikası | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Bərk cisim elektronikası | 60.5 | 60.5 |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 30)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - İstilik fizikası və molekulyar fizika
  - Kvant elektronikası
  - Astrofizika
  - Atom və molekul fizikası
  - Bioloji sistemlə r fizikası
  - Yarımkeçirici cihazlar və mikroelektronika
  - nü və fizikası
  - ciklə r fizikası
  - Bə rk cisim elektronikası
  - Qaz və plazma elektronikas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 59.5 | 59.5 |
| Sumqayıt Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 51.5 | 51.5 |
| Bakı Dövlət Universiteti | Kvant elektronikası | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Astrofizika | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Nüvə və elementar zərrəciklər fizikası | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Bərk cisim elektronikası | 60.5 | 60.5 |

</details>

---

### Proqram № 32

#### Blok 1 (Minimal bal: `45`, Səhifə: 12)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | texnologiyası və rin kimyə vi texnologiyası |
| `T 251700` | Kimyə vi istehsalatların kimyə vi kibernetikası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
- ** `060504` Kimya**
  - vi kinetika və kataliz
  - Kompozisiya materiallarıkimyası
  - Qeyri-üzvi kimya
  - Üzvi kimya
  - Fiziki kimya
  - Kolloid kimya
  - Analitik kimya
  - lə r kimyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Bakı Dövlət Universiteti | Kimyanın tədrisi | 62.5 | 59 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 65 | 65 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Üzvi kimya İngilis dilində | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Bakı Dövlət Universiteti | Fiziki kimya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Bakı Dövlət Universiteti | Analitik kimya | 66.5 | 66.5 |
| Bakı Dövlət Universiteti | Analitik kimya İngilis dilində | 75 | 45 |
| Bakı Dövlət Universiteti | Elektrokimya | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Təbii və fizioloji fəal maddələr kimyası | 64 | 64 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| *... və daha 57 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 25)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060504` Kimya**
  - vi kinetika və kataliz
  - Kompozisiya materiallarıkimyası
  - Qeyri-üzvi kimya
  - Üzvi kimya
  - Fiziki kimya
  - Kolloid kimya
  - Analitik kimya
  - lə r kimyası
  - Elektrokimya
  - Bə rk cisim kimyası
  - lə r kimyası
  - Neft kimyası
  - Nanomateriallar kimyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Bakı Dövlət Universiteti | Kimyanın tədrisi | 62.5 | 59 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 65 | 65 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Üzvi kimya İngilis dilində | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Bakı Dövlət Universiteti | Fiziki kimya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Bakı Dövlət Universiteti | Analitik kimya | 66.5 | 66.5 |
| Bakı Dövlət Universiteti | Analitik kimya İngilis dilində | 75 | 45 |
| Bakı Dövlət Universiteti | Elektrokimya | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Təbii və fizioloji fəal maddələr kimyası | 64 | 64 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| *... və daha 39 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 28)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `TE 050300` | Biokimya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyəvi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
- ** `060504` Kimya**
  - vi kinetika və kataliz
  - Kompozisiya materiallarıkimyası
  - Qeyri-üzvi kimya
  - Üzvi kimya
  - Fiziki kimya
  - Kolloid kimya
  - Analitik kimya
  - lər kimyası
  - Elektrokimya
  - Bərk cisim kimyası
  - lər kimyası
  - Neft kimyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Bakı Dövlət Universiteti | Kimyanın tədrisi | 62.5 | 59 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 65 | 65 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Üzvi kimya İngilis dilində | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Bakı Dövlət Universiteti | Fiziki kimya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Bakı Dövlət Universiteti | Analitik kimya | 66.5 | 66.5 |
| Bakı Dövlət Universiteti | Analitik kimya İngilis dilində | 75 | 45 |
| Bakı Dövlət Universiteti | Elektrokimya | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Təbii və fizioloji fəal maddələr kimyası | 64 | 64 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| *... və daha 57 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `45`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060504` Kimya**
  - vi kinetika və kataliz
  - Kompozisiya materiallarıkimyası
  - Qeyri-üzvi kimya
  - Üzvi kimya
  - Fiziki kimya
  - Kolloid kimya
  - Analitik kimya
  - lər kimyası
  - Elektrokimya
  - Bə rk cisim kimyası
  - lə r kimyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Bakı Dövlət Universiteti | Kimyanın tədrisi | 62.5 | 59 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 65 | 65 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Üzvi kimya İngilis dilində | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Bakı Dövlət Universiteti | Fiziki kimya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Bakı Dövlət Universiteti | Analitik kimya | 66.5 | 66.5 |
| Bakı Dövlət Universiteti | Analitik kimya İngilis dilində | 75 | 45 |
| Bakı Dövlət Universiteti | Elektrokimya | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Təbii və fizioloji fəal maddələr kimyası | 64 | 64 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| *... və daha 39 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `45`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050804` | Tibbi profilaktika |
| `HS 190300` | Tibbi profilaktika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - vi kinetika və kataliz
  - Kompozisiya materiallarıkimyası
  - Qeyri-üzvi kimya
  - Üzvi kimya
  - Fiziki kimya
  - Kolloid kimya
  - Analitik kimya
  - lə r kimyası
  - Elektrokimya
  - Bə rk cisim kimyası
  - lə r kimyası
  - Neft kimyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 65 | 65 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Naxçıvan Dövlət Universiteti | Qeyri-üzvi kimya | 46.5 | 46.5 |
| Gəncə Dövlət Universiteti | Qeyri-üzvi kimya | 51 | 45 |
| Gəncə Dövlət Universiteti | Üzvi kimya | 52 | 45 |
| Sumqayıt Dövlət Universiteti | Üzvi kimya | 48 | 45.5 |
| Bakı Dövlət Universiteti | Üzvi kimya İngilis dilində | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Bakı Dövlət Universiteti | Fiziki kimya İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Fiziki kimya | None | 45 |
| Sumqayıt Dövlət Universiteti | Fiziki kimya | 47 | 45 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Bakı Dövlət Universiteti | Analitik kimya | 66.5 | 66.5 |
| *... və daha 9 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `45`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050802` | Ə czaç ılıq |
| `050806` | Ə czaç ılıq |
| `HS 190500` | Ə czaç ılıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - vi kinetika və kataliz
  - Kompozisiya materiallarıkimyası
  - Qeyri-üzvi kimya
  - Üzvi kimya
  - Fiziki kimya
  - Kolloid kimya
  - Analitik kimya
  - lə r kimyası
  - Elektrokimya
  - Bə rk cisim kimyası
  - lə r kimyası
  - Neft kimyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 65 | 65 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Naxçıvan Dövlət Universiteti | Qeyri-üzvi kimya | 46.5 | 46.5 |
| Gəncə Dövlət Universiteti | Qeyri-üzvi kimya | 51 | 45 |
| Gəncə Dövlət Universiteti | Üzvi kimya | 52 | 45 |
| Sumqayıt Dövlət Universiteti | Üzvi kimya | 48 | 45.5 |
| Bakı Dövlət Universiteti | Üzvi kimya İngilis dilində | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Bakı Dövlət Universiteti | Fiziki kimya İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Fiziki kimya | None | 45 |
| Sumqayıt Dövlət Universiteti | Fiziki kimya | 47 | 45 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Bakı Dövlət Universiteti | Analitik kimya | 66.5 | 66.5 |
| *... və daha 9 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 33

#### Blok 1 (Minimal bal: `45`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050808` | Tibbi biologiya |
| `TT 240100` | Tibbi biologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Mikologiya
  - Mikrobiologiya
  - Genetika
  - Biofizika
  - Nanobiotexnologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Biokimya | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Biokimya İngilis dilində | 71.5 | 67 |
| Azərbaycan Tibb Universiteti | Biokimya | 73.5 | 73.5 |
| Gəncə Dövlət Universiteti | Biokimya | 65 | 65 |
| Bakı Dövlət Universiteti | İnsan və heyvan fiziologiyası | 71 | 71 |
| Gəncə Dövlət Universiteti | İnsan və heyvan fiziologiyası | 51 | 51 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Ekoloji biologiya
- ** `060505` Biologiya**
  - Biofizika
  - Mikrobiologiya
  - Onurğ alılar zoologiyası
  - si və bioloji monitorinq
  - İxtiologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Biologiyanın tədrisi | 63 | 53 |
| Naxçıvan Dövlət Universiteti | Biologiyanın tədrisi | 70.5 | 40 |
| Gəncə Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Sumqayıt Dövlət Universiteti | Biologiyanın tədrisi | None | 42.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `45`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Ekoloji biologiya
- ** `060505` Biologiya**
  - Bitki fiziologiyası
  - Botanika
  - Onurğ asızlar zoologiyası
  - Onurğ alılar zoologiyası
  - Entomologiya
  - si və bioloji monitorinq
  - İxtiologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Biologiyanın tədrisi | 63 | 53 |
| Naxçıvan Dövlət Universiteti | Biologiyanın tədrisi | 70.5 | 40 |
| Gəncə Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Sumqayıt Dövlət Universiteti | Biologiyanın tədrisi | None | 42.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| *... və daha 15 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `45`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060505` Biologiya**
  - Molekulyar biologiya
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Bitki fiziologiyası
  - Mikologiya
  - Mikrobiologiya
  - Botanika
  - Genetika
  - Onurğ asızlar zoologiyası
  - Onurğ alılar zoologiyası
  - Biofizika
  - Nanobiotexnologiya
  - Entomologiya
  - si və bioloji monitorinq
  - Sə naye mikrobiologiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Biologiyanın tədrisi | 63 | 53 |
| Naxçıvan Dövlət Universiteti | Biologiyanın tədrisi | 70.5 | 40 |
| Gəncə Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Sumqayıt Dövlət Universiteti | Biologiyanın tədrisi | None | 42.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| Lənkəran Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| *... və daha 31 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `45`, Səhifə: 27)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060505` Biologiya**
  - Molekulyar biologiya
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Bitki fiziologiyası
  - Mikologiya
  - Mikrobiologiya
  - Botanika
  - Genetika
  - Onurğ asızlar zoologiyası
  - Onurğ alılar zoologiyası
  - Biofizika
  - Nanobiotexnologiya
  - Entomologiya
  - si və bioloji monitorinq
  - Sə naye mikrobiologiyası
  - Bitkilə rin genetikası və seleksiyası
  - İnsan genetikası
  - Biotexnologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Biologiyanın tədrisi | 63 | 53 |
| Naxçıvan Dövlət Universiteti | Biologiyanın tədrisi | 70.5 | 40 |
| Gəncə Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Sumqayıt Dövlət Universiteti | Biologiyanın tədrisi | None | 42.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| Lənkəran Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| *... və daha 36 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `45`, Səhifə: 28)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060505` Biologiya**
  - Molekulyar biologiya
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Bitki fiziologiyası
  - Mikologiya
  - Botanika
  - Genetika
  - Onurğ asızlar zoologiyası
  - Onurğ alılar zoologiyası
  - Biofizika
  - Entomologiya
  - si və bioloji monitorinq
  - Sənaye mikrobiologiyası
  - Bitkilərin genetikasıvə seleksiyası
  - İnsan genetikası
  - Biotexnologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Biologiyanın tədrisi | 63 | 53 |
| Naxçıvan Dövlət Universiteti | Biologiyanın tədrisi | 70.5 | 40 |
| Gəncə Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Sumqayıt Dövlət Universiteti | Biologiyanın tədrisi | None | 42.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| Lənkəran Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| *... və daha 36 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `45`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Bitki fiziologiyası
  - Mikologiya
  - Mikrobiologiya
  - Botanika
  - Genetika
  - Onurğ asızlar zoologiyası
  - Onurğ alılar zoologiyası
  - Biofizika
  - Nanobiotexnologiya
  - Entomologiya
  - si və bioloji monitorinq
  - Sə naye mikrobiologiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Biokimya | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Biokimya İngilis dilində | 71.5 | 67 |
| Azərbaycan Tibb Universiteti | Biokimya | 73.5 | 73.5 |
| Gəncə Dövlət Universiteti | Biokimya | 65 | 65 |
| Bakı Dövlət Universiteti | İnsan və heyvan fiziologiyası | 71 | 71 |
| Gəncə Dövlət Universiteti | İnsan və heyvan fiziologiyası | 51 | 51 |
| Bakı Dövlət Universiteti | Bitki fiziologiyası | 67 | 67 |
| Gəncə Dövlət Universiteti | Bitki fiziologiyası | 47 | 45 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| *... və daha 18 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `45`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050901` | Hə rbi tibb |
| `050904` | Tibb işi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Mikologiya
  - Mikrobiologiya
  - Genetika
  - Biofizika
  - Nanobiotexnologiya
  - Sə naye mikrobiologiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Biokimya | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Biokimya İngilis dilində | 71.5 | 67 |
| Azərbaycan Tibb Universiteti | Biokimya | 73.5 | 73.5 |
| Gəncə Dövlət Universiteti | Biokimya | 65 | 65 |
| Bakı Dövlət Universiteti | İnsan və heyvan fiziologiyası | 71 | 71 |
| Gəncə Dövlət Universiteti | İnsan və heyvan fiziologiyası | 51 | 51 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `45`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060505` Biologiya**
  - Molekulyar biologiya
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Mikrobiologiya
  - Genetika
  - Biofizika
  - Sə naye mikrobiologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Biologiyanın tədrisi | 63 | 53 |
| Naxçıvan Dövlət Universiteti | Biologiyanın tədrisi | 70.5 | 40 |
| Gəncə Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Sumqayıt Dövlət Universiteti | Biologiyanın tədrisi | None | 42.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| Lənkəran Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| *... və daha 16 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 10 (Minimal bal: `45`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Mikologiya
  - Mikrobiologiya
  - Genetika
  - Biofizika
  - Sə naye mikrobiologiyası
  - Biotexnologiya
- ** `060504` Kimya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Biokimya | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Biokimya İngilis dilində | 71.5 | 67 |
| Azərbaycan Tibb Universiteti | Biokimya | 73.5 | 73.5 |
| Gəncə Dövlət Universiteti | Biokimya | 65 | 65 |
| Bakı Dövlət Universiteti | İnsan və heyvan fiziologiyası | 71 | 71 |
| Gəncə Dövlət Universiteti | İnsan və heyvan fiziologiyası | 51 | 51 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| *... və daha 61 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 11 (Minimal bal: `45`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050903` | Stomatologiya |
| `HS 190400` | Stomatologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060505` Biologiya**
  - Molekulyar biologiya
  - Biokimya
  - nsan və heyvan fiziologiyası
  - Mikrobiologiya
  - Genetika
  - Biofizika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Biologiyanın tədrisi | 63 | 53 |
| Naxçıvan Dövlət Universiteti | Biologiyanın tədrisi | 70.5 | 40 |
| Gəncə Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Sumqayıt Dövlət Universiteti | Biologiyanın tədrisi | None | 42.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| Lənkəran Dövlət Universiteti | Biologiyanın tədrisi | None | 40 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| *... və daha 16 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 12 (Minimal bal: `45`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nsan və heyvan fiziologiyası
  - Bitki fiziologiyası
  - Mikologiya
  - Mikrobiologiya
  - Botanika
  - Biofizika
  - Sə naye mikrobiologiyası
  - Biotexnologiya
- ** `060504` Kimya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İnsan və heyvan fiziologiyası | 71 | 71 |
| Gəncə Dövlət Universiteti | İnsan və heyvan fiziologiyası | 51 | 51 |
| Bakı Dövlət Universiteti | Bitki fiziologiyası | 67 | 67 |
| Gəncə Dövlət Universiteti | Bitki fiziologiyası | 47 | 45 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| Sumqayıt Dövlət Universiteti | Mikrobiologiya | 58.5 | 58.5 |
| “Odlar Yurdu” Universiteti | Mikrobiologiya | 70 | 70 |
| Bakı Dövlət Universiteti | Botanika | 64.5 | 64.5 |
| Naxçıvan Dövlət Universiteti | Botanika | 47 | 45 |
| Gəncə Dövlət Universiteti | Botanika | 49.5 | 49.5 |
| Bakı Dövlət Universiteti | Biofizika | 69.5 | 69.5 |
| *... və daha 60 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 34

#### Blok 1 (Minimal bal: `45`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060506` Coğ rafiya**
  - sosial coğ rafiya
  - aftşünaslıq
  - Azə rbaycanın fiziki coğ rafiyası
  - Geomorfologiya
  - Azə rbaycanı sosial coğ rafiyası
  - Dünyanı sosial coğ rafiyası
  - razi planlaşdırma və rayon plana alınması

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Coğrafiyanın tədrisi | 65 | 49.5 |
| Bakı Dövlət Universiteti | İqtisadi və sosial coğrafiya | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Azərbaycan coğrafiyası | 56 | 56 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Coğrafiyanın tədrisi | 62.5 | 47 |
| Naxçıvan Dövlət Universiteti | Coğrafiyanın tədrisi | None | 40 |
| Naxçıvan Dövlət Universiteti | İqtisadi və sosial coğrafiya | None | 45 |
| Gəncə Dövlət Universiteti | Coğrafiyanın tədrisi | None | 42.5 |
| Gəncə Dövlət Universiteti | Azərbaycan coğrafiyası | 45.5 | 45.5 |
| Sumqayıt Dövlət Universiteti | Coğrafiyanın tədrisi | None | 42 |
| Sumqayıt Dövlət Universiteti | Azərbaycan coğrafiyası | 46 | 45 |
| Lənkəran Dövlət Universiteti | Coğrafiyanın tədrisi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | İqtisadi və sosial coğrafiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Geomorfologiya | 56 | 56 |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 31)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | müəllimliyi coğrafiya müəllimliyi coğrafiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060506` Coğ rafiya**
  - sosial coğ rafiya
  - aftşünaslıq
  - Azə rbaycanın fiziki coğ rafiyası
  - Geomorfologiya
  - Azə rbaycanı sosial coğ rafiyası
  - Dünyanı sosial coğ rafiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Coğrafiyanın tədrisi | 65 | 49.5 |
| Bakı Dövlət Universiteti | İqtisadi və sosial coğrafiya | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Azərbaycan coğrafiyası | 56 | 56 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Coğrafiyanın tədrisi | 62.5 | 47 |
| Naxçıvan Dövlət Universiteti | Coğrafiyanın tədrisi | None | 40 |
| Naxçıvan Dövlət Universiteti | İqtisadi və sosial coğrafiya | None | 45 |
| Gəncə Dövlət Universiteti | Coğrafiyanın tədrisi | None | 42.5 |
| Gəncə Dövlət Universiteti | Azərbaycan coğrafiyası | 45.5 | 45.5 |
| Sumqayıt Dövlət Universiteti | Coğrafiyanın tədrisi | None | 42 |
| Sumqayıt Dövlət Universiteti | Azərbaycan coğrafiyası | 46 | 45 |
| Lənkəran Dövlət Universiteti | Coğrafiyanın tədrisi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | İqtisadi və sosial coğrafiya (tədris Azərbaycan dilində) | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Geomorfologiya | 56 | 56 |

</details>

---

### Proqram № 35

#### Blok 1 (Minimal bal: `45`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ndisliyi işi meşə -park təsərrüfatı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - traf mühitin mühafizə si
- ** `060702` Aqronomluq**
  - rin mühafizə si
  - n mühafizə si
  - Mey və çilik
  - Bitkilə rin seleksiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası | 46 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası İngilis dilində | 56 | 56 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Memarlıq abidələrinin mühafizəsi və bərpası | 51.5 | 40 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ı ı si və kompleks istifadə si |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
- ** `060701` Torpaqşünaslıq və aqrokimya**
  - Aqrokimya
  - Torpağ rə ayr lmas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Bakı Dövlət Universiteti | Kimyanın tədrisi | 62.5 | 59 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| *... və daha 70 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 19)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050701` | Aqronomluq |
| `050702` | Bağ çılı və zçilik |
| `050705` | Bitki mühafizəsi |
| `050709` | Torpaqşünaslıq və aqrokimya |
| `050701` | Torpaqşünaslıq və aqrokimya |
| `050702` | Aqronomluq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060701` Torpaqşüna slıq və aqrokimya**
  - Torpaqşünaslıq
  - Aqrokimya
  - Torpağ ı rə ayrılması
  - Torpağ ın ekoloji monitorinqi və qorunması
- ** `060702` Aqronomluq**
  - rin mühafizə si
  - pə kçilik
  - rin toxumçuluğ u
  - Bitkilə rin genetikası
  - n mühafizə si
  - Aqrobiotexnologiya
  - Bitkilə rin karantini
  - Bitkiçilik
  - Mey və çilik
  - və zçilik
  - Üzümçülük
  - Bitkilə rin seleksiyası
  - Aqrogeobotanika
  - sə rrüfatınınə sasları
  - Bitki anatomiyas və morfologiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Torpaqşünaslıq | 54.5 | 54.5 |
| Naxçıvan Dövlət Universiteti | Torpaqşünaslıq | 43.5 | 30 |
| Lənkəran Dövlət Universiteti | Torpaqşünaslıq | 40.5 | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Torpaqşünaslıq (tədris Azərbaycan dilində) | 38 | 30 |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimya və torpaq münbitliyinin idarə olunması (tədris Azərbaycan dilində) | 39 | 39 |
| Lənkəran Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 44 | 44 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Gəncə Dövlət Universiteti | Genetika | 57 | 57 |
| Qərbi Kaspi Universiteti | Genetika | 60 | 60 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası | 46 | 40 |
| *... və daha 17 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Torpağ ı rəayrılması
  - Torpağ ın ekoloji monitorinqi və qorunması
- ** `060702` Aqronomluq**
  - rin mühafizəsi
  - Bitkilə rin genetikası
  - n mühafizəsi
  - Aqrobiotexnologiya
  - Bitkilə rin karantini
  - Bitkiçilik
  - Bitkilə rin seleksiyası
  - Aqrogeobotanika
  - sə rrüfatınınə sasları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Gəncə Dövlət Universiteti | Genetika | 57 | 57 |
| Qərbi Kaspi Universiteti | Genetika | 60 | 60 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası | 46 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq abidələrinin mühafizəsi və bərpası İngilis dilində | 56 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Memarlıq abidələrinin mühafizəsi və bərpası | 51.5 | 40 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `45`, Səhifə: 27)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
- ** `060701` Torpaqşünaslıq və aqrokimya**
  - Aqrokimya
  - Torpağ ı rəayrılması
  - Torpağ ın ekoloji monitorinqi və qorunması
- ** `060702` Aqronomluq**
  - rin mühafizəsi
  - pə kçilik
  - rin toxumçuluğ u
  - Bitkilə rin genetikası
  - n mühafizəsi
  - Aqrobiotexnologiya
  - Bitkilə rin karantini
  - Bitkiçilik

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Bakı Dövlət Universiteti | Kimyanın tədrisi | 62.5 | 59 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Qeyri-üzvi kimya | 65 | 65 |
| Bakı Dövlət Universiteti | Üzvi kimya | 67.5 | 67.5 |
| Bakı Dövlət Universiteti | Üzvi kimya İngilis dilində | 55.5 | 55.5 |
| Bakı Dövlət Universiteti | Fiziki kimya | 62 | 62 |
| Bakı Dövlət Universiteti | Fiziki kimya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Kolloid kimya | 63 | 63 |
| Bakı Dövlət Universiteti | Analitik kimya | 66.5 | 66.5 |
| Bakı Dövlət Universiteti | Analitik kimya İngilis dilində | 75 | 45 |
| Bakı Dövlət Universiteti | Elektrokimya | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Təbii və fizioloji fəal maddələr kimyası | 64 | 64 |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| *... və daha 81 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 28)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Nanomateriallar kimyası
  - Kimyəvi ekspertiza
- ** `060701` Torpaqşünaslıq və aqrokimya**
  - Aqrokimya
  - Torpağ ı rəayrılması
  - Torpağ ın ekoloji monitorinqi və qorunması
- ** `060702` Aqronomluq**
  - rin mühafizəsi
  - pəkçilik
  - rin toxumçuluğ u
  - Bitkilərin genetikası
  - n mühafizəsi
  - Bitkilərin karantini
  - Bitkiçilik
  - Meyvə çilik
  - və zçilik
  - Üzümçülük
  - Bitkilərin seleksiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Materiallar kimyası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Kimyəvi ekspertiza | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Torpaqşünaslıq | 54.5 | 54.5 |
| Naxçıvan Dövlət Universiteti | Torpaqşünaslıq | 43.5 | 30 |
| Lənkəran Dövlət Universiteti | Torpaqşünaslıq | 40.5 | 30 |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimya və torpaq münbitliyinin idarə olunması (tədris Azərbaycan dilində) | 39 | 39 |
| Lənkəran Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 44 | 44 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Gəncə Dövlət Universiteti | Genetika | 57 | 57 |
| Qərbi Kaspi Universiteti | Genetika | 60 | 60 |
| *... və daha 17 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 36

#### Blok 1 (Minimal bal: `45`, Səhifə: 19)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050704` | Baytarlı babə ti |
| `050711` | Zoomühəndisliyi |
| `050703` | zootexniklik |
| `050704` | Baytarlıq |
| `AT 030100` | zootexniklik |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
- ** `060703` Zootexniklik**
  - Maldarlıq
  - Qoyunçuluq
  - Quşçuluq
- ** `060704` Baytarlıq**
  - liklə r
  - liklə r

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Bakı Dövlət Universiteti | Geokimya | 51 | 51 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Bakı Dövlət Universiteti | Kimyanın tədrisi | 62.5 | 59 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| *... və daha 83 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Də rman preparatlarını tinin tə minatı
- ** `060704` Baytarlıq**
  - Baytarlıqə czaç ılığ ı
- ** `060505` Biologiya**
  - Molekulyar biologiya
  - Biokimya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Naxçıvan Dövlət Universiteti | Baytarlıq cərrahiyyəsi | 43 | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Baytarlıq cərrahiyyəsi (tədris Azərbaycan dilində) | 45 | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Baytarlıq sanitariya-ekspertizası (tədris Azərbaycan dilində) | 41 | 41 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Baytarlıq təbabəti əczaçılığı (tədris Azərbaycan dilində) | 40.5 | 40.5 |
| Lənkəran Dövlət Universiteti | Baytarlıq təbabətində mamalıq- ginekologiya və süni mayalanma | None | 30 |
| Lənkəran Dövlət Universiteti | Baytarlıq sanitariya-ekspertizası | 37 | 30 |
| Xəzər Universiteti | Baytarlıq epidemiologiyası | 45 | 45 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Molekulyar biologiya | 72.5 | 72.5 |
| Bakı Dövlət Universiteti | Molekulyar biologiya İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Mikrobiologiya | 76.5 | 76.5 |
| Bakı Dövlət Universiteti | Mikrobiologiya İngilis dilində | 69 | 69 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası | 65 | 65 |
| Bakı Dövlət Universiteti | Ətraf mühitin biologiyası İngilis dilində | 69 | 54.5 |
| Azərbaycan Tibb Universiteti | Mikrobiologiya | 75.5 | 75.5 |
| *... və daha 14 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 37

#### Blok 1 (Minimal bal: `40`, Səhifə: 31)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nbəş ünaslığ ı və ta rixşünaslığ ı
  - lə ri tarixi
- ** `060111` Tarix mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası
- ** `060301` Muzeyşünaslı lə rin qorunması**
  - Muzeyşünaslıq
  - Arxeoloji və tarixi memarlı rinin mühafizə si
  - arxivşünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan tarixinin mənbəşünaslığı və tarixşünaslığı | 63.5 | 63.5 |
| Bakı Dövlət Universiteti | Slavyan ölkələri tarixi | 65.5 | 65.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Muzeyşünaslıq | 52.5 | 47 |
| Azərbaycan Turizm və Menecment Universiteti | Muzeyşünaslıq | 53.5 | 43 |
| Lənkəran Dövlət Universiteti | Muzeyşünaslıq | 52.5 | 39 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Naxçıvan Dövlət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 64.5 | 43 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 151700` | Kitabxanaşünaslıq və biblioqrafiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Biblioqrafik ehtiyatların yaradılması istifadə si
  - tşünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 4 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050206` | Tarix |
| `050207` | Antropologiya |
| `HS 070100` | Tarix |
| `HS 070200` | Tarix-arxivşünaslıq |
| `HS 070300` | Tarix-muzeyşünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060207` Antropologiya**
  - də ni antropologiya
- ** `060111` Tarix mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası
- ** `060301` Muzeyşünaslı lə rin qorunması**
  - Muzeyşünaslıq
  - Arxeoloji və tarixi memarlı rinin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Antropologiya | 61 | 59 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Muzeyşünaslıq | 52.5 | 47 |
| Azərbaycan Turizm və Menecment Universiteti | Muzeyşünaslıq | 53.5 | 43 |
| Lənkəran Dövlət Universiteti | Muzeyşünaslıq | 52.5 | 39 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Naxçıvan Dövlət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 64.5 | 43 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | i və lə rin qorunması |
| `050301` | Muzeyşünaslı i və lə rin qorunması |
| `HS 080100` | Müzeyşünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - və monitorinq
  - kili və metodikası(SABAH)
- ** `060301` Muzeyşünaslı lə rin qorunması**
  - Muzeyşünaslıq
  - arxivşünaslıq
  - Arxeoloji və tarixi memarlı rinin mühafizə si
  - tşünaslıq
  - riyyə si
  - niyyə tin tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Muzeyşünaslıq | 52.5 | 47 |
| Azərbaycan Turizm və Menecment Universiteti | Muzeyşünaslıq | 53.5 | 43 |
| Lənkəran Dövlət Universiteti | Muzeyşünaslıq | 52.5 | 39 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Naxçıvan Dövlət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 64.5 | 43 |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| *... və daha 50 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - stə karlıq
  - nə ti
  - Balet tarixi
  - Balet tə nqidi
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Bəstəkarlıq (akademik bəstəkarlıq, audiovizual və teatr musiqisi) | 46.5 | 30 |
| Azərbaycan Milli Konservatoriyası | Akademik bəstəkarlıq | 32 | 30 |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| *... və daha 46 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nə ti
  - riyyə si
  - nə ti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 44 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | tşünaslı lər üzrə ) |
| `050313` | Teatrşünaslıq |
| `HS 150400` | Teatrşünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Teatr tə nqidi
  - riyyə si
- ** `060314` Bə dii yaradıcılıq və ekran dramaturgiyası**
  - bi iş
  - tşünaslıq
  - riyyə si
- ** `060316` Kinoş ünasl q**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Teatr tənqidi | 49 | 39 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| *... və daha 45 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | tşünaslı lər üzrə ) İ |
| `050316` | Kinoşünaslıq |
| `HS 150600` | Kinoşünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Kino tə nqidi
  - riyyə si
- ** `060314` Bə dii yaradıcılıq və ekran dramaturgiyası**
  - bi iş
  - bi redaktə
  - Ssenarist

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Kino tənqidi | 48 | 48 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| *... və daha 27 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 150700` | Kinooperatorluq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nə ti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 10 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050302` | Bə dii yaradıcılıq və ekran dramaturgiyası |
| `050314` | Bə dii yaradıcılıq və ekran dramaturgiyası |
| `HS 151600` | Bə dii yaradıcılıq rüzrə ) də bi yaradıcılıq və ekran dramaturgiyas |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060314` Bə dii yaradıcılıq və ekran dramaturgiyası**
  - bi iş
  - Ssenarist
  - tşünaslıq
  - riyyə si
- ** `060316` Kinoş ünaslıq**
  - Kino tə nqidi
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Ssenarist | 48.5 | 48.5 |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| *... və daha 46 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 11 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | i və lə rin qorunması |
| `050301` | Muzeyşünaslı i və lə rin qorunması lə rin mühafizəsi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060301` Muzeyşünaslı lə rin qorunması**
  - Muzeyşünaslıq
  - Arxeoloji və tarixi memarlı rinin mühafizə si
  - arxivşünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Muzeyşünaslıq | 52.5 | 47 |
| Azərbaycan Turizm və Menecment Universiteti | Muzeyşünaslıq | 53.5 | 43 |
| Lənkəran Dövlət Universiteti | Muzeyşünaslıq | 52.5 | 39 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 58.5 | 58.5 |
| Azərbaycan Turizm və Menecment Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 53 | 47 |
| Naxçıvan Dövlət Universiteti | Arxeoloji və tarixi memarlıq abidələrinin mühafizəsi | 64.5 | 43 |

</details>

---

#### Blok 12 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | tşünaslı lər üzrə ) tşünaslıq |
| `HS 152800` | Kulturologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - riyyə si
  - niyyə tin tarixi
- ** `060301` Muzeyşünaslı lə rin qorunması**
  - Muzeyşünaslıq
  - Arxeoloji və tarixi memarlı rinin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 50 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 13 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | təş kilatç ısı niyyə t meneceri (prodüser) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - riyyə si
  - niyyə tin tarixi
- ** `060301` Muzeyşünaslı lə rin qorunması**
  - Muzeyşünaslıq
  - Arxeoloji və tarixi memarlı rinin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| Azərbaycan Milli Konservatoriyası | Musiqi tarixi və nəzəriyyəsi | 49 | 48.5 |
| *... və daha 31 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 14 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050315` | Rejissorluq lər üzrə ) |
| `HS 153200` | Dram rejissoru |
| `HS 153300` | Televiziya rejissoru |
| `HS 153400` | Kino rejissoru |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Teatr tə nqidi
  - riyyə si
- ** `060315` Rejissorluq**
  - riyyə si
- ** `060316` Kinoşünaslıq**
  - Kino tə nqidi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Teatr tənqidi | 49 | 39 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| *... və daha 27 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 38

#### Blok 1 (Minimal bal: `40`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | AzəAzərbaycan dili və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - dəbiyyatının tə drisi metodikası və metodologiyası
- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslı riyyə si)
  - biyyatşünaslıq (folklorşünaslıq və mifologiya)
  - biyyatşünaslı si və tarixi)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Folklorşünaslıq | 65 | 65 |

</details>

---

### Proqram № 39

#### Blok 1 (Minimal bal: `40`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050117` | Rus dili və ədəbiyyatı müəllimliyi |
| `050121` | Rus dili və ədəbiyyatı müəllimliyi |
| `050205` | Filologiya (rus dili və ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikası və metodologiyası(rus dili)
  - biyyat mü ə llimliyi
  - dəbiyyatın tə drisi metodikası və metodologiyası(rus dili və
  - dəbiyyatı)
- ** `060201` Filologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Azərbaycan ədəbiyyatı | 65 | 61 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 64.5 | 52.5 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 62 | 62 |
| Azərbaycan Dillər Universiteti | Azərbaycan ədəbiyyatı | None | 53.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (rus dili üzrə) tədrisi | 63 | 53 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (ingilis dili üzrə) tədrisi | 63 | 51 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (alman dili üzrə) tədrisi | 64.5 | 64.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (fransız dili üzrə) tədrisi Ж | 66 | 54 |
| *... və daha 24 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | Tərcümə (rus dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (rus dili)
  - biyyat mü ə llimliyi
  - dəbiyyatın tə drisi metodikası və metodologiyası(rus dili və

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (rus dili üzrə) | 65 | 50 |
| Bakı Slavyan Universiteti | Dilşünaslıq (rus dili üzrə) | None | 50 |

</details>

---

### Proqram № 41

#### Blok 1 (Minimal bal: `50`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat b dili və ədəbiyyat ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslı rəb dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyatı) rə b dili) ədəbiyyat llimliyi (fars dili və ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)
- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünasl q (fars dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fars dili üzrə) | None | 58 |
| Naxçıvan Dövlət Universiteti | Dilşünaslıq (fars dili üzrə) | None | 50 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (türk dili və ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi (türk dili) ədəbiyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - və monitorinq
  - kili və metodikası(SABAH)
- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 4 (Minimal bal: `50`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 020400` | Xarici dil (türk dili) ədəbiyyat llimliyi (yapon dili və ədəbiyyatı) |
| `050121` | Xarici dil müəllimliyi (yapon dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Dilşünaslıq (türk dili)
- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (yapon dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (yapon dili üzrə) | None | 50 |

</details>

---

#### Blok 5 (Minimal bal: `50`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 020400` | Xarici dil (yapon dili) ədəbiyyat llimliyi (urdu dili və ədəbiyyatı) İ |
| `050121` | Xarici dil müəllimliyi (urdu dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (urdu dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 6 (Minimal bal: `50`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (ibri dili və ədəbiyyatı) |
| `050121` | Xarici dil müəllimliyi (ibri dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (ibri dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 7 (Minimal bal: `50`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050121` | Xarici dil müəllimliyi (ispan dili) |
| `050205` | Filologiya (ispan dili və ədəbiyyat ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə (ispan dili)
- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (latın dili)
- ** `060407` Menecment**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| *... və daha 62 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `50`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (alman dili və ədəbiyyatı) |
| `050121` | Xarici dil müəllimliyi (alman dili) |
| `050205` | Filologiya (alman dili və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (alman dili)
  - Dilşünaslıq (latın dili)
  - biyyat mü ə llimliyi
  - dəbiyyat n tə drisi metodikas və metodologiyas (alman dili və

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (alman dili üzrə) | 65.5 | 54.5 |
| Azərbaycan Dillər Universiteti | Dilşünaslıq (alman dili üzrə) | None | 58.5 |

</details>

---

#### Blok 9 (Minimal bal: `50`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat müəllimliyi (fransız dili və ədəbiyyatı) |
| `050121` | Xarici dil müəllimliyi (fransız dili) |
| `050205` | Filologiya (fransız dili və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslıq (fransı dəbiyyatı)
  - Dilşünaslıq (fransız dili)
  - Dilşünaslıq (latın dili)
  - biyyat mü ə llimliyi
  - dəbiyyat n tə drisi metodikas və metodologiyas (frans z dili və

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fransız dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Dilşünaslıq (fransız dili üzrə) | None | 60.5 |

</details>

---

#### Blok 10 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | rə b dili) rə b dili) rə b dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rəb dili)
- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslı rəb dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 11 (Minimal bal: `40`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (alman dili) rcümə (alman dili) rcümə (alman dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - dəbiyyatın tə drisi metodikası və metodologiyası(alman dili və
  - dəbiyyatı)
- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikası və metodologiyası(alman dili)
- ** `060201` Filologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Azərbaycan ədəbiyyatı | 65 | 61 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 64.5 | 52.5 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 62 | 62 |
| Azərbaycan Dillər Universiteti | Azərbaycan ədəbiyyatı | None | 53.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (rus dili üzrə) tədrisi | 63 | 53 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (ingilis dili üzrə) tədrisi | 63 | 51 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (alman dili üzrə) tədrisi | 64.5 | 64.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (fransız dili üzrə) tədrisi Ж | 66 | 54 |
| *... və daha 24 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 12 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (ispan dili) rcümə (ispan dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 13 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (fransız dili) rcümə (fransız dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslıq (fransı dəbiyyatı)
  - Dilşünaslıq (fransız dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fransız dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Dilşünaslıq (fransız dili üzrə) | None | 60.5 |

</details>

---

#### Blok 14 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (Koreya dili) rcümə (Koreya dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
- ** `060204` Jurnalistika**
  - Jurnalistika (ümumi tə yinatlı) (SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Radiotelejurnalistika | 57 | 50 |
| Bakı Dövlət Universiteti | Beynəlxalq jurnalistika | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Beynəlxalq jurnalistika (tədris ingilis dilində) | None | 50.5 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Publisistik jurnalistika | 51.5 | 50 |
| Bakı Dövlət Universiteti | İdman jurnalistikası | 53.5 | 50 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman jurnalistikası | None | 50 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman jurnalistikası İngilis dilində | None | 50 |
| Naxçıvan Dövlət Universiteti | Beynəlxalq jurnalistika | None | 50 |

</details>

---

#### Blok 15 (Minimal bal: `50`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | Regionşünaslıq (Türkiyə üzrə )i |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (türk dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk dili üzrə) | None | 50 |

</details>

---

#### Blok 16 (Minimal bal: `50`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | Regionşünaslı rə b riüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslı rəb dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |

</details>

---

#### Blok 17 (Minimal bal: `50`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | Regionşünaslıq ( İran üzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (fars dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fars dili üzrə) | None | 58 |
| Naxçıvan Dövlət Universiteti | Dilşünaslıq (fars dili üzrə) | None | 50 |

</details>

---

#### Blok 18 (Minimal bal: `50`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | RegionDşünaslıq ( İsrail M - 2024 üzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (ibri dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 19 (Minimal bal: `50`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 20 (Minimal bal: `50`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | Regionşünaslıq (Pakistan üzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - Dilşünaslıq (urdu dili)
- ** `060803` Turizm və otelçilik**

---

### Proqram № 42

#### Blok 1 (Minimal bal: `40`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050213` | Sosiologiya |
| `050210` | Sosiologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060805` Sosial iş**
  - halinin sosial müdafiə si
  - şə raitinin yaxşılaşdırılması
- ** `060210` Sosiologiya**
  - Siyasə tin sosiologiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 75 | 75 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 65 |
| Azərbaycan Turizm və Menecment Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 66.5 | 48.5 |
| Azərbaycan Turizm və Menecment Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş | None | 44.5 |
| Naxçıvan Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 70 | 59.5 |
| Gəncə Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 51.5 |
| Azərbaycan Kooperasiya Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş (tədris Azərbaycan dilində) | 67 | 50.5 |
| Azərbaycan Kooperasiya Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş (tədris Azərbaycan dilində) | None | 42.5 |
| “Azərbaycan” Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 68 | 46 |
| Bakı Biznes Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 67.5 | 46.5 |
| Bakı Biznes Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş | None | 43 |
| Azərbaycan Əmək və Sosial Münasibətlər Akademiyası | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 51 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial müdafiənin təşkili | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050807` | Sosial iş |
| `050813` | Sosial iş |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060805` Sosial iş**
  - halinin sosial müdafiə si
  - şə raitinin yaxşılaşdırılması
- ** `060210` Sosiologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 75 | 75 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 65 |
| Azərbaycan Turizm və Menecment Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 66.5 | 48.5 |
| Azərbaycan Turizm və Menecment Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş | None | 44.5 |
| Naxçıvan Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 70 | 59.5 |
| Gəncə Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 51.5 |
| Azərbaycan Kooperasiya Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş (tədris Azərbaycan dilində) | 67 | 50.5 |
| Azərbaycan Kooperasiya Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş (tədris Azərbaycan dilində) | None | 42.5 |
| “Azərbaycan” Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 68 | 46 |
| Bakı Biznes Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 67.5 | 46.5 |
| Bakı Biznes Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş | None | 43 |
| Azərbaycan Əmək və Sosial Münasibətlər Akademiyası | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 51 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial müdafiənin təşkili | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - fə tarixi
  - tşünaslı fə si
- ** `060210` Sosiologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Fəlsəfə tarixi | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İdarəetmənin sosiologiyası | 64 | 63 |
| Azərbaycan İlahiyyat İnstitutu | Dinin sosiologiyası | 50 | None |

</details>

---

#### Blok 4 (Minimal bal: `50`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - riyyə si
  - Dünya siyasi proseslə ri
- ** `060210` Sosiologiya**
  - Siyasə tin sosiologiyası
- ** `060209` Psixologiya**
  - Ümumi psixologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| Azərbaycan Milli Konservatoriyası | Musiqi tarixi və nəzəriyyəsi | 49 | 48.5 |
| *... və daha 56 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `50`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060210` Sosiologiya**
  - Siyasə tin sosiologiyası
  - etmə nin sosiologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İdarəetmənin sosiologiyası | 64 | 63 |
| Azərbaycan İlahiyyat İnstitutu | Dinin sosiologiyası | 50 | None |

</details>

---

#### Blok 6 (Minimal bal: `50`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | t və ictimai tlər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060210` Sosiologiya**
  - etmə nin sosiologiyası
  - si və idman

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İdarəetmənin sosiologiyası | 64 | 63 |
| Azərbaycan İlahiyyat İnstitutu | Dinin sosiologiyası | 50 | None |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 52)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | “Sosial iş” ixtisasının rlə iş” və aliyyə tinin sosial iş” ixtisaslaşmalarınıbütün r ali təhsilli rlər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060805` Sosial iş**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 75 | 75 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 65 |
| Azərbaycan Turizm və Menecment Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 66.5 | 48.5 |
| Azərbaycan Turizm və Menecment Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş | None | 44.5 |
| Naxçıvan Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 70 | 59.5 |
| Gəncə Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 51.5 |
| Azərbaycan Kooperasiya Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş (tədris Azərbaycan dilində) | 67 | 50.5 |
| Azərbaycan Kooperasiya Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş (tədris Azərbaycan dilində) | None | 42.5 |
| “Azərbaycan” Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 68 | 46 |
| Bakı Biznes Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 67.5 | 46.5 |
| Bakı Biznes Universiteti | Əhalinin müxtəlif qrupları ilə sosial iş | None | 43 |
| Azərbaycan Əmək və Sosial Münasibətlər Akademiyası | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 65 | 51 |

</details>

---

#### Blok 8 (Minimal bal: `50`, Səhifə: 52)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | fə ixtisasının tşünaslıq fə si” ixtisaslaşmasını biə t ixtisaslarıqrupunu bitirə n bütün r ali təhsilli rlər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslı fə si

---

#### Blok 9 (Minimal bal: `50`, Səhifə: 52)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | fə ixtisasının tarixi və fə ” ixtisaslaşmalarını Humanitar və sosial ixtisaslar qrupunu bitirə n bütün bakalavrlar r seç ə rlər QEYD: n rinin yeni profilli yüks ixtisaslaş malar siyah s ı ı siyah s ı ı bağ l mə lumat "Magistr" xüsusi burax i Regionşünaslı riüzrə) ixtisaslar |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - fə tarixi
  - əbul lm
  - ı ı
  - fli inkiş af n n, hə mçinin haz rk
  - ı ı ı ı
  - ə kixtisasl ləbat rə
  - ı ı ı
  - ikliklə r apar l r. Odur ki, bu il qəbul
  - ı ı
  - n ixtisaslaş malar bu siyah danç
  - lş n n növbə ti say ndaçap olunacaqd r.
  - ı ı ı ı ı ı
  - ını li proqrama daxil olan ixtisaslaşmaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Fəlsəfə tarixi | 65.5 | 65.5 |

</details>

---

### Proqram № 43

#### Blok 1 (Minimal bal: `50`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050117` | Rus dili və ədəbiyyatı müəllimliyi |
| `050103` | Xarici dil müəllimliyi (rus dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (rus dili)
  - rcümə
  - rcümə (rus dili)
  - Yaz l rbaycan dili-rus diliüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (rus dili üzrə) | 65 | 50 |
| Bakı Slavyan Universiteti | Dilşünaslıq (rus dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| *... və daha 4 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `50`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050121` | Xarici dil müəllimliyi rə b dili) ədəbiyyat b dili və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rəb dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |
| *... və daha 1 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050205` | Filologiya (ingilis dili və ədəbiyyatı) ədəbiyyat llimliyi (ingilis dili və ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi (ingilis dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - dəbiyyatı)
- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikası və metodologiyası(ingilis dili)
  - rcümə
  - (ingilis diliüzrə )
  - rcümə (ingilis dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Azərbaycan ədəbiyyatı | 65 | 61 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 64.5 | 52.5 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 62 | 62 |
| Azərbaycan Dillər Universiteti | Azərbaycan ədəbiyyatı | None | 53.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (rus dili üzrə) tədrisi | 63 | 53 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (ingilis dili üzrə) tədrisi | 63 | 51 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (alman dili üzrə) tədrisi | 64.5 | 64.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (fransız dili üzrə) tədrisi Ж | 66 | 54 |
| *... və daha 44 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat llimliyi (ispan dili və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)
  - rcümə

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyatı) ədəbiyyat llimliyi (alman dili və ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi (alman dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı ı
  - dəbiyyatı)
- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikası və metodologiyası(alman dili)
  - rcümə
  - (alman diliüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Azərbaycan ədəbiyyatı | 65 | 61 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 64.5 | 52.5 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 62 | 62 |
| Azərbaycan Dillər Universiteti | Azərbaycan ədəbiyyatı | None | 53.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (rus dili üzrə) tədrisi | 63 | 53 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (ingilis dili üzrə) tədrisi | 63 | 51 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (alman dili üzrə) tədrisi | 64.5 | 64.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (fransız dili üzrə) tədrisi Ж | 66 | 54 |
| *... və daha 40 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyatı) ədəbiyyat müəllimliyi (fransız dili və ədəbiyyatı) |
| `050103` | Xarici dil müəllimliyi (fransız dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı ı ı
  - dəbiyyatı)
- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikası və metodologiyası(fransız dili)
  - rcümə
  - rcümə (fransız dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Azərbaycan ədəbiyyatı | 65 | 61 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 64.5 | 52.5 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 62 | 62 |
| Azərbaycan Dillər Universiteti | Azərbaycan ədəbiyyatı | None | 53.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (rus dili üzrə) tədrisi | 63 | 53 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (ingilis dili üzrə) tədrisi | 63 | 51 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (alman dili üzrə) tədrisi | 64.5 | 64.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (fransız dili üzrə) tədrisi Ж | 66 | 54 |
| *... və daha 38 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Siyasə tin sosiologiyası
  - etmə nin sosiologiyası
  - Sosioloji tə dqiqatların metodları və metodologiyası
  - rcümə
  - rcümə (ingilis dili)
  - rcümə (ingilis dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Siyasətin sosiologiyası | 70 | 70 |
| Azərbaycan İlahiyyat İnstitutu | Dinin sosiologiyası | 50 | None |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İdarəetmənin sosiologiyası | 64 | 63 |
| Bakı Dövlət Universiteti | Sosioloji tədqiqatlar | 69 | 69 |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| *... və daha 4 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `40`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - dəbiyyatı)
- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikası və metodologiyası(ingilis dili)
  - rcümə

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Azərbaycan ədəbiyyatı | 65 | 61 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 64.5 | 52.5 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 62 | 62 |
| Azərbaycan Dillər Universiteti | Azərbaycan ədəbiyyatı | None | 53.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (rus dili üzrə) tədrisi | 63 | 53 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (ingilis dili üzrə) tədrisi | 63 | 51 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (alman dili üzrə) tədrisi | 64.5 | 64.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (fransız dili üzrə) tədrisi Ж | 66 | 54 |
| *... və daha 38 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (alman dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rcümə (alman dili)
  - biyyat mü ə llimliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 10 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (ispan dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - biyyatşünaslı dəbiyyatı)
  - Dilşünaslıq (alman dili)
  - rcümə
  - rcümə (ispan dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (alman dili üzrə) | 65.5 | 54.5 |
| Azərbaycan Dillər Universiteti | Dilşünaslıq (alman dili üzrə) | None | 58.5 |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| *... və daha 4 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 11 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (italyan dili) rcümə (italyan dili) rcümə (italyan dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rcümə (italyan dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 12 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | D rcümə (fransız dili) M - 2024 |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rcümə (fransız dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 13 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rcümə (rus dili)
  - Yazılı rbaycan dili-rus diliüzrə )
- ** `060201` Filologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 14 (Minimal bal: `40`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (polyak dili) rcümə (polyak dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - dəbiyyatı)
- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikası və metodologiyası(rus dili)
  - rcümə
  - rcümə (polyak dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Azərbaycan ədəbiyyatı | 65 | 61 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 64.5 | 52.5 |
| Azərbaycan Dillər Universiteti | Azərbaycan dili və ədəbiyyatının tədrisi | 62 | 62 |
| Azərbaycan Dillər Universiteti | Azərbaycan ədəbiyyatı | None | 53.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (rus dili üzrə) tədrisi | 63 | 53 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (ingilis dili üzrə) tədrisi | 63 | 51 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (alman dili üzrə) tədrisi | 64.5 | 64.5 |
| Azərbaycan Dillər Universiteti | Dil və ədəbiyyatın (fransız dili üzrə) tədrisi Ж | 66 | 54 |
| *... və daha 38 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 15 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (polyak dili) rcümə (Ukrayna dili) rcümə (Ukrayna dili) rcümə (Ukrayna dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Yazılı rbaycan dili- polyak diliüzrə )
  - rcümə
  - rcümə (Ukrayna dili)
  - Yazılı rbaycan dili - Ukrayna diliüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 16 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (çex dili) rcümə (çex dili) rcümə (çex dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rcümə (çex dili)
  - Yazılı rbaycan dili- çex diliüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 17 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (bolqar dili) rcümə (bolqar dili) rcümə (bolqar dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rcümə (bolqar dili)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 18 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (Koreya dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - (Koreya diliüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

#### Blok 19 (Minimal bal: `50`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rcümə
  - rcümə (Koreya dili)
- ** `060803` Turizm və otelçilik**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| Azərbaycan Dillər Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 57 |
| Azərbaycan Dillər Universiteti | Tərcümə (alman dili üzrə) | None | 53 |
| Azərbaycan Dillər Universiteti | Tərcümə (fransız dili üzrə) | 75 | 64.5 |
| Azərbaycan Dillər Universiteti | Tərcümə (italyan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ispan dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (koreya dili üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Tərcümə (ərəb dili üzrə) | None | 50 |
| Naxçıvan Dövlət Universiteti | Tərcümə (ingilis dili üzrə) | 69.5 | 50 |
| Gəncə Dövlət Universiteti | Tərcümə (ingilis dili) | 73.5 | 50 |
| Azərbaycan Kooperasiya Universiteti | Tərcümə (ingilis dili üzrə, tədris Azərbaycan dilində) | None | 50 |
| “Azərbaycan” Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Tərcümə (ingilis dili üzrə) İngilis dilində | 71 | 50 |
| Bakı Avrasiya Universiteti | Tərcümə (ingilis dili üzrə) | None | 50 |

</details>

---

### Proqram № 44

#### Blok 1 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050208` | Jurnalistika |
| `050216` | Kommunikasiya və qə msal media |
| `050204` | Jurnalistika |
| `HS 050100` | Jurnalistika |
| `HS 050200` | Beynə lxalq jurnalistika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Beynə lxalq jurnalistika
  - Mə tbuat tarixi
  - riyyə si
  - Publisistik jurnalistika
  - kommunikasiya sistemlə ri
  - Televiziya və radio yayımlarımenecmenti
  - İdman jurnalistikası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Beynəlxalq jurnalistika | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Beynəlxalq jurnalistika (tədris ingilis dilində) | None | 50.5 |
| Naxçıvan Dövlət Universiteti | Beynəlxalq jurnalistika | None | 50 |
| Bakı Dövlət Universiteti | Mətbuat tarixi | 58.5 | 50 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| *... və daha 45 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `50`, Səhifə: 52)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Jurnalistika ixtisasının ixtisaslaşmalarınıbütün r ali təhsilli rlər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060204` Jurnalistika**
  - Beynə lxalq jurnalistika
  - Mə tbuat tarixi
  - riyyə si
  - Publisistik jurnalistika
  - kommunikasiya sistemlə ri
  - Televiziya və radio yay mlar menecmenti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Radiotelejurnalistika | 57 | 50 |
| Bakı Dövlət Universiteti | Beynəlxalq jurnalistika | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Beynəlxalq jurnalistika (tədris ingilis dilində) | None | 50.5 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Publisistik jurnalistika | 51.5 | 50 |
| Bakı Dövlət Universiteti | İdman jurnalistikası | 53.5 | 50 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman jurnalistikası | None | 50 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman jurnalistikası İngilis dilində | None | 50 |
| Naxçıvan Dövlət Universiteti | Beynəlxalq jurnalistika | None | 50 |
| Bakı Dövlət Universiteti | Mətbuat tarixi | 58.5 | 50 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| *... və daha 46 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 45

#### Blok 1 (Minimal bal: `50`, Səhifə: 40)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050209` | kitabxanaçılıq və aliyyə ti |
| `050205` | Kitabş ünaslıq |
| `050215` | kitabxanaçılıq vİ ə informasiya i və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060205` Kitabşünaslıq**
  - etmə
  - rbaycan kitabşünaslığ ı
- ** `060215` Kitabxanaç ılıq və informasiya**
  - nə d resursları və informasiya-axtarı sistemlə ri
  - Kitabxanaşünaslıq
  - Biblioqrafiyaşünaslıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kitabxanaşünaslıq | None | 50 |
| Naxçıvan Dövlət Universiteti | Kitabxanaşünaslıq | None | 50 |
| Bakı Dövlət Universiteti | İqtisadiyyatda optimal idarəetmənin riyazi üsulları | 67 | 67 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Optimallaşdırma və optimal idarəetmə | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | İdarəetmənin sosiologiyası | 64.5 | 60 |
| Bakı Dövlət Universiteti | Nəşriyyat işi və redaktəetmə | None | 50 |
| Bakı Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | 68 | 60.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texniki sistemlərdə idarəetmə | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ümumi idarəetmə | None | 54.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ümumi idarəetmə İngilis dilində | None | 53.5 |
| *... və daha 57 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 46

#### Blok 1 (Minimal bal: `50`, Səhifə: 31)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060206` Tarix**
  - Azə rbaycanı srlə r tarixi
  - lə rinin tarixi
  - Qə dim dünya tarixi
  - Arxeologiya və etnoqrafiya
  - Etnologiya
  - Avropa və Amerikanı ə n yeni tarixi
  - Türk dünyasıtarixi
  - Qafqaz xalqlarının tarixi
  - Yaxı OrtaŞə rqin tarixi
  - srlə r tarixi
  - Azə rbaycanı ə n yeni tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Fəlsəfə tarixi | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Mətbuat tarixi | 58.5 | 50 |
| Bakı Dövlət Universiteti | Tarixin tədrisi | 63 | 60 |
| Bakı Dövlət Universiteti | Azərbaycanın qədim və orta əsrlər tarixi | 64 | 64 |
| Bakı Dövlət Universiteti | Asiya və Afrika ölkələrinin tarixi | 61 | 61 |
| Bakı Dövlət Universiteti | Qədim dünya tarixi | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Avropa və Amerikanın yeni və ən yeni tarixi | 69.5 | 69.5 |
| Bakı Dövlət Universiteti | Avropa və Amerikanın yeni və ən yeni tarixi İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Türk dünyası tarixi | 65 | 65 |
| Bakı Dövlət Universiteti | Yaxın və Orta Şərqin qədim tarixi | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Yaxın və Orta Şərqin qədim tarixi İngilis dilində | 69.5 | 69.5 |
| Bakı Dövlət Universiteti | Orta əsrlər tarixi | 63 | 63 |
| Bakı Dövlət Universiteti | Azərbaycanın yeni və ən yeni tarixi | 67 | 67 |
| Bakı Dövlət Universiteti | Azərbaycan tarixinin mənbəşünaslığı və tarixşünaslığı | 63.5 | 63.5 |
| *... və daha 54 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `50`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Qə dim dünya tarixi
  - Arxeologiya və etnoqrafiya
  - Etnologiya
  - Avropa və Amerikanı ə n yeni tarixi
  - Türk dünyasıtarixi
  - Qafqaz xalqlarının tarixi
  - Yaxı OrtaŞə rqin tarixi
  - srlə r tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Qədim dünya tarixi | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Arxeologiya | 62.5 | 58 |
| Bakı Dövlət Universiteti | Etnologiya və etnoqrafiya | None | 56 |
| Bakı Dövlət Universiteti | Avropa və Amerikanın yeni və ən yeni tarixi | 69.5 | 69.5 |
| Bakı Dövlət Universiteti | Avropa və Amerikanın yeni və ən yeni tarixi İngilis dilində | 70 | 70 |
| Gəncə Dövlət Universiteti | Avropa və Amerikanın yeni və ən yeni tarixi | 61.5 | 50 |
| Bakı Dövlət Universiteti | Türk dünyası tarixi | 65 | 65 |
| Naxçıvan Dövlət Universiteti | Türk dünyası tarixi | None | 50 |
| Gəncə Dövlət Universiteti | Türk dünyası tarixi | None | 50 |
| Bakı Dövlət Universiteti | Qafqaz xalqlarının tarixi | 63.5 | 63.5 |
| Qərbi Kaspi Universiteti | Qafqaz xalqlarının tarixi | None | 50 |
| Bakı Dövlət Universiteti | Azərbaycanın qədim və orta əsrlər tarixi | 64 | 64 |
| Bakı Dövlət Universiteti | Orta əsrlər tarixi | 63 | 63 |
| Naxçıvan Dövlət Universiteti | Azərbaycanın qədim və orta əsrlər tarixi | 67.5 | 67.5 |
| Gəncə Dövlət Universiteti | Azərbaycanın qədim və orta əsrlər tarixi | 61 | 57 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `50`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050116` | Tarix müəllimliyi |
| `050214` | Tarix |
| `050113` | Tarix müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060206` Tarix**
  - Azə rbaycanı srlə r tarixi
  - lə rinin tarixi
  - Qə dim dünya tarixi
  - Arxeologiya və etnoqrafiya
  - Etnologiya
  - Avropa və Amerikanı ə n yeni tarixi
  - Türk dünyasıtarixi
  - Qafqaz xalqlarının tarixi
  - Yaxı OrtaŞə rqin tarixi
  - srlə r tarixi
  - Azə rbaycanı ə n yeni tarixi
  - nbəş ünaslığ ı tarixşüna slığ ı
  - lə ri tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Fəlsəfə tarixi | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Mətbuat tarixi | 58.5 | 50 |
| Bakı Dövlət Universiteti | Tarixin tədrisi | 63 | 60 |
| Bakı Dövlət Universiteti | Azərbaycanın qədim və orta əsrlər tarixi | 64 | 64 |
| Bakı Dövlət Universiteti | Asiya və Afrika ölkələrinin tarixi | 61 | 61 |
| Bakı Dövlət Universiteti | Qədim dünya tarixi | 62.5 | 62.5 |
| Bakı Dövlət Universiteti | Avropa və Amerikanın yeni və ən yeni tarixi | 69.5 | 69.5 |
| Bakı Dövlət Universiteti | Avropa və Amerikanın yeni və ən yeni tarixi İngilis dilində | 70 | 70 |
| Bakı Dövlət Universiteti | Türk dünyası tarixi | 65 | 65 |
| Bakı Dövlət Universiteti | Yaxın və Orta Şərqin qədim tarixi | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Yaxın və Orta Şərqin qədim tarixi İngilis dilində | 69.5 | 69.5 |
| Bakı Dövlət Universiteti | Orta əsrlər tarixi | 63 | 63 |
| Bakı Dövlət Universiteti | Azərbaycanın yeni və ən yeni tarixi | 67 | 67 |
| Bakı Dövlət Universiteti | Azərbaycan tarixinin mənbəşünaslığı və tarixşünaslığı | 63.5 | 63.5 |
| *... və daha 54 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 47

#### Blok 1 (Minimal bal: `50`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050210` | Politologiya |
| `050208` | Politologiya |
| `HS 090100` | Politologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - niyyə tinin tarixi
- ** `060208` Politologiya**
  - sizlik və siyasi strategiya
  - rbaycanda siyasi proseslə r
  - Konfliktologiya
  - Siyasi analiz və konsaltinq
  - tlə r
  - Dünya siyasə ti
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Milli təhlükəsizlik və siyasi strategiya | 67 | 59 |
| Bakı Dövlət Universiteti | Azərbaycanda siyasi proseslər | None | 50 |
| Bakı Dövlət Universiteti | Konfliktologiya | None | 50 |
| Xəzər Universiteti | Konfliktologiya İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya | 71 | 55 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | 68.5 | 51.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Azərbaycan Texniki Universiteti | Liftlər və eskalatorlar | None | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Mülkiyyət obyektlərinin qiymətləndirilməsi | 64 | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər və diplomatiya | 72 | 54 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 57 |
| *... və daha 61 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `50`, Səhifə: 42)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050212` | Regionşünaslıq (regionlar üzrə ) |
| `050211` | Regionşünaslıq (regionlar üzrə ) |
| `HS 120100` | Regionşünaslıq (regionlarüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060211` Regionşünaslıq**
  - Ölkəş ünaslı rüzrə )
  - Regionşünaslıq (regionlarüzrə )
  - tlə r
  - r və diplomatiya
  - Dünya siyasə ti
  - Müasir danışı crübə si
  - riyyə si
  - riyyə si
  - Müasir dövrdə Yaxı rinin xarici siyasə ti
  - r və diplomatiya (Rusiyanın Xalqlar dostluğ u
  - birgə ikili diplom proqramı).
  - də ni
  - Avropaİttifaqının geosiyasə ti) (Bolqarıstanın Sofiya
  - Universiteti ilə ikili diplom proqramı)
- ** `060208` Politologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Regionşünaslıq (Azərbaycan üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Türkiyə üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Qafqaz ölkələri üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Amerika ölkələri üzrə) İngilis dilində | None | 50 |
| Azərbaycan Dillər Universiteti | Regionşünaslıq (İsrail və Yaxın Şərq üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Regionşünaslıq (Skandinaviya üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Regionşünaslıq (Mərkəzi və Şərqi Avropa üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Regionşünaslıq (Qafqaz üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Regionşünaslıq (ABŞ üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Regionşünaslıq (Böyük Britaniya üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Regionşünaslıq (Türkiyəşünaslıq) | None | 50 |
| Xəzər Universiteti | Regionşünaslıq (Avropaşünaslıq və Asiyaşünashq) İngilis dilində | None | 50 |
| Bakı Avrasiya Universiteti | Regionşünaslıq (ABŞ və Kanada üzrə) | None | 50 |
| Bakı Avrasiya Universiteti | Regionşünaslıq (Avropa ölkələri üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya | 71 | 55 |
| *... və daha 87 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `50`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 160100` | Beynə lxalq tlər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tlə r
  - r və diplomatiya
  - Dünya siyasə ti
  - Müasir danışı crübə si
  - riyyə si
  - riyyə si
  - Müasir dövrdə Yaxı rinin xarici siyasə ti
- ** `060208` Politologiya**
  - rbaycanda siyasi proseslə r

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya | 71 | 55 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | 68.5 | 51.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Azərbaycan Texniki Universiteti | Liftlər və eskalatorlar | None | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Mülkiyyət obyektlərinin qiymətləndirilməsi | 64 | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər və diplomatiya | 72 | 54 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 57 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | None | 50 |
| Bakı Mühəndislik Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 50 |
| Bakı Mühəndislik Universiteti | Sərnişindaşıma xidmətlərinin təşkili və təhlükəsizliyi | 43.5 | 43.5 |
| Azərbaycan Respublikası Prezidenti yanında Dövlət İdarəçilik Akademiyası | Beynəlxalq münasibətlər və diplomatiya | 72 | 72 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 48

#### Blok 1 (Minimal bal: `50`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060209` Psixologiya**
  - Ümumi psixologiya
  - Klinik psixologiya
  - yaşpsixologiyası
- ** `060505` Biologiya**
  - Molekulyar biologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 71 |
| Bakı Dövlət Universiteti | İnkişaf psixologiyası | 68 | 60 |
| Bakı Dövlət Universiteti | Məhkəmə psixologiyası | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Bakı Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | 68 | 60.5 |
| Azərbaycan Tibb Universiteti | Klinik (tibbi) psixologiya | 77.5 | 77.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| Azərbaycan Dillər Universiteti | Təhsil psixologiyası | None | 50 |
| Bakı Slavyan Universiteti | Təhsil psixologiyası | None | 53 |
| Naxçıvan Dövlət Universiteti | İnkişaf psixologiyası | 70 | 58 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil psixologiyası | None | 50 |
| Gəncə Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | None | 50 |
| Sumqayıt Dövlət Universiteti | Təhsil psixologiyası | None | 50 |
| “Azərbaycan” Universiteti | Təhsil psixologiyası | None | 50 |
| *... və daha 29 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `50`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060209` Psixologiya**
  - Ümumi psixologiya
  - Sosial psixologiya
  - nkişaf psixologiyası
  - Pedaqoji psixologiya
  - yaşpsixologiyası
  - Klinik psixologiya
  - btidai sinif mü ə llimliyi
  - drisin metodika və metodologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 71 |
| Bakı Dövlət Universiteti | İnkişaf psixologiyası | 68 | 60 |
| Bakı Dövlət Universiteti | Məhkəmə psixologiyası | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Bakı Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | 68 | 60.5 |
| Azərbaycan Tibb Universiteti | Klinik (tibbi) psixologiya | 77.5 | 77.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| Azərbaycan Dillər Universiteti | Təhsil psixologiyası | None | 50 |
| Bakı Slavyan Universiteti | Təhsil psixologiyası | None | 53 |
| Naxçıvan Dövlət Universiteti | İnkişaf psixologiyası | 70 | 58 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil psixologiyası | None | 50 |
| Gəncə Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | None | 50 |
| Sumqayıt Dövlət Universiteti | Təhsil psixologiyası | None | 50 |
| “Azərbaycan” Universiteti | Təhsil psixologiyası | None | 50 |
| *... və daha 11 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `50`, Səhifə: 41)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050211` | Psixologiya |
| `050209` | Psixologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Sosial psixologiya
  - Klinik psixologiya
  - nkişaf psixologiyası
  - Hüquq psixologiyası
  - Pedaqoji psixologiya
  - yaşpsixologiyas

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 68.5 |
| Qərbi Kaspi Universiteti | Sosial psixologiya | 78 | 50 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 71 |
| Azərbaycan Tibb Universiteti | Klinik (tibbi) psixologiya | 77.5 | 77.5 |
| Qərbi Kaspi Universiteti | Klinik (tibbi) psixologiya | 68 | 64.5 |
| Xəzər Universiteti | Klinik (tibbi) psixologiya | 70 | 70 |
| “Odlar Yurdu” Universiteti | Klinik (tibbi) psixologiya | 68 | 62.5 |
| Bakı Dövlət Universiteti | İnkişaf psixologiyası | 68 | 60 |
| Naxçıvan Dövlət Universiteti | İnkişaf psixologiyası | 70 | 58 |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| Azərbaycan Dillər Universiteti | Təhsil psixologiyası | None | 50 |
| Bakı Slavyan Universiteti | Təhsil psixologiyası | None | 53 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil psixologiyası | None | 50 |
| Sumqayıt Dövlət Universiteti | Təhsil psixologiyası | None | 50 |
| *... və daha 3 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `50`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - mə k hü ququ: sosial tə minat hüququ
  - Beynə lxalq iqtisadi hüquq
  - Ekoloji hüquq
  - Vergi hüququ
  - niyyə t hüququ
- ** `060209` Psixologiya**
  - Hüquq psixologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Əmək və sosial təminat hüququ | 71.5 | 71 |
| Bakı Dövlət Universiteti | Beynəlxalq iqtisadiyyat | 64 | 55.5 |
| Azərbaycan Texniki Universiteti | Beynəlxalq iqtisadiyyat | 63.5 | 52 |
| Azərbaycan Dövlət İqtisad Universiteti | Beynəlxalq iqtisadiyyat | 68.5 | 68.5 |
| Milli Aviasiya Akademiyası | Beynəlxalq iqtisadiyyat | 68 | 68 |
| Dövlət Gömrük Komitəsinin Akademiyası | Beynəlxalq iqtisadi hüquq | None | 65.5 |
| Naxçıvan Dövlət Universiteti | Beynəlxalq iqtisadiyyat | 68.5 | 53.5 |
| “Odlar Yurdu” Universiteti | Beynəlxalq iqtisadiyyat | None | 45 |
| Bakı Biznes Universiteti | Beynəlxalq iqtisadiyyat | 66.5 | 45 |
| Bakı Dövlət Universiteti | Vergi hüququ | 78.5 | 78.5 |
| Bakı Dövlət Universiteti | Mədəniyyət hüququ | None | 56.5 |
| Bakı Dövlət Universiteti | Mədəniyyət hüququ İngilis dilində | None | 57 |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 71 |
| Bakı Dövlət Universiteti | İnkişaf psixologiyası | 68 | 60 |
| *... və daha 23 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `50`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | kim işi işi kim işi iş iİ D kim işi M - 2024 |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Biotexnologiya
- ** `060209` Psixologiya**
  - Ümumi psixologiya
  - Klinik psixologiya
  - nkişaf psixologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Nanobiotexnologiya | None | 45 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 71 |
| Bakı Dövlət Universiteti | İnkişaf psixologiyası | 68 | 60 |
| Bakı Dövlət Universiteti | Məhkəmə psixologiyası | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Bakı Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | 68 | 60.5 |
| Azərbaycan Tibb Universiteti | Klinik (tibbi) psixologiya | 77.5 | 77.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| *... və daha 18 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `50`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050904` | Tibb |
| `050802` | Pediatriya |
| `HS 190200` | Pediatriya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Biotexnologiya
- ** `060209` Psixologiya**
  - Ümumi psixologiya
  - Klinik psixologiya
  - nkişaf psixologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Nanobiotexnologiya | None | 45 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 71 |
| Bakı Dövlət Universiteti | İnkişaf psixologiyası | 68 | 60 |
| Bakı Dövlət Universiteti | Məhkəmə psixologiyası | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Bakı Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | 68 | 60.5 |
| Azərbaycan Tibb Universiteti | Klinik (tibbi) psixologiya | 77.5 | 77.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| *... və daha 18 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `50`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060209` Psixologiya**
  - Ümumi psixologiya
  - Klinik psixologiya
- ** `060505` Biologiya**
  - Molekulyar biologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Sosial psixologiya | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Klinik (tibbi) psixologiya | 71 | 71 |
| Bakı Dövlət Universiteti | İnkişaf psixologiyası | 68 | 60 |
| Bakı Dövlət Universiteti | Məhkəmə psixologiyası | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Təhsil psixologiyası | 68 | 56 |
| Bakı Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | 68 | 60.5 |
| Azərbaycan Tibb Universiteti | Klinik (tibbi) psixologiya | 77.5 | 77.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil psixologiyası | None | 50 |
| Azərbaycan Dillər Universiteti | Təhsil psixologiyası | None | 50 |
| Bakı Slavyan Universiteti | Təhsil psixologiyası | None | 53 |
| Naxçıvan Dövlət Universiteti | İnkişaf psixologiyası | 70 | 58 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil psixologiyası | None | 50 |
| Gəncə Dövlət Universiteti | Uşaq və yeniyetmə psixologiyası | None | 50 |
| Sumqayıt Dövlət Universiteti | Təhsil psixologiyası | None | 50 |
| “Azərbaycan” Universiteti | Təhsil psixologiyası | None | 50 |
| *... və daha 29 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 49

#### Blok 1 (Minimal bal: `50`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050206` | Hüquqşünaslıq |
| `050212` | Hüquqşünaslıq |
| `HS 130100` | Hüquqşünaslıq |
| `HS 200100` | Beynə lxalq hüquq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Konstitusiya hüququ
  - mə ekspertizası
  - sə rrüfat hüququ
  - İnsan hüquqları
  - Transmilli cinayə t hüququ
  - İnformasiya hüququ
  - Kommersiya hüququ
  - Avropa hüququ
  - niz və enerji hüququ
  - qli mülkiyyə t hüququ
  - Tibbi hüquq
  - Turizm hüququ
  - İdman hüququ
  - maliyyə hüququ

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Cinayət prosesi, kriminalistika, məlikəmə ekspertizası və əməliyyat-axtarış fəaliyyəti | 79.5 | 79.5 |
| Naxçıvan Dövlət Universiteti | Cinayət prosesi, kriminalistika, məhkəmə ekspertizası və əməliyyat-axtarış fəaliyyəti | 77 | 67.5 |
| Bakı Dövlət Universiteti | İnsan haqları hüququ | 73.5 | 67 |
| Bakı Dövlət Universiteti | Transmilli cinayət hüququ | 73 | 73 |
| Bakı Dövlət Universiteti | İnformasiya hüququ | 71 | 67.5 |
| Bakı Dövlət Universiteti | Kommersiya hüququ | 81 | 81 |
| Bakı Dövlət Universiteti | Kommersiya hüququ İngilis dilində | 86.5 | 86.5 |
| Bakı Dövlət Universiteti | Avropa hüququ | 72 | 63 |
| Bakı Dövlət Universiteti | Dəniz və enerji hüququ İngilis dilində | 76 | 65.5 |
| Bakı Dövlət Universiteti | Əqli mülkiyyət hüququ | 72.5 | 65.5 |
| Bakı Dövlət Universiteti | Əqli mülkiyyət hüququ İngilis dilində | 76 | 76 |
| Bakı Dövlət Universiteti | Tibb hüququ | 71 | 62.5 |

</details>

---

### Proqram № 50

#### Blok 1 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 140100` | İnstrumental ifaç ılıq riüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - stə karlıq
- ** `060303` İnstrumental ifaç ılıq**
  - İnstrumental ifaç ılığ ı si və metodikası tlə ri
  - üzrə )
- ** `060307` Musiqişünaslıq**
  - Musiqi tarixi
  - riyyə si
  - Etnomusiqişünasl q

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Bəstəkarlıq (akademik bəstəkarlıq, audiovizual və teatr musiqisi) | 46.5 | 30 |
| Azərbaycan Milli Konservatoriyası | Akademik bəstəkarlıq | 32 | 30 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk xalqları dilləri üzrə) | 65.5 | 57.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (rus dili üzrə) | 65 | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (ingilis dili üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fransız dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (alman dili üzrə) | 65.5 | 54.5 |
| Bakı Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fars dili üzrə) | None | 58 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk dili üzrə) | None | 50 |
| *... və daha 110 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Musiqi texnologiyaları
- ** `060310` Xalqçalğ ı tlə ri ifaç ılığ ı**
  - Xalqçalğ ı tlə ri ifaç ılığ ını si və metodikası
- ** `060310` Xalqçalğ ı tlə ri ifaç ılığ ı**
  - Xalqçalğ tlə ri ifaç lğ riüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Musiqi texnologiyaları | 50 | 48 |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 140200` | Solooxuma |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Populyar musiqi və caz ifaç ılığ ı
- ** `060304` Solooxuma**
  - Vokal ifaç ılığ ını riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Milli Konservatoriyası | Populyar musiqi və caz ifaçılığı (vokal, tar, kamança, qanun, balaban,fortepiano, violin, akkordeon, saksofon, klarnet, fleyta, qoboy, truba, gitara, zərb alətləri) | 39.5 | 39.5 |
| Bakı Musiqi Akademiyası | Vokal | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Vokal | 41.5 | 41.5 |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050317` | Vokal rüzrə ) |
| `050304` | Solooxuma |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060304` Solooxuma**
  - Vokal ifaç ılığ ını riyyə si
- ** `060304` Solooxuma**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Vokal | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Vokal | 41.5 | 41.5 |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | stə karlıq stə karlıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Musiqi tarixi
  - riyyə si
  - Musiqi tə nqidi
  - Etnomusiqişünaslıq
  - Musiqi texnologiyalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| Azərbaycan Milli Konservatoriyası | Musiqi tarixi və nəzəriyyəsi | 49 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Musiqi tarixi və nəzəriyyəsi | 50.5 | 47.5 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| *... və daha 30 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050305` | Dirijorluq |
| `HS 140300` | Dirijorluq |
| `HS 152600` | Xalqçalğ ı tlə ri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060303` İnstrumental ifaç ılıq**
  - İnstrumental ifaç ılığ ı si və metodikası tlə ri
  - üzrə )
- ** `060307` Musiqişünaslıq**
  - Etnomusiqişünaslıq
  - Musiqi tə nqidi
  - Musiqi tarixi
  - riyyə si
  - Musiqi texnologiyaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk xalqları dilləri üzrə) | 65.5 | 57.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (rus dili üzrə) | 65 | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (ingilis dili üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fransız dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (alman dili üzrə) | 65.5 | 54.5 |
| Bakı Dövlət Universiteti | Dilşünaslıq (ərəb dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (fars dili üzrə) | None | 58 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Dilşünaslıq (yapon dili üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Tərcümə (ərəb dili üzrə) | None | 51 |
| *... və daha 110 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050309` | musiqişünaslıq |
| `050307` | Musiqiş ünasl q |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Etnomusiqişünaslıq
  - Musiqi tə nqidi
  - Musiqi tarixi
  - riyyə si
  - Musiqi texnologiyaları
- ** `060303` İnstrumental ifaç l q**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Etnomusiqişünaslıq | 49.5 | 43 |
| Azərbaycan Milli Konservatoriyası | Etnomusiqişünaslıq | 49 | 43 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Etnomusiqişünaslıq | None | 45 |
| Naxçıvan Dövlət Universiteti | Musiqi tənqidi | None | 42.5 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| Azərbaycan Milli Konservatoriyası | Musiqi tarixi və nəzəriyyəsi | 49 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Musiqi tarixi və nəzəriyyəsi | 50.5 | 47.5 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| *... və daha 30 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 51

#### Blok 1 (Minimal bal: `50`, Səhifə: 43)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050202` | Dinşünaslıq slamşünaslıq |
| `050214` | Dinşünaslıq |
| `HS 180100` | Dinşünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060214` Dinşünaslıq**
  - slamşünaslıq
  - Dinlə rin tarixi
  - Dinin psixologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| Azərbaycan İlahiyyat İnstitutu | Dinlərin tarixi | 55.5 | None |

</details>

---

### Proqram № 52

#### Blok 1 (Minimal bal: `30`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060707` Balıqç ılıq və balıqç ılı sə rrüfatıişi**
  - Balıqç ılıq
  - Balıqç ılı sə rrüfatıişi
- ** `060510` Ekologiya**
  - traf mühitin mühafizə metodları bə rpası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Ekologiya hüququ | None | 57 |
| Azərbaycan Tibb Universiteti | Mama-ginekologiyada tibb bacısı (qardaşı) işi | 64 | 40 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Lənkəran Dövlət Universiteti | Baytarlıq təbabətində mamalıq- ginekologiya və süni mayalanma | None | 30 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| *... və daha 2 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 20)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060709` Su bioehtiyatları akvabitkilə r**
  - Suı
  - Akvabitkilə r
- ** `060707` Balıqç ılıq və balıqç ılı sə rrüfatıişi**
  - Balıqç ılıq
  - Balıqç ılı sə rrüfatıişi
- ** `060510` Ekologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Ekologiya hüququ | None | 57 |
| Azərbaycan Tibb Universiteti | Mama-ginekologiyada tibb bacısı (qardaşı) işi | 64 | 40 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Lənkəran Dövlət Universiteti | Baytarlıq təbabətində mamalıq- ginekologiya və süni mayalanma | None | 30 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - idmanda tibbi-bioloji təminat
- ** `060709` Su bioehtiyatları akvabitkilə r**
  - Su bioehtiyatları
  - Akvabitkilə r
- ** `060707` Balıqç ılıq və balıqç ılı sə rrüfatıişi**
  - Balıqç ılıq
  - Balıqç ılı sə rrüfatıişi
- ** `060701` Torpaqşünaslıq və aqrokimya**
  - Aqrokimya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Bakı Dövlət Universiteti | Torpaqşünaslıq | 54.5 | 54.5 |
| Naxçıvan Dövlət Universiteti | Torpaqşünaslıq | 43.5 | 30 |
| Lənkəran Dövlət Universiteti | Torpaqşünaslıq | 40.5 | 30 |
| Bakı Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 56.5 | 56.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrokimya və torpaq münbitliyinin idarə olunması (tədris Azərbaycan dilində) | 39 | 39 |
| Lənkəran Dövlət Universiteti | Aqrokimya və torpaq münbitliyinin idarə olunması | 44 | 44 |

</details>

---

### Proqram № 53

#### Blok 1 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050315` | Rə ngkarlıq |
| `050318` | Rə ngkarlıq nə ti |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - rinin bə rpası və ekspertizası
  - riyyə si
  - Rə nkarlığ ı riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 44 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050313` | Qrafika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - rinin bə rpası və ekspertizası
  - riyyə si
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 44 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nə t rüzrə ) nə t |
| `HS 151300` | Dekorativ-tə tbiqi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - rinin bə rpası və ekspertizası
  - riyyə si
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 44 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - rinin bə rpası və ekspertizası
  - riyyə si
  - ltaraşlığ ı riyyə si
- ** `060321` Dizayn**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 67 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050321` | Dizayn |
| `HS 151400` | Dizayn rə ssam |
| `HS 154200` | Modelyer rə ssam |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Dizayn və texniki estetika
  - Vizual dizayn və media
  - aft bağ çılığ ı
  - riyyə si
  - tşünaslıq
  - rinin bə rpası və ekspertizası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Vizual dizayn | 52 | 30 |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| *... və daha 45 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - rinin bə rpası və ekspertizası
  - riyyə si
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 44 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | tşünaslı lər üzrə ) tşünaslıq nə t tarixi riyyə si ti və dekorativ kosmetologiya rlərinin bərpası və ekspertizası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - rinin bə rpası və ekspertizası
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 44 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `30`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050321` | Dizayn iaşə bə dii tə rtibat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060321` Dizayn**
  - Dizayn və texniki estetika
  - Vizual dizayn və media
  - aft bağ çılıq
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq mühitinin dizaynı | 43.5 | 43.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnteryer dizaynı | 52 | 44.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Qrafik dizayn | 52.5 | 37 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Vizual dizayn | 52 | 30 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texniki dizayn | None | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | Geyim dizaynı | None | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | İnteryer dizaynı | 52.5 | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | Qrafik dizayn | 52.5 | 46 |
| Bakı Mühəndislik Universiteti | Memarlıq mühitinin dizaynı | 49 | 49 |
| Bakı Mühəndislik Universiteti | Sənaye dizaynı | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Geyim dizaynı | 32 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İnteryer dizaynı | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Qrafik dizayn | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sənaye dizaynı | None | 30 |
| *... və daha 48 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 54

#### Blok 1 (Minimal bal: `45`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Bioekologiya
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
  - si və idman

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| *... və daha 68 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və idman
  - si və metodikası
  - si və metodikası
  - idmanda tibbi-bioloji tə minat

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050805` | Məş qçilik si və idman qçi (idman növü üzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və metodikası
  - si və metodikası
  - idmanda tibbi-bioloji tə minat
  - ə çağ ırı də rki hazırlıq (qızlarüçün fiziki

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və idman
  - idmanda tibbi-bioloji tə minat
  - dman tibbi və reabilitasiya (rezidenturan kimlə rüçün)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 49)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və idman
  - idmanda tibbi-bioloji tə minat
  - dman tibbi və reabilitasiya (rezidenturanı kimlə rüçün)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |

</details>

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050808` | Tibb bacısıişi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və idman
  - idmanda tibbi-bioloji tə minat

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |

</details>

---

#### Blok 7 (Minimal bal: `30`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və idman
  - ə minat

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Əmək və sosial təminat hüququ | 71.5 | 71 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Metrologiya və metroloji təminat | 50.5 | 40 |
| Azərbaycan Texniki Universiteti | Metrologiya və metroloji təminat | 50 | 45.5 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |
| Milli Aviasiya Akademiyası | Aeronaviqasiya təminatı İngilis dilində | 74 | 40 |
| Milli Aviasiya Akademiyası | Uçuşların təhlükəsizliyinin təminatı və idarə edilməsi İngilis dilində | None | 40 |

</details>

---

#### Blok 8 (Minimal bal: `30`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | si və idmanda reabilitasiya |
| `050803` | Fizioterapiya və tibbi reabilitasiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və idman
  - si və metodikası
  - si və metodikası
  - idmanda tibbi-bioloji tə minat

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdmanda tibbi-bioloji təminat | 59 | 59 |

</details>

---

### Proqram № 55

#### Blok 1 (Minimal bal: `40`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060801` Ə czaç ılıq**
  - Ə czaç ılıq kimyası
- ** `060612` Maşın mühəndisliyi**
  - Maşınqayırma texnologiyası
  - Maşınqayırmada kompüter texnologiyaları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Tibb Universiteti | Əczaçılıq menecmenti | None | 45 |
| Azərbaycan Tibb Universiteti | Əczaçılıq kimyası | 67 | 67 |
| Azərbaycan Tibb Universiteti | Əczaçılıq texnologiyası | 60 | 60 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Əczaçılıq kimyası (tədris Azərbaycan dilində) | 52 | 52 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası | 40.5 | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası Alman dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Maşınqayırma texnologiyası İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Cihazqayırma texnologiyası | 53 | 45.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları | 44.5 | 44.5 |
| Azərbaycan Texniki Universiteti | Maşınqayırmada kompüter texnologiyaları İngilis dilində | 51.5 | 40 |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 25)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)
- ** `060801` Ə czaç ılıq**
  - Ə czaç ılıq kimyası
  - Toksikoloji kimya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 94 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 27)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Mey və çilik
  - və zçilik
  - Üzümçülük
  - Bitkilə rin seleksiyası
  - Aqrogeobotanika
  - sə rrüfatınınə sasları
  - Bitki anatomiyası və morfologiyası
  - sə rrüfatı
- ** `060801` Ə czaç ılıq**
  - Ə czaç ılıq kimyası
  - Farmakoqnoziya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Botanika | 64.5 | 64.5 |
| Naxçıvan Dövlət Universiteti | Botanika | 47 | 45 |
| Gəncə Dövlət Universiteti | Botanika | 49.5 | 49.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Bitki anatomiyası və morfologiyası (tədris Azərbaycan dilində) | 45 | 45 |
| Azərbaycan Texniki Universiteti | Lokomotiv və vaqon təsərrüfatı | None | 40 |
| Azərbaycan Texniki Universiteti | Dəmiryolu təsərrüfatı və onun istismarı | 54.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin genetikası (tədris Azərbaycan dilində) | 39.5 | 39.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı heyvanlarının yetişdirilməsi, genetikası və seleksiyası (tədris Azərbaycan dilində) | 33.5 | 33.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Dəmiryolu təsərrüfatı və onun istismarı | None | 40 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu | 33.5 | 30 |
| Azərbaycan Tibb Universiteti | Əczaçılıq menecmenti | None | 45 |
| *... və daha 4 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 28)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Aqrogeobotanika
  - sərrüfatınınəsasları
  - Bitki anatomiyasıvə morfologiyası
  - sərrüfatı
- ** `060801` Ə czaç ılıq**
  - Ə czaç ılıq kimyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Botanika | 64.5 | 64.5 |
| Naxçıvan Dövlət Universiteti | Botanika | 47 | 45 |
| Gəncə Dövlət Universiteti | Botanika | 49.5 | 49.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Bitki anatomiyası və morfologiyası (tədris Azərbaycan dilində) | 45 | 45 |
| Azərbaycan Texniki Universiteti | Lokomotiv və vaqon təsərrüfatı | None | 40 |
| Azərbaycan Texniki Universiteti | Dəmiryolu təsərrüfatı və onun istismarı | 54.5 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin genetikası (tədris Azərbaycan dilində) | 39.5 | 39.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı heyvanlarının yetişdirilməsi, genetikası və seleksiyası (tədris Azərbaycan dilində) | 33.5 | 33.5 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Balıqçılıq təsərrüfatı işi (tədris Azərbaycan dilində) | 39 | 39 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Dəmiryolu təsərrüfatı və onun istismarı | None | 40 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin seleksiyası və toxumçuluğu | 33.5 | 30 |
| Azərbaycan Tibb Universiteti | Əczaçılıq menecmenti | None | 45 |
| *... və daha 3 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 50)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Ə czaç ılıq kimyası
  - Farmakoqnoziya
  - Ə czaç ılıq texnologiyası
  - Toksikoloji kimya
  - Ə czaç ılığ ın təş kili

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Tibb Universiteti | Əczaçılıq kimyası | 67 | 67 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Əczaçılıq kimyası (tədris Azərbaycan dilində) | 52 | 52 |
| Azərbaycan Tibb Universiteti | Farmakoqnoziya | 55 | 55 |
| Azərbaycan Tibb Universiteti | Əczaçılıq texnologiyası | 60 | 60 |
| Bakı Dövlət Universiteti | Ekoloji kimya | 61 | 53 |
| Azərbaycan Tibb Universiteti | Toksikoloji kimya | 75.5 | 75.5 |
| Naxçıvan Dövlət Universiteti | Toksikoloji kimya | 47.5 | 40 |

</details>

---

### Proqram № 56

#### Blok 1 (Minimal bal: `45`, Səhifə: 52)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | MBA proqramınıbütün r ali təhsilli rlər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı
  - İdman jurnalistikası
  - MBA proqramıüzrə
  - edilmə si
  - rüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdman jurnalistikası | 53.5 | 50 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman jurnalistikası | None | 50 |
| Azərbaycan Respublikası Gənclər və İdman Nazirliyinin Azərbaycan İdman Akademiyası | İdman jurnalistikası İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Su ehtiyatlarının inteqrasiyalı idarə edilməsi | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnologiyalar və əməliyyatların idarə edilməsi | 62.5 | 62.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya texnologiyalarının idarə edilməsi | None | 60 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya texnologiyalarının idarə edilməsi İngilis dilində | None | 58.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Əməliyyatların idarə edilməsi | None | 47.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Əməliyyatların idarə edilməsi İngilis dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyat əməliyyatlarının intellektual idarə edilməsi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Texniki Universiteti | Energetika sistemlərinin avtomatik idarə edilməsi | 54.5 | 40 |
| Azərbaycan Texniki Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 61.5 | 61.5 |
| *... və daha 100 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 57

#### Blok 1 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050811` | nəqliyyat servisi (avtomobil nəqliyyatıüzrə ) nəqliyyat maşın və avadanlıqlarının quraşdırılması, texniki istismarı servis xidməti rüzrə ) lərinin servis xidməti lə dçiliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - riüzrə )
  - Avtomobil servisinin texnologiyası
  - mir yolu nə qliyyatı tinin təş kili

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk xalqları dilləri üzrə) | 65.5 | 57.5 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Qafqaz ölkələri üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Amerika ölkələri üzrə) İngilis dilində | None | 50 |
| Bakı Mühəndislik Universiteti | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 55.5 | 51.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Nəqliyyatda daşımalar və menecment (nəqliyyat növləri üzrə) | 57 | 44.5 |
| Bakı Avrasiya Universiteti | Regionşünaslıq (Avropa ölkələri üzrə) | None | 50 |

</details>

---

### Proqram № 58

#### Blok 1 (Minimal bal: `40`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050614` | Aviasiya texnikası avadanlıqlarının istismarı mühəndisliyi |
| `T 070300` | Uçan aparatların və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı ı ı
  - Güc elektronikası
- ** `060648` Biotibbi texnika mühəndisliyi**
  - ndis işi
  - Biotibbi və radioelektron aparatlarına servis xidmə ti
  - sistemlə r
  - texniki diaqnostiküsul və cihazlar
- ** `060614` Aviasiya texnikasıavadanlıqlarının istismarımühəndisliyi**
  - Uçuşaparatları güc qurğ uları
  - Uçuşaparatlarının elektrik, radio və cihaz avadanlıqları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Güc elektronikası | 43 | 40 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Güc elektronikası | 43.5 | 40 |
| Xəzər Universiteti | Güc elektronikası İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diskret sistemlər | 61 | 61 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| *... və daha 90 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `40`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050613` | Hava nəqliyyatının tinin təşkili |
| `050615` | Hava nəqliyyatının tinin idarə olunması mühəndisliyi |
| `T 100700` | Hava nəqliyyatının istismar kə tinin |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060615` Hava nə qliyyatını tinin idarə olunmasımühəndisliyi**
  - Hava nə qliyyatı tinin idarə olunması
  - Aeronaviqasiya tə minatı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Hava nəqliyyatı hərəkətinin idarə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Aeronaviqasiya təminatı İngilis dilində | 74 | 40 |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 15)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | edilmə si mühəndisliyi mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - mühəndisliyi
  - rinin uçuşistismarı
- ** `060503` Fizika**
  - ri və riyazi fizika
  - rk cisimlə r fizikası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar | 57.5 | 57.5 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar İngilis dilində | 65 | 63.5 |
| Milli Aviasiya Akademiyası | Hava gəmilərinin uçuş istismarı İngilis dilində | None | 40 |
| Bakı Dövlət Universiteti | Riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Fizikanın tədrisi | 69 | 69 |
| Bakı Dövlət Universiteti | Nəzəri və riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bərk cisimlər fizikası | 64 | 64 |
| Bakı Dövlət Universiteti | Tətbiqi fizika (yarımkeçiricilər və dielektriklər fizikası) | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Tətbiqi fizika (yarımkeçiricilər və dielektriklər fizikası) İngilis dilində | 74 | 45 |
| Bakı Dövlət Universiteti | İstilik fizikası və molekulyar fizika | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Astrofizika | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Nanofizika və nanotexnologiyalar | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Nanofizika və nanotexnologiyalar İngilis dilində | 56.5 | 45 |
| Bakı Dövlət Universiteti | Yüksək enerjilər fizikası | 61 | 61 |
| *... və daha 12 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050629` | Mexatronika və robototexnika mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060614` Aviasiya texnikasıavadanlıqlarının istismarımühəndisliyi**
  - Uçuşaparatları güc qurğ uları
  - Uçuşaparatlarının elektrik, radio və cihaz avadanlıqları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Uçuş aparatları və güc qurğuları | 52.5 | 52.5 |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050601` | Aerokosmik mühəndisliyi edilmə si |
| `050403` | Davamlıinkişafın idarə |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060614` Aviasiya texnikasıavadanlıqlarının istismarımühəndisliyi**
  - Uçuşaparatları güc qurğ uları
  - Uçuşaparatlarının elektrik, radio və cihaz avadanlıqları

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Milli Aviasiya Akademiyası | Uçuş aparatları və güc qurğuları | 52.5 | 52.5 |

</details>

---

### Proqram № 60

#### Blok 1 (Minimal bal: `40`, Səhifə: 16)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050601` | Aerokosmik mühəndisliyi |
| `050652` | Kosmik texnologiyalar mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - texnologiyalar mühəndisliyi
  - sistemlə ri

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar | 57.5 | 57.5 |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İdarəetmədə informasiya sistemləri | 70 | 70 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| *... və daha 63 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 61

#### Blok 1 (Minimal bal: `30`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | sistemlərinin istehsal texnologiyası |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Maşı yədavamlılığ ını bə rpası
  - texnologiyasıvə avadanlığ ı
  - Avadanlıqların bərpası möhkə mliyinin artırılması
  - silah sistemlə rinin istehsal texnologiyası
  - Atıcı, artilleriya və raket silahlarının istehsal texnologiyası
  - Döyü şsursatları lə rin istehsal texnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Azərbaycan Texniki Universiteti | Atıcı artilleriya və raket silahlarının istehsal texnologiyası | 45.5 | None |

</details>

---

### Proqram № 62

#### Blok 1 (Minimal bal: `30`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050103` | Optotexnika mühəndisliyi XTB |
| `050002` | Optotexnika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - XTM 060002 Optotexnika
  - Lazer texnikası və texnologiyası
  - sistemlə r

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diskret sistemlər | 61 | 61 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bioloji sistemlər fizikası | 59 | 59 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri | 52.5 | 52.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İntellektual ölçmə və idarəetmə sistemləri İngilis dilində | 64.5 | 64.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər | 50 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Biotexniki və tibbi aparatlar və sistemlər İngilis dilində | 52.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Çoxkanallı telekommunikasiya sistemləri | 49 | 40 |
| *... və daha 86 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 63

#### Blok 1 (Minimal bal: `30`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050104` | Pirotexniki və partladıcı r mühəndisliyi lə rin |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - lə rin texnologiyası
  - Barıtları bə rk raket yanacaqlarının kimya texnologiyası
  - Partlayıcımə mulatların texnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Pedaqoji Universiteti | Texnologiyanın tədrisi | None | 48.5 |
| Naxçıvan Dövlət Universiteti | Texnologiyanın tədrisi | None | 45.5 |
| Gəncə Dövlət Universiteti | Texnologiyanın tədrisi | None | 44 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Alkoqollu içkilərin texnologiyası | None | 40 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Alkoqolsuz və az alkoqollu içkilərin texnologiyası | None | 40 |
| Lənkəran Dövlət Universiteti | Texnologiyanın tədrisi | None | 41 |

</details>

---

### Proqram № 64

#### Blok 1 (Minimal bal: `30`, Səhifə: 17)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | lə ri mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı ı
  - hazırlanması, istismarı tə miri
  - k tezliklər texnikası
  - lə ri
  - lə ri
  - radiotexnika mühəndisliyi
  - r və televiziya
  - Radiotexnika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İdarəetmədə informasiya sistemləri | 71.5 | 71.5 |
| Bakı Dövlət Universiteti | Kompüter sistemləri və şəbəkələri | 75.5 | 75.5 |
| Bakı Dövlət Universiteti | Diferensial tənliklər İngilis dilində | 77 | 55.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Bakı Dövlət Universiteti | Dilşünaslıq (türk xalqları dilləri üzrə) | 65.5 | 57.5 |
| Bakı Dövlət Universiteti | Həyat fəaliyyətinin müxtəlif sahələrində sosial iş | 75 | 75 |
| Bakı Dövlət Universiteti | Media və kommunikasiya sistemləri | 56 | 55 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri | None | 50 |
| Bakı Dövlət Universiteti | Kitabxana informasiya-axtarış sistemləri İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Asiya və Afrika ölkələrinin tarixi | 61 | 61 |
| Bakı Dövlət Universiteti | Slavyan ölkələri tarixi | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Qafqaz ölkələri üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Regionşünaslıq (Amerika ölkələri üzrə) İngilis dilində | None | 50 |
| *... və daha 209 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 65

#### Blok 1 (Minimal bal: `30`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050101` | Hə rbi kompozisiya materiallarımühəndisliyi XTB |
| `050005` | Kompozisiya materiallar ndan müdafiə |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - XTM 060005 Kompozisiya materialları tə yinatlı
  - mə mulatları si və istehsalı
  - Metalə saslıkompozisiya materialları rbi tə yinatlımə mulatların
  - istehsalı
  - Qeyri-metalə saslıkompozisiya materialları rbi tə yinatlı
  - mə mulatların istehsalı
- ** `060611` Metallurgiya mühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Enerji maşınlarının istehsalı | 42.5 | 40 |
| Azərbaycan Texniki Universiteti | Qaynaq istehsalı metallurgiyası, texnologiyası və avadanlığı | 40 | 40 |
| Azərbaycan Texniki Universiteti | Enerji maşınlarının istehsalı | 43 | 40 |
| Azərbaycan Texniki Universiteti | Texnoloji maşın və avadanlıqların istehsalı, təmiri və texniki xidmət texnologiyaları | 44.5 | 40 |
| Bakı Mühəndislik Universiteti | Tökmə və qaynaq istehsalının maşın və avadanlıqları | None | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Aqrar istehsalın və texnoloji proseslərin təhlükəsizliyi (tədris Azərbaycan dilində) | 51 | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Şərabçılıq və qıcqırtma istehsalının texnologiyası (tədris Azərbaycan dilində) | None | 40 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Arıçılıq və baramaçılıq məhsulları istehsalında innovativ texnologiyalar (tədris Azərbaycan dilində) | 42 | 30 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Heyvandarlıq məhsulları istehsalının texnologiyası (tədris Azərbaycan dilində) | 32 | 30 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Qida istehsalının idarə edilməsi | 42.5 | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Şərabçılıq və qıcqırtma istehsalının texnologiyası | None | 40 |
| Lənkəran Dövlət Universiteti | Qida istehsalının idarə edilməsi | None | 40 |
| Azərbaycan Kooperasiya Universiteti | Qida istehsalının idarə edilməsi (tədris Azərbaycan dilində) | 50 | 50 |
| Azərbaycan Kooperasiya Universiteti | Şərabçılıq və qıcqırtma istehsalının texnologiyası (tədris Azərbaycan dilində) | None | 45 |

</details>

---

### Proqram № 68

#### Blok 1 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050308` | İnstrumental ifaç ılıq rüzrə ) |
| `050303` | İnstrumental ifaç ılıq riüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060303` İnstrumental ifaç ılıq**
  - İnstrumental ifaç ılı riüzrə )
  - nə ti
  - Populyar musiqi və caz ifaç ılığ ı
- ** `060305` Dirijorluq**
  - tlə ri
  - orkestri dirijorluğ u)
- ** `060304` Solooxuma**
  - Vokal ifaç ılığ ı(akademik)
  - stə karlıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 30 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050308` | İnstrumental ifaç ılıq rüzrə ) |
| `050310` | Xalqçalğ ı tlə ri ifaç ılığ ı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı ı ı
  - nə ti
  - Populyar musiqi və caz ifaç ılığ ı
- ** `060305` Dirijorluq**
  - ğ u, xalqçalğ ı ri orkestrinin dirijorluğ u)
  - stə karlıq
  - stə karl q

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 12 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050308` | İnstrumental ifaç ılıq rüzrə ) |
| `050310` | Xalqçalğ ı tlə ri ifaç ılığ ı tiüzrə ) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060304` Solooxuma**
  - Aşı nə ti
- ** `060305` Dirijorluq**
  - ğ u, xalqçalğ ı ri orkestrinin dirijorluğ u)
  - stə karlıq
  - stə karlıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Dirijorluq (xor dirijoru, opera- simfonik orkestr dirijoru, nəfəs alətləri orkestri dirijoru) | 42.5 | 42.5 |
| Azərbaycan Milli Konservatoriyası | Dirijorluq (xalq çalğı alətləri orkestri dirijoru, xor dirijoru) | 43.5 | 30 |
| Bakı Musiqi Akademiyası | Bəstəkarlıq (akademik bəstəkarlıq, audiovizual və teatr musiqisi) | 46.5 | 30 |
| Azərbaycan Milli Konservatoriyası | Akademik bəstəkarlıq | 32 | 30 |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050317` | Vokal lər üzrə ) |
| `050304` | Solooxuma |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060304` Solooxuma**
  - ndə lik
  - Vokal ifaç ılığ ı(milli)
  - Vokal ifaç ılığ ı(akademik)
  - Aşı nə ti
  - nə ti

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Vokal | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Vokal | 41.5 | 41.5 |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| *... və daha 9 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060304` Solooxuma**
  - Aşı nə ti

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 140200` | Solooxuma (opera kamera mü ğə nnisi) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Vokal ifaç ılığ ı(akademik)
  - nə ti
  - Populyar musiqi və caz ifaç ılığ ı
- ** `060307` Musiqişünasl q**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Vokal | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Vokal | 41.5 | 41.5 |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| *... və daha 13 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `30`, Səhifə: 44)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060305` Dirijorluq**
  - rüzrə )
  - stə karlıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Dirijorluq (xor dirijoru, opera- simfonik orkestr dirijoru, nəfəs alətləri orkestri dirijoru) | 42.5 | 42.5 |
| Azərbaycan Milli Konservatoriyası | Dirijorluq (xalq çalğı alətləri orkestri dirijoru, xor dirijoru) | 43.5 | 30 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Texniki Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 52.5 | 51 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 59.5 | 46 |
| Bakı Mühəndislik Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 46 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060310` Xalqçalğ ı tlə ri ifaç ılığ ı**
  - Xalqçalğ ı tlə ri ifaç ılığ ını si və metodikası
- ** `060305` Dirijorluq**
  - rüzrə )
  - stə karlıq
  - stə karlıq
- ** `060307` Musiqişünasl q**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Musiqi Akademiyası | Dirijorluq (xor dirijoru, opera- simfonik orkestr dirijoru, nəfəs alətləri orkestri dirijoru) | 42.5 | 42.5 |
| Azərbaycan Milli Konservatoriyası | Dirijorluq (xalq çalğı alətləri orkestri dirijoru, xor dirijoru) | 43.5 | 30 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Texniki Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 52.5 | 51 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 59.5 | 46 |
| Bakı Mühəndislik Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 46 |
| *... və daha 10 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 141000` | Etnomuzikologiya |
| `HS 140500` | musiqişünaslıq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı
  - İnstrumental ifaç ılı riüzrə )
  - nə ti
  - Populyar musiqi və caz ifaç ılığ ı
- ** `060305` Dirijorluq**
  - rüzrə )
  - stə karlıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 30 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 10 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050312` | Populyar musiqi və caz ifaç ılığ ı nə ti nə ti |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nə ti
  - Populyar musiqi və caz ifaç ılığ ı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 8 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 11 (Minimal bal: `30`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050312` | Populyar musiqi və caz ifaç ılığ ı nə ti nə ti |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060303` İnstrumental ifaç ılıq**
  - İnstrumental ifaç ılı riüzrə )
- ** `060310` Xalqçalğ ı tlə ri ifaç ılığ ı**
  - Xalqçalğ tlə ri ifaç lğ riüzrə )

---

### Proqram № 69

#### Blok 1 (Minimal bal: `30`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050616` | İnformasiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060315` Rejissorluq**
  - Rejissorluq (Animasiya rejissoru)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Animasiya rejissoru | None | 30 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nə ti
  - qs, milli rə qs, baletmeyster,
  - qs mü ə llimliyi)
  - llim-tə dqiqatç

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 8 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | rüzrə ) qs müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - llim-tə dqiqatç ı
  - qs, milli rə qs, baletmeyster,
  - qs mü ə llimliyi)
- ** `060313` Teatrşünasl q**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Xoreoqrafiya Akademiyası | Milli rəqs | None | 30 |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 45)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tşünaslıq
  - riyyə si
  - nə ti
  - rüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | İqlimşünaslıq | None | 45 |
| Bakı Dövlət Universiteti | Landşaftşünaslıq | 54 | 54 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Təbiətşünaslıq fəlsəfəsi | 58.5 | 58.5 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Milli Aviasiya Akademiyası | İqlimşünaslıq | 48.5 | 48.5 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| *... və daha 81 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nə ti nə ti nə ti |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - arxivşünaslıq
  - nə ti
  - rüzrə )
  - nə ti (Dram teatrı və kino aktyoru, Musiqili teatr aktyoru)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 27 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | r və tamaşalar rejissoru |
| `HS 153600` | Teatr kollektivlİ ə ri rejissoru |
| `HS 153700` | Estrada rejissoru |
| `HS 154500` | Musiqili teatr rejissoru |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - riyyə si
- ** `060315` Rejissorluq**
  - rüzrə )
  - Rejissorluq (Televiziya rejissoru, Kino
  - rejissoru)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| Azərbaycan Milli Konservatoriyası | Musiqi tarixi və nəzəriyyəsi | 49 | 48.5 |
| *... və daha 48 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 70

#### Blok 1 (Minimal bal: `30`, Səhifə: 10)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `TE 100200` | İnformatika XTB 50106İnformasiya tətəhlükəsizliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - robototexnika mühəndisliyi
  - Süni intellekt (SABAH)
- ** `060319` Qrafika**
  - Qrafika (animasiya və kompüter qrafikası)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Süni intellekt | 73.5 | 73.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dəzgah qrafikası | 33 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Qrafika əsərlərinin bərpası | 40.5 | 30 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Qrafika (dəzgah qrafikası, kitab tərtibatı və illüstrasiyası, poster qrafikası, animasiya rəssamı) | 37 | 30 |

</details>

---

#### Blok 2 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 150800` | Rə ngkarlıq |
| `HS 155300` | Televiziya və kino rə ssamı |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060318` Rə ngkarlıq**
  - Rə ngkarlı rüzrə )
  - Rə ngkarlı zgah rə ngkarlığ ı, Rə ngkarlı rinin bə rpası və
  - ekspertizası televiziya rə ssamı riüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Rəngkarlıq əsərlərinin bərpası | None | 30 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Rəngkarlıq (dəzgah rəngkarlığı, monumental rəngkarlıq, səhnəqrafiya, audiovizual sahə üzrə rəssam, rəngkarlıq əsərlərinin bərpası) | 41 | 30 |

</details>

---

#### Blok 3 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050319` | Qrafika |
| `HS 150900` | Qrafika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060319` Qrafika**
  - rüzrə )
  - Qrafika (Kitab tə rtibatı və illüstrasiyası rinin bə rpası və
  - ekspertizası, Də zgah qrafikası riüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dəzgah qrafikası | 33 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Qrafika əsərlərinin bərpası | 40.5 | 30 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Qrafika (dəzgah qrafikası, kitab tərtibatı və illüstrasiyası, poster qrafikası, animasiya rəssamı) | 37 | 30 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Texniki Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 52.5 | 51 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 59.5 | 46 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 4 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 152300` | Bə dii toxuculuq |
| `HS 153800` | Xalçaç ırə ssam |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nə t
  - rüzrə )
  - ü şə ,
  - riüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Texniki Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 52.5 | 51 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 59.5 | 46 |
| Bakı Mühəndislik Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 46 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dekorativ-tətbiqi sənət (bədii xalça, bədii toxuculuq, bədii keramika və şüşə, bədii metal, dekorativ-tətbiqi sənət əsərlərinin bərpası (sahələr üzrə)) | 32 | 30 |
| Milli Aviasiya Akademiyası | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 57.5 | 40 |
| *... və daha 9 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - raşlıq
  - raşlıq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Heykəltaraşlıq (monumental heykəltaraşlıq, dəzgah heykəltaraşlığı) | 33 | 30 |

</details>

---

#### Blok 6 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 154300` | Dizayner rə ssam |
| `HS 210100` | Dizayn rə ssam |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - riyyə si
- ** `060321` Dizayn**
  - rüzrə )
  - Dizayn (Sə naye dizaynı, Qrafik dizaynı, Geyim dizaynı İnteryerüzrə
  - riüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| Azərbaycan Milli Konservatoriyası | Musiqi tarixi və nəzəriyyəsi | 49 | 48.5 |
| *... və daha 72 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `30`, Səhifə: 46)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050626` | Memarlıq |
| `050633` | Memarlıq |
| `HS 155100` | Rə ssam-memar rə ssam |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rüzrə )
  - Dizayn (Sə naye dizaynı, Qrafik dizaynı, Geyim dizaynı İnteryerüzrə
  - riüzrə )

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 51 | 51 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) İngilis dilində | 64.5 | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 58 | 43.5 |
| Azərbaycan Texniki Universiteti | Elektrik təchizatı (sahələr üzrə) | 47.5 | 40 |
| Azərbaycan Texniki Universiteti | Keyfiyyətə nəzarət və diaqnostika sistemləri (sahələr üzrə) | 49.5 | 45 |
| Azərbaycan Texniki Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 61.5 | 61.5 |
| Azərbaycan Texniki Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | None | 49 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 52.5 | 51 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Tullantıların emal texnologiyaları (sahələr üzrə) | 59.5 | 46 |
| Bakı Mühəndislik Universiteti | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 53 | 46 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dekorativ-tətbiqi sənət (bədii xalça, bədii toxuculuq, bədii keramika və şüşə, bədii metal, dekorativ-tətbiqi sənət əsərlərinin bərpası (sahələr üzrə)) | 32 | 30 |
| Milli Aviasiya Akademiyası | Texnoloji proseslərin avtomatlaşdırılması və idarə edilməsi (sahələr üzrə) | 57.5 | 40 |
| *... və daha 19 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 8 (Minimal bal: `30`, Səhifə: 51)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `T 281200` | Toxuculuq və yüngül sə naye mallarının bə dii ndirilmə si |
| `HS 210100` | Dizayn (sə naye |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060321` Dizayn**
  - rüzrə )
  - Dizayn (Geyim dizaynı, Sə naye dizaynı)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Memarlıq mühitinin dizaynı | 43.5 | 43.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnteryer dizaynı | 52 | 44.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Qrafik dizayn | 52.5 | 37 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Vizual dizayn | 52 | 30 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Texniki dizayn | None | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | Geyim dizaynı | None | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | İnteryer dizaynı | 52.5 | 30 |
| Azərbaycan Dövlət İqtisad Universiteti | Qrafik dizayn | 52.5 | 46 |
| Bakı Mühəndislik Universiteti | Memarlıq mühitinin dizaynı | 49 | 49 |
| Bakı Mühəndislik Universiteti | Sənaye dizaynı | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Geyim dizaynı | 32 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | İnteryer dizaynı | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Qrafik dizayn | None | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Sənaye dizaynı | None | 30 |
| *... və daha 28 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 71

#### Blok 1 (Minimal bal: `40`, Səhifə: 14)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050640` | Yanğ ı tətəhlükəsizliyi mühəndisliyi |
| `050650` | Yanğ ı tətəhlükəsizliyi mühəndisliyi aliyyə tinin sizliyi mühəndisliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060650` Yanğ ı sizliyi mühəndisliyi**

---

### Proqram № 72

#### Blok 1 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | texnologiyası qida mə hsullarının rman bitkilərinin saxlanılması, emalı texnologiyası və mtəəş ünaslığ ı nə n malların texnologiyasımühəndisliyi bii liflə rin istehsalı texnologiyası və avadanlıqları İr və onların ə sas nda kompozisiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nə n malların texnologiyasımühəndisliyi
  - mə mulatlarının texnologiyası
  - bii liflə rin istehsalının texnologiyası və avadanlıqları
  - Toxuculuq texnologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar | 57.5 | 57.5 |
| Bakı Mühəndislik Universiteti | Kimya mühəndisliyində yaşıl texnologiyalar İngilis dilində | 65 | 63.5 |

</details>

---

### Proqram № 74

#### Blok 1 (Minimal bal: `30`, Səhifə: 47)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 152900` | Teatr və kino aktyoru |
| `HS 153000` | Musiqili teatr aktyoru |
| `HS 153100` | Estrada aktyoru |
| `050314` | Rejissorluq |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - nə ti
  - Aktyor ifaç ılığ ını riyyə si
- ** `060313` Teatrşünaslıq**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Kimyəvi kinetika və kataliz | 64 | 64 |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər | 66 | 66 |
| Azərbaycan Texniki Universiteti | Əşyaların interneti və kiberfiziki sistemlər İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təsviri sənətin tədrisi | 63.5 | 40 |
| Azərbaycan Milli Konservatoriyası | Xanəndə sənəti | 31 | 31 |
| Azərbaycan Milli Konservatoriyası | Aşıq sənəti | 42 | 30 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Dizayn sənətinin tarixi və nəzəriyyəsi | 48.5 | 48.5 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Xanəndə sənəti | 32 | 32 |
| Azərbaycan Dövlət Mədəniyyət və İncəsənət Universiteti | Aşıq sənəti | 33.5 | 33.5 |
| Azərbaycan Dövlət Rəssamlıq Akademiyası | Dizayn sənətinin tarixi və nəzəriyyəsi | 47 | 47 |
| Bakı Xoreoqrafiya Akademiyası | Xoreoqrafiya sənətinin tarixi və nəzəriyyəsi | 53 | 35 |
| Bakı Xoreoqrafiya Akademiyası | Baletmeyster sənəti | None | 30 |
| Naxçıvan Dövlət Universiteti | Təsviri sənətin tədrisi | None | 40 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

### Proqram № 75

#### Blok 1 (Minimal bal: `50`, Səhifə: 48)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | t və ictimai tlər |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - tlə r
  - ctimai siyasə t

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya | 71 | 55 |
| Bakı Dövlət Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | 68.5 | 51.5 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti | None | 50 |
| Bakı Dövlət Universiteti | Müasir dövrdə Uzaq Şərq dövlətlərinin xarici siyasəti İngilis dilində | None | 50 |
| Azərbaycan Texniki Universiteti | Liftlər və eskalatorlar | None | 40 |
| Azərbaycan Texniki Universiteti | Nəqliyyat xidmətləri üçün böhran və risklərin idarə edilməsi | 55.5 | 50.5 |
| Azərbaycan Dövlət İqtisad Universiteti | Mülkiyyət obyektlərinin qiymətləndirilməsi | 64 | 45 |
| Azərbaycan Dövlət İqtisad Universiteti | Sosial xidmətlərin təşkili | 66 | 66 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər və diplomatiya | 72 | 54 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 57 |
| Bakı Slavyan Universiteti | Beynəlxalq münasibətlər və diplomatiya İngilis dilində | None | 50 |
| Bakı Mühəndislik Universiteti | Beynəlxalq münasibətlər və diplomatiya | None | 50 |
| Bakı Mühəndislik Universiteti | Sərnişindaşıma xidmətlərinin təşkili və təhlükəsizliyi | 43.5 | 43.5 |
| Azərbaycan Respublikası Prezidenti yanında Dövlət İdarəçilik Akademiyası | Beynəlxalq münasibətlər və diplomatiya | 72 | 72 |
| *... və daha 24 təhsil müəssisəsi* | | | |

</details>

---

### Ümumi / Digər Proqramlar

#### Blok 1 (Minimal bal: `40`, Səhifə: 13)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050706` | Meşə çilik |
| `050708` | Meşə çilik |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060649` Ekologiya mühəndisliyi**
  - torpaq mühafizə si
  - li istifadə olunması
- ** `060510` Ekologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| *... və daha 7 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 2 (Minimal bal: `45`, Səhifə: 18)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `ET 010800` | Ə traf mühitin tə bii li istifadə olunması |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - traf mühitin mühafizə metodları bə rpası
  - tin mühafizə si
  - Bioekologiya
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**
  - Ekoloji biologiya
- ** `060649` Ekologiya mühəndisliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| *... və daha 74 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 3 (Minimal bal: `40`, Səhifə: 22)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050105` | Riyaziyyat və informatika müəllimliyi |
| `050106` | Riyaziyyat müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 4 (Minimal bal: `40`, Səhifə: 23)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nformatika müəllimliyi |
| `050114` | Riyaziyyat müəllimliyi |
| `050115` | Riyaziyyat və informatika müəllimliyi |
| `050509` | Kompüter elmlə ri |
| `050511` | Riyaziyyat |
| `050501` | Riyaziyyat |
| `050105` | Riyaziyyat və informatika müəllimliyi |
| `050106` | Riyaziyyat müəllimliyi |
| `050509` | Kompüter elmlə ri |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060509` Kompüter elmlə ri**
  - informasiya tə minatı
  - dirmə
  - Tə tbiqi riyaziyyat
  - etmə nin riyazi-iqtisadiüsulları
- ** `060105` Riyaziyyat mü ə llimliyi**
  - Riyaziyyatın tə drisi metodikası və metodologiyası
- ** `060509` Kompüter elmlə ri**
  - ntellektual sistemlə r
  - rin idarə olunması
  - nformasiya sistemlə ri
  - qtisadi informasiya sistemlə ri
  - etmə nin informasiya texnologiyalar

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Riyazi modelləşdirmə | 64 | 64 |
| Bakı Dövlət Universiteti | İqtisadi-riyazi modelləşdirmə | 64 | 55 |
| Bakı Dövlət Universiteti | Təhsildə monitorinq və qiymətləndirmə | 80 | 80 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə | 66 | 66 |
| Bakı Dövlət Universiteti | Hesablama riyaziyyatı və modelləşdirmə İngilis dilində | None | 55.5 |
| Bakı Dövlət Universiteti | Stoxastik modelləşdirmə | 61 | 61 |
| Azərbaycan Texniki Universiteti | Əlvan və nadir metalların metallurgiyası | 51 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi İngilis dilində | 65.5 | 65.5 |
| Azərbaycan Texniki Universiteti | Kompüter modelləşdirməsi Türk dilində | 63.5 | 63.5 |
| Azərbaycan Texniki Universiteti | Riyazi modelləşdirmə | 62.5 | 62.5 |
| Azərbaycan Texniki Universiteti | İqtisadi-riyazi modelləşdirmə | 65.5 | 46 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsildə monitorinq və qiymətləndirmə | 68.5 | 68.5 |
| Azərbaycan Dillər Universiteti | Təhsildə monitorinq və qiymətləndirmə | 73.5 | 73.5 |
| Naxçıvan Dövlət Universiteti | Kompüter modelləşdirməsi | 55 | 55 |
| *... və daha 50 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 5 (Minimal bal: `40`, Səhifə: 23)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060631` Kompüter mühəndisliyi**
  - Dinamiki arxitekturalı lə ri
  - Kompüter texnikasını konstruksiya edilmə si
  - si sistemlə ri
  - hlükə sizliyi
  - lə ri
- ** `060632` İnformasiya texnologiyaları ri mühəndisliyi**
  - hlükə sizliyi
  - İnformasiya texnologiyaları telekommunikasiya sistemlə ri
  - informasiya sistemlə ri
  - nin avtomatlaşdırılmı sistemlə ri
  - tbiqi proqram tə minatı
  - Aerokosmik informasiya sistemlə ri
  - İqtisadi informatika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Texniki Universiteti | Biliklərin əldə edilməsi sistemləri | 67 | 67 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) | None | 40 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnformasiya sistemlərinin təhlükəsizliyi (sahələr üzrə) İngilis dilində | 75 | 51.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 56.5 | 56.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Fövqəladə hallarda texnoloji proseslərin təhlükəsizliyi | 51.5 | 48 |
| Azərbaycan Texniki Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 44 | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Kompüter və şəbəkə təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi | None | 40 |
| Azərbaycan Texniki Universiteti | Telekommunikasiya sistemlərinin informasiya təhlükəsizliyi İngilis dilində | None | 40 |
| Azərbaycan Texniki Universiteti | Sənaye idarəetmə sistemlərinin təhlükəsizliyi | None | 50.5 |
| Azərbaycan Texniki Universiteti | Sənaye müəssisələrində həyat fəaliyyətinin təhlükəsizliyi | 52.5 | 47.5 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Yol hərəkətinin təşkili və təhlükəsizliyi | 42.5 | 40 |
| Azərbaycan Dövlət İqtisad Universiteti | İdarəetmə sistemlərinin proqram təminatının təhlükəsizliyi | 75.5 | 47 |
| Azərbaycan Dövlət İqtisad Universiteti | Qida təhlükəsizliyi və risklərin idarə edilməsi | 61.5 | 61.5 |
| *... və daha 222 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 6 (Minimal bal: `40`, Səhifə: 24)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `TE 030200` | Tə tbiqi fizika |
| `TE 030300` | Nü və fizikası |
| `M 010100` | Fizika və astronomiya r və fizika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Optoelektronika
  - k enerjilə r fizikası
  - Radiasiya materialşünaslığ ı
- ** `060104` Fizika mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası
- ** `060407` Menecment**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Optoelektronika | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Yüksək enerjilər fizikası | 61 | 61 |
| Bakı Dövlət Universiteti | Radiasiya materialşünaslığı | 58.5 | 58.5 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| *... və daha 61 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 7 (Minimal bal: `40`, Səhifə: 24)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ı ı
- ** `060119` Pedaqogika**
  - si və tarixi
  - və monitorinq
  - Sosial pedaqogika

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 8 (Minimal bal: `45`, Səhifə: 25)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - traf mühitin mühafizə metodları bə rpası
  - tin mühafizə si
  - Bioekologiya
  - traf mühitin mühafizə si
- ** `060504` Kimya**
  - Ə traf mühit kimyası
  - Ekoloji kimya
  - Ekoloji kimyə vi monitorinq
- ** `060505` Biologiya**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| “Odlar Yurdu” Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| *... və daha 74 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 9 (Minimal bal: `40`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Bitkilə rin genetikası və seleksiyası
  - İnsan genetikası
  - Biotexnologiya
  - İxtiologiya
- ** `060109` Biologiya mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Gəncə Dövlət Universiteti | Genetika | 57 | 57 |
| Qərbi Kaspi Universiteti | Genetika | 60 | 60 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya | None | 45 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Sənaye ixtiologiyası (tədris Azərbaycan dilində) | 40 | 40 |

</details>

---

#### Blok 10 (Minimal bal: `40`, Səhifə: 26)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
- ** `060649` Ekologiya mühəndisliyi**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |

</details>

---

#### Blok 11 (Minimal bal: `45`, Səhifə: 29)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060510` Ekologiya**
  - traf mühitin mühafizə metodları bə rpası
  - traf mühitin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Ekologiya hüququ | None | 57 |
| Azərbaycan Tibb Universiteti | Mama-ginekologiyada tibb bacısı (qardaşı) işi | 64 | 40 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| Lənkəran Dövlət Universiteti | Baytarlıq təbabətində mamalıq- ginekologiya və süni mayalanma | None | 30 |
| Azərbaycan Kooperasiya Universiteti | Aqroekologiya (tədris Azərbaycan dilində) | None | 45 |
| Qərbi Kaspi Universiteti | Bioekologiya | None | 45 |
| “Odlar Yurdu” Universiteti | Bioekologiya | None | 45 |
| Bakı Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 61.5 | 61.5 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| Lənkəran Dövlət Universiteti | Ətraf mühitin mühafizə və bərpa metodları | 64.5 | 45 |
| Qərbi Kaspi Universiteti | Ətraf mühitin mühafizə və bərpa metodları | None | 45 |
| *... və daha 12 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 12 (Minimal bal: `40`, Səhifə: 30)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `M 010300` | Riyaziyyat və fizika |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Aktuar riyaziyyat
  - Diskret sistemlə r
  - statistik metodlarla tə hlili
- ** `060105` Riyaziyyat mü ə llimliyi**
  - Riyaziyyatın tə drisi metodikası və metodologiyası
- ** `060503` Fizika**
  - ri və riyazi fizika
  - rk cisimlə r fizikası
  - Yarımkeçiricilə r fizikası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Aktuar riyaziyyat | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Diskret sistemlər | 61 | 61 |
| Bakı Dövlət Universiteti | Riyaziyyatın tədrisi | 78.5 | 78.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Riyaziyyatın tədrisi | 62.5 | 60.5 |
| Naxçıvan Müəllimlər İnstitutu | Riyaziyyatın tədrisi | None | 42.5 |
| Gəncə Dövlət Universiteti | Riyaziyyatın tədrisi | None | 43 |
| Sumqayıt Dövlət Universiteti | Riyaziyyatın tədrisi | 73 | 53 |
| Mingəçevir Dövlət Universiteti | Riyaziyyatın tədrisi | 69 | 41 |
| Lənkəran Dövlət Universiteti | Riyaziyyatın tədrisi | 66 | 40 |
| Bakı Dövlət Universiteti | Riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Fizikanın tədrisi | 69 | 69 |
| Bakı Dövlət Universiteti | Nəzəri və riyazi fizika | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Bərk cisimlər fizikası | 64 | 64 |
| Bakı Dövlət Universiteti | Tətbiqi fizika (yarımkeçiricilər və dielektriklər fizikası) | 59.5 | 59.5 |
| Bakı Dövlət Universiteti | Tətbiqi fizika (yarımkeçiricilər və dielektriklər fizikası) İngilis dilində | 74 | 45 |
| *... və daha 18 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 13 (Minimal bal: `40`, Səhifə: 30)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Optoelektronika
  - k enerjilə r fizikası
  - Radiasiya materialşünaslığ ı
- ** `060104` Fizika mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Optoelektronika | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Yüksək enerjilər fizikası | 61 | 61 |
| Bakı Dövlət Universiteti | Radiasiya materialşünaslığı | 58.5 | 58.5 |

</details>

---

#### Blok 14 (Minimal bal: `40`, Səhifə: 30)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 15 (Minimal bal: `40`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | və çağ ırı də rki hazırlıq (qızlar rbiyə ) müəllimliyi və |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - ə çağ ırı də rki hazırlıq (qızlarüçün fiziki
  - ) mü ə llimliyi
  - ə çağ ırı də rki hazırlı nninin tə drisi metodikası və
  - metodologiyası
- ** `060119` Pedaqogika**

---

#### Blok 16 (Minimal bal: `40`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)
- ** `060107` Texnologiya mü ə llimliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 17 (Minimal bal: `45`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - kili və metodikası(SABAH)
- ** `060407` Menecment**
  - idarə olunması)
- ** `060108` Musiqi mü ə llimliyi**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 18 (Minimal bal: `45`, Səhifə: 32)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - kili və metodikası(SABAH)
- ** `060407` Menecment**
  - idarə olunması)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 19 (Minimal bal: `40`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Neft kimyası
  - Nanomateriallar kimyası
  - Kimyə vi ekspertiza
- ** `060110` Kimya mü ə llimliyi**
  - nninin tə drisi metodikasıvə metodologiyası
- ** `060510` Ekologiya**
  - traf mühitin mühafizəmetodları bə rpası
  - tin mühafizə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Neft kimyası | 67 | 67 |
| Bakı Dövlət Universiteti | Neft kimyası İngilis dilində | 64.5 | 55 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Neft-kimya sintezinin texnologiyası | 64 | 64 |
| Sumqayıt Dövlət Universiteti | Neft kimyası | 51 | 51 |
| Bakı Dövlət Universiteti | Kompozit materiallar kimyası | 61.5 | 61.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası | 64.5 | 64.5 |
| Bakı Dövlət Universiteti | Nanomateriallar kimyası İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Materiallar kimyası | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Kimyəvi ekspertiza | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Aqroekologiya | 60 | 53.5 |
| Bakı Dövlət Universiteti | Bioekologiya | 64 | 64 |
| Bakı Dövlət Universiteti | Mikologiya | 65.5 | 65.5 |
| Bakı Dövlət Universiteti | Ekologiya hüququ | None | 57 |
| Azərbaycan Tibb Universiteti | Mama-ginekologiyada tibb bacısı (qardaşı) işi | 64 | 40 |
| Gəncə Dövlət Universiteti | Mikologiya | 47 | 47 |
| *... və daha 21 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 20 (Minimal bal: `40`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050110` | Kimya və biologiya müəllimliyi |
| `050112` | Kimya və biologiya müəllimliyi |
| `M 011200` | Kimya və biologiya |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Su ehtiyatlarını kompleks istifadə si
  - torpaq mühafizə si
  - Təbii ehtiyatların qorunması tə krar emalı
  - traf mühitin mühafizəsi
  - neft sə nayesi
  - Bə rk tullantıların emalıtexnologiyası
  - li istifadə olunması
  - Aerokosmik monitorinq
  - Nəqliyyat ekologiyası
  - Ekologiya mühəndisliyi
- ** `060505` Biologiya**
  - Molekulyar biologiya

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Memarlıq və İnşaat Universiteti | Meliorasiya, rekultivasiya və torpaq mühafizəsi | 58.5 | 46.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61.5 | 61.5 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | 58.5 | 44 |
| Azərbaycan Texniki Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 58 | 56 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 65 | 45 |
| Bakı Mühəndislik Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Milli Aviasiya Akademiyası | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | 61 | 61 |
| Gəncə Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 42.5 |
| Azərbaycan Texnologiya Universiteti (Gəncə şəhəri) | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması İngilis dilində | None | 40 |
| Sumqayıt Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 44.5 |
| Mingəçevir Dövlət Universiteti | Ətraf mühitin mühafizəsi və təbii ehtiyatlardan səmərəli istifadə olunması | None | 43 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | Ətraf mühit və neft sənayesi | 59 | 59 |
| Azərbaycan Texniki Universiteti | Ətraf mühit və neft sənayesi | 58 | 55.5 |
| Milli Aviasiya Akademiyası | Aerokosmik monitorinq | 59.5 | 51.5 |
| *... və daha 18 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 21 (Minimal bal: `40`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Bitkilə rin genetikası və seleksiyası
  - İnsan genetikası
  - Biotexnologiya
  - İxtiologiya
- ** `060109` Biologiya mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Genetika | 73.5 | 73.5 |
| Bakı Dövlət Universiteti | Bitkilərin genetikası və seleksiyası | 70 | 70 |
| Gəncə Dövlət Universiteti | Genetika | 57 | 57 |
| Qərbi Kaspi Universiteti | Genetika | 60 | 60 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya | None | 45 |
| Bakı Dövlət Universiteti | Nanobiotexnologiya İngilis dilində | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Bakı Dövlət Universiteti | Bitki biotexnologiyası İngilis dilində | None | 45 |
| Naxçıvan Dövlət Universiteti | Bitki biotexnologiyası | None | 45 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Kənd təsərrüfatı bitkilərinin biotexnologiyası (tədris Azərbaycan dilində) | 44 | 44 |
| Lənkəran Dövlət Universiteti | Kənd təsərrüfatı bitkilərinin biotexnologiyası | 32 | 32 |
| Azərbaycan Dövlət Aqrar Universiteti (Gəncə şəhəri) | Sənaye ixtiologiyası (tədris Azərbaycan dilində) | 40 | 40 |

</details>

---

#### Blok 22 (Minimal bal: `45`, Səhifə: 33)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 58 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 23 (Minimal bal: `45`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | btidai sinif müəllimliyi |
| `050111` | Korreksiyaedici təlim r təhsil |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - və monitorinq
  - kili və metodikası(SABAH)
- ** `060407` Menecment**
  - idarə olunması)
  - btidai sinif mü ə llimliyi
  - drisin metodika və metodologiyası
- ** `060116` Korreksiyaedici tə lim**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 24 (Minimal bal: `45`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `M 011700` | Sosial pedaqogika |
| `M 011800` | Defektologiya |
| `M 012000` | Korreksiyaedici pedaqogika və xüsusi də r) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - və monitorinq
  - kili və metodikası(SABAH)
- ** `060407` Menecment**
  - idarə olunması)
- ** `060206` Tarix**
  - Azə rbaycanı srlə r tarixi
  - lə rinin tarixi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 155 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 25 (Minimal bal: `40`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Azə rbaycanı ə n yeni tarixi
  - nbəş ünaslığ ı tarixşünaslığ ı
  - lə ri tarixi
- ** `060111` Tarix mü ə llimliyi**
  - nninin tə drisi metodikası və metodologiyası
- ** `060119` Pedaqogika**

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Azərbaycanın yeni və ən yeni tarixi | 67 | 67 |
| Naxçıvan Dövlət Universiteti | Azərbaycanın yeni və ən yeni tarixi | 62 | 50 |
| Gəncə Dövlət Universiteti | Azərbaycanın yeni və ən yeni tarixi | 63.5 | 53 |
| Sumqayıt Dövlət Universiteti | Azərbaycanın yeni və ən yeni tarixi | None | 50 |
| “Azərbaycan” Universiteti | Azərbaycanın yeni və ən yeni tarixi | 61 | 50 |
| Bakı Dövlət Universiteti | Slavyan ölkələri tarixi | 65.5 | 65.5 |

</details>

---

#### Blok 26 (Minimal bal: `45`, Səhifə: 34)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060407` Menecment**
  - idarə olunması)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti | 67 | 67 |
| Bakı Dövlət Universiteti | Televiziya və radio yayımları menecmenti İngilis dilində | None | 50 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Dövlət Neft və Sənaye Universiteti | İstehsal və əməliyyat menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (avtomobil nəqliyyatı üzrə) | 55.5 | 55.5 |
| Azərbaycan Texniki Universiteti | Nəqliyyatda daşımalar və menecment (dəmiryol nəqliyyatı üzrə) | 57 | 50 |
| Azərbaycan Texniki Universiteti | Strateji menecment | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti | None | 55.5 |
| Azərbaycan Texniki Universiteti | İnnovasiya menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | Layihə menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti | None | 45 |
| Azərbaycan Texniki Universiteti | İnsan resursları menecmenti Türk dilində | None | 45 |
| Azərbaycan Texniki Universiteti | Səhiyyə menecmenti | 91.5 | 45 |
| Azərbaycan Memarlıq və İnşaat Universiteti | İnnovasiya menecmenti | None | 48.5 |
| *... və daha 88 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 27 (Minimal bal: `30`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | nə t müəllimliyi |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - rinin bə rpası və ekspertizası
  - riyyə si

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi | 69 | 69 |
| Bakı Dövlət Universiteti | Cəbr və ədədlər nəzəriyyəsi İngilis dilində | 70.5 | 70.5 |
| Bakı Dövlət Universiteti | Ehtimal nəzəriyyəsi və riyazi statistika | 66 | 66 |
| Bakı Dövlət Universiteti | Dinamik sistemlər və idarəetmə nəzəriyyəsi | 60.5 | 60.5 |
| Bakı Dövlət Universiteti | Ədəbiyyat nəzəriyyəsi, ədəbi təhlil və tənqid | 67 | 57 |
| Bakı Dövlət Universiteti | Jurnalistika nəzəriyyəsi və təcrübəsi | 66 | 66 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Azərbaycan Dillər Universiteti | Beynəlxalq münasibətlər tarixi və nəzəriyyəsi | None | 50 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Bakı Mühəndislik Universiteti | Qurğular nəzəriyyəsi | 57 | 57 |
| Bakı Musiqi Akademiyası | Musiqi tarixi və nəzəriyyəsi | 50 | 50 |
| Azərbaycan Milli Konservatoriyası | Musiqi tarixi və nəzəriyyəsi | 49 | 48.5 |
| *... və daha 25 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 28 (Minimal bal: `40`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)
  - də biyyatımü ə llimliyi

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 29 (Minimal bal: `50`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyatımüəllimliyi |
| `050205` | Filologiya (Azərbaycan ədəbiyyatı) AzəAzərbaycan dili və ədəbiyyatımüəllimliyi |
| `050201` | Filologiya (AzəAzəAzərbaycan dili ədəbiyyatı) |
| `HS 020100` | Filologiya (Azərbaycan |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - biyyatşünaslıq (türk xalqlarını dəbiyyatı)
  - biyyatşünaslıq (Asiya xalqları dəbiyyatı)
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslıq (Yaxı Ortaşə rq)
  - biyyatşünaslıq
  - dəbiyyatı
  - Azə rbaycan dili
  - Dilşünasl q (müqayisə li dilçilik)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı üzrə) | None | 61.5 |
| Bakı Avrasiya Universiteti | Ədəbiyyatşünaslıq (türk xalqları ədəbiyyatı) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | 68.5 | 68.5 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (fars ədəbiyyatı üzrə) | None | 50 |
| Bakı Dövlət Universiteti | Ədəbiyyatşünaslıq (türk ədəbiyyatı üzrə) | None | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | 65 | 50 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (fransız ədəbiyyatı) | None | 50 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (Amerika ədəbiyyatı) | None | 50 |
| “Azərbaycan” Universiteti | Ədəbiyyatşünaslıq (ingilis ədəbiyyatı) | None | 50 |
| Bakı Avrasiya Universiteti | Ədəbiyyatşünaslıq (Avropa ədəbiyyatı) | None | 50 |
| Bakı Avrasiya Universiteti | Ədəbiyyatşünaslıq (dünya ədəbiyyatı üzrə) | None | 50 |
| *... və daha 141 təhsil müəssisəsi* | | | |

</details>

---

#### Blok 30 (Minimal bal: `40`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| - | Göstərilməyib |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 31 (Minimal bal: `40`, Səhifə: 35)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyatı) ədəbiyyat ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikas (SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 32 (Minimal bal: `40`, Səhifə: 36)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050103` | Xarici dil müəllimliyi (fars dili) ədəbiyyat ədəbiyyatı) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 33 (Minimal bal: `50`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `HS 020400` | Xarici dil (ibri dili) ədəbiyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslıq (xariciölkə xalqlarını dəbiyyatı dəbiyyatı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 34 (Minimal bal: `40`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | llimliyi (ingilis dili və ədəbiyyatı) |
| `050121` | Xarici dil müəllimliyi (ingilis dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Dilşünaslıq (ingilis dili)
  - Dilşünaslıq (latın dili)
  - biyyat mü ə llimliyi
  - dəbiyyatın tə drisi metodikası və metodologiyası(ingilis dili və

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Dilşünaslıq (ingilis dili üzrə) | 68.5 | 68.5 |
| Azərbaycan Dillər Universiteti | Dilşünaslıq (ingilis dili üzrə) | 64.5 | 50 |
| Naxçıvan Dövlət Universiteti | Dilşünaslıq (ingilis dili üzrə) | 75.5 | 50 |
| “Azərbaycan” Universiteti | Dilşünaslıq (ingilis dili) | None | 50 |
| Qərbi Kaspi Universiteti | Dilşünaslıq (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Dilşünaslıq (ingilis dili) İngilis dilində | 64.5 | 50 |
| Bakı Avrasiya Universiteti | Dilşünaslıq (ingilis dili) | None | 50 |

</details>

---

#### Blok 35 (Minimal bal: `40`, Səhifə: 37)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `050201` | Filologiya (ispan dili və ədəbiyyatı) ədəbiyyat |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 36 (Minimal bal: `40`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat ədəbiyyatı, eksperiment) |
| `HS 020400` | Xarici dil (alman dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 37 (Minimal bal: `40`, Səhifə: 38)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | ədəbiyyat (fransı ədəbiyyatı, filyer) |
| `HS 020400` | Xarici dil (fransız dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - si və tarixi
  - Sosial pedaqogika
  - və monitorinq
  - kili və metodikası(SABAH)

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 74 | 74 |
| Bakı Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | 78.5 | 61.5 |
| Azərbaycan Dövlət Pedaqoji Universiteti | Təhsil nəzəriyyəsi və tarixi | 64 | 64 |
| Azərbaycan Dillər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67.5 | 67.5 |
| Bakı Slavyan Universiteti | Təhsil nəzəriyyəsi və tarixi | 62.5 | 62.5 |
| Naxçıvan Dövlət Universiteti | Hüquq nəzəriyyəsi və tarixi | None | 50 |
| Naxçıvan Müəllimlər İnstitutu | Təhsil nəzəriyyəsi və tarixi | None | 44 |
| Gəncə Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 47 |
| Sumqayıt Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | 62 | 51.5 |
| Lənkəran Dövlət Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 43.5 |
| Xəzər Universiteti | Təhsil nəzəriyyəsi və tarixi | 67 | 67 |
| Bakı Qızlar Universiteti | Təhsil nəzəriyyəsi və tarixi | None | 45 |

</details>

---

#### Blok 38 (Minimal bal: `50`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (ingilis dili) rcümə (ingilis dili) |
| `HS 040100` | Linqvistika rcümə (ingilis |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Ardıcı rbaycan dili-ingilis diliüzrə )
- ** `060201` Filologiya**
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslı dəbiyyatı)
  - biyyatşünaslıq (xariciölkə xalqlarını dəbiyyatı dəbiyyatı

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (alman ədəbiyyatı) | None | 55 |
| Azərbaycan Dillər Universiteti | Ədəbiyyatşünaslıq (ispan ədəbiyyatı) | None | 50 |
| Bakı Slavyan Universiteti | Ədəbiyyatşünaslıq (rus ədəbiyyatı) | None | 50 |

</details>

---

#### Blok 39 (Minimal bal: `40`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | dili) rcümə (ingilis dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** Magistratura ixtisaslaşması**
  - Dilşünaslıq (ingilis dili)
  - Dilşünaslıq (latın dili)
  - biyyat mü ə llimliyi
  - dəbiyyatın tə drisi metodikası və metodologiyası(ingilis dili və

<details><summary>Təhsil Müəssisələri və Keçid Balları (Universitetlər)</summary>

| Universitet | İxtisaslaşma | Ödənişsiz Bal | Ödənişli Bal |
| :--- | :--- | :--- | :--- |
| Bakı Dövlət Universiteti | Dilşünaslıq (ingilis dili üzrə) | 68.5 | 68.5 |
| Azərbaycan Dillər Universiteti | Dilşünaslıq (ingilis dili üzrə) | 64.5 | 50 |
| Naxçıvan Dövlət Universiteti | Dilşünaslıq (ingilis dili üzrə) | 75.5 | 50 |
| “Azərbaycan” Universiteti | Dilşünaslıq (ingilis dili) | None | 50 |
| Qərbi Kaspi Universiteti | Dilşünaslıq (ingilis dili üzrə) | None | 50 |
| Xəzər Universiteti | Dilşünaslıq (ingilis dili) İngilis dilində | 64.5 | 50 |
| Bakı Avrasiya Universiteti | Dilşünaslıq (ingilis dili) | None | 50 |

</details>

---

#### Blok 40 (Minimal bal: `40`, Səhifə: 39)

**Bakalavriat səviyyəsi üzrə bitirilən ixtisaslar:**

| Kod / Şifr | Bakalavr İxtisasının Adı |
| :--- | :--- |
| `-` | Tərcümə (fransız dili) |

**Magistratura səviyyəsində seçilə bilən ixtisaslaşmalar:**

- ** `060103` Xarici dil mü ə llimliyi**
  - Xarici dilin tə drisi metodikas və metodologiyas (frans z dili)

---
