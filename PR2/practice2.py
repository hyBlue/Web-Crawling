import requests
import json
# GET 요청 - 조회


url = 'https://www.naver.com'
response = requests.get(url)

#Get 요청 시 커스텀헤더 지정

request_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'http://news.naver.com/main/home.nhn', # 뉴스홈
}
response = requests.get('http://news.naver.com/main/main.nhn', headers=request_headers)

"""
requests 라이브러리에서의 기본 User-Agent값은 python-requests/버
전입니다. 서버에 따라 User-Agent값으로 응답 거부여부를 결정하기도
합니다.
"""

get_params = [('k1', 'v1'), ('k1', 'v3'), ('k2', 'v2')]
get_params = { 'k1' : ['v1', 'v2']}
response = requests.get('http://httpbin.org/get', params=get_params)

print(response.json())
"""
response.status_code
response.ok

status 가 200~400이면 ok
"""

print('header : ',response.headers)
# headers의 타입은 CaseInsensitiveDict : 대소문자 구분 X

#   response.encoding : response.header['Content-Type']의 charset을 반환
#   charset 이 없을 경우 iso-8859-1 반환

#response의 응답 : body

bytes_data = response.content # 응답 Raw 데이터 (bytes) ex) 이미지 데이터
str_data = response.text # response.encoding으로 디코딩하여 유니코드 변환 ex) 문자열 데이터
                         # 유니코드 변환이 안될경우 charset이 정해지지 않은것 -> 직접 해줘야됨
response.json()['args'] #json 파일


"""
한글이 깨진 것처럼 보여질 경우
.charset 정보가 없을 경우, 먼저 utf8로 디코딩을 시도하고 UnicodeDecodeError가 발생할
경우, iso-8859-1 (latin-1)로 디코딩을 수행. 이때 한글이 깨진 것처럼 보여집니다.
이때는 다음과 같이 직접 인코딩을 지정한 후에, .text에 접근해주세요.
>>> response.encoding
'iso-8859-1'
>>> response.encoding = 'euc-kr'
>>> html = response.text
혹은 .content를 직접 디코딩하실 수도 있습니다.
>>> html = response.content.decode('euckr')
"""

#POST 요청 - 수정 추가 삭제

response = requests.post('http://httpbin.org/post')
#get 인자는 param, post인자는 data 혹은 files

request_headers = {
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
    'Referer': 'http://httpbin.org',
    }
get_params = {'k1': 'v1', 'k2': 'v2'}
response = requests.post('http://httpbin.org/post',
            headers=request_headers,
            data=get_params,
            params = get_params)


print(response.text)

# JSON 인코딩

json_data = {'k1': 'v2', 'k2': [1, 2, 3], 'name': 'Ask장고'}
# json포맷 문자열로 변환한 후, data인자로 지정
json_string = json.dumps(json_data) #json을 문자열로 변환
response = requests.post('http://httpbin.org/post', data=json_string)
# 객체를 json인자로 지정하면, 내부적으로 json.dumps 처리
response = requests.post('http://httpbin.org/post', json=json_data)

# multipart/form-data 인코딩
files = {
        'photo1': open('f1.jpg', 'rb'), # 데이터만 전송
        'photo2': open('f2.jpg', 'rb'),
        'photo3': ('f3.jpg', open('f3.jpg', 'rb'), 'image/jpeg', {'Expires': '0'}),
        }
post_params = {'k1': 'v1'}
response = requests.post('http://httpbin.org/post', files=files, data=post_params)
print(response.text)