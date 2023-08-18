import requests
response=requests.get('https://www.python.org/dpwnloads/')
text=response.text
print(text)
