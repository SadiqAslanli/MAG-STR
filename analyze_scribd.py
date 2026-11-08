import re
import json

with open('scribd_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Length of html:', len(html))

# Look for page contents or text nodes or json blobs
page_count = re.findall(r'"page_count":\s*(\d+)', html)
print('Page count matches:', page_count)

# Check for text in html
texts = re.findall(r'<span class="a\s+[^"]*">(.*?)</span>', html)
print('Span matches count:', len(texts))

# Check for text layer or paragraphs
div_texts = re.findall(r'<div class="text_layer[^"]*">(.*?)</div>', html, re.DOTALL)
print('Text layer matches count:', len(div_texts))

# Check script json tags
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print('Script tags count:', len(scripts))

for i, s in enumerate(scripts):
    if 'pageParams' in s or 'documentContent' in s or 'jsonp' in s or 'page_' in s or 'archive' in s:
        print(f'Script {i} contains keywords, len: {len(s)}')

# Check for asset urls like html.scribdassets.com
asset_urls = re.findall(r'https?://[^\s"\'<>]+\.jsonp[^\s"\'<>]*', html)
print('Asset jsonp urls:', len(asset_urls), asset_urls[:5])

asset_urls_gen = re.findall(r'https?://html\.scribdassets\.com/[^\s"\'<>]+', html)
print('html.scribdassets urls:', len(asset_urls_gen), set(asset_urls_gen[:10]))
