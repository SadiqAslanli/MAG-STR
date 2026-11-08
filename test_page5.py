import requests
import re
import json

u = 'https://html.scribdassets.com/eoh9xur0gchwezt/pages/5-c40328b208.jsonp'
r = requests.get(u)
raw = r.text
prefix = 'window.page5_callback('
if raw.startswith(prefix):
    json_str = raw[len(prefix):].rstrip(');')
    data = json.loads(json_str)
    html_page = data[0]
    # Let's inspect raw text of html_page
    with open('page5.html', 'w', encoding='utf-8') as f:
        f.write(html_page)
    print('Wrote page5.html successfully!')
