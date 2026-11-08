import requests

url = 'https://html.scribdassets.com/eoh9xur0gchwezt/pages/1-6d4dba2526.jsonp'
r = requests.get(url)
print('Status:', r.status_code)
print('Len:', len(r.text))
print('Snippet:', r.text[:1000])
