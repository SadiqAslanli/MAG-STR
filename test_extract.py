import requests
import re
from xml.sax.saxutils import unescape

def extract_text_from_jsonp(raw):
    # JSONP is window.pageN_callback(["...html..."])
    m = re.search(r'callback\(\[\s*"(.*)"\s*\]\)', raw, re.DOTALL)
    if not m:
        # maybe json array
        return ""
    content = m.group(1).encode('utf-8').decode('unicode_escape')
    # strip HTML tags to get text tokens
    clean = re.sub(r'<style.*?</style>', '', content, flags=re.DOTALL)
    # Extract spans or lines with positions or text
    # In scribd text layer: <span class=a ...>text</span>
    spans = re.findall(r'<span class=[^>]*>(.*?)</span>', clean)
    text_pieces = [re.sub(r'<[^>]+>', '', s).strip() for s in spans if s.strip()]
    return "\n".join(text_pieces)

urls = [
    'https://html.scribdassets.com/eoh9xur0gchwezt/pages/2-1ec82e1715.jsonp',
    'https://html.scribdassets.com/eoh9xur0gchwezt/pages/3-4596338672.jsonp',
    'https://html.scribdassets.com/eoh9xur0gchwezt/pages/4-67e805868e.jsonp',
    'https://html.scribdassets.com/eoh9xur0gchwezt/pages/5-c40328b208.jsonp'
]

for idx, u in enumerate(urls, start=2):
    r = requests.get(u)
    txt = extract_text_from_jsonp(r.text)
    print(f"=== PAGE {idx} (len {len(txt)}) ===")
    print(txt[:400])
