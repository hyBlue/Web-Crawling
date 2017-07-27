import requests

request = requests.get('https://www.naver.com')
print(request.text)