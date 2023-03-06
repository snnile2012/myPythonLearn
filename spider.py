import requests

url = 'https://www.baidu.com'
html = requests.get(url)
html.encoding = 'utf-8'
print(html.text)
