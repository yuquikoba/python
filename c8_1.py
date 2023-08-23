import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url='https://blog.python.org/'
req=urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
		body=str(res.read())

if 'security' in body or 'vulnerability' in body:
		print('セキュリテイに関する記述があります')
		print('https://blog.python.org/を確認してください')
else:
		print('調査対象のセキュリティ用語はありませんでした')
