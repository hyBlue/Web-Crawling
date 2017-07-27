from bs4 import BeautifulSoup
import requests
html = '''
<ol>
<li>NEVER - 국민의 아들</li>
<li>SIGNAL - TWICE</li>
<li>LONELY - 씨스타</li>
<li>I LUV IT - PSY</li>
<li>New Face - PSY</li>
</ol>
'''
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('li'):
    print(tag.text)

# Parser 종류 : html.parser , lxml
# lxml - C 라이브러리. 유연하고 빠름

html = requests.get('http://www.melon.com/chart/index.htm').text
soup = BeautifulSoup(html, 'html.parser')
tag_list = []
artist_list = []
for tr_tag in soup.find_all('tr'):
    tag = tr_tag.find('div', class_='wrap_song_info')
    if tag:
        tag_sub_list = tag.find_all(href=lambda value: (value and 'playSong' in value))
        tag_list.extend(tag_sub_list)
        artist_sub_list = tag.find_all(href=lambda value: (value and 'goArtistDetail' in value))
        artist_list.extend(artist_sub_list)
for idx, tag in enumerate(tag_list, 1):
    print(idx, tag.text, end = ' - ')
    print(artist_list[idx].text)
"""
• CSS Selector를 통한 Tag 찾기 지원
• tag name : "tag_name"
• tag id : "#tag_id"
• tag class names : ".tag_class"
• * : 모든 Tag
• tag : 해당 모든 Tag
• Tag1 > Tag2 : Tag1 의 직계인 모든 Tag2
• Tag1 Tag2 : Tag1 의 자손인 모든 Tag2 (직계임이 요구되지 않음)
• Tag1, Tag2 : Tag1이거나 Tag2인 모든 Tag
• tag[attr] : attr속성이 정의된 모든 Tag
• tag[attr="bar"] : attr속성이 "bar"문자열과 일치하는 모든 Tag
• tag[attr*="bar"] : attr속성이 "bar"문자열과 부분 매칭되는 모든 Tag
• tag[attr^="bar"] : attr속성이 "bar"문자열로 시작하는 모든 Tag
• tag[attr$="bar"] : attr속성이 "bar"문자열로 끝나는 모든 Tag
• tag#tag_id : id가 tag_id인 모든 Tag
• tag.tag_class : 클래스명 중에 tag_class가 포함된 모든 Tag
• tag#tag_id.tag_cls1.tag_cls2
• id가 tag_id 이고, 클래스명 중에 tag_cls1와 tag_cls2가 모두 포함된 모든
Tag
• tag.tag_cls1.tag_cls2
• 클래스명 중에 tag_cls1와 tag_cls2가 모든 포함된 모든 Tag
• tag.tag_cls1 .tag_cls2
• 클래스명 중에 tag_cls1이 포함된 Tag의 자식 중에 (직계가 아니어도 OK), 클래
스명에 tag_cls2가 포함된 모든 Tag
"""
html = requests.get('http://www.melon.com/chart/index.htm').text
soup = BeautifulSoup(html, 'html.parser')
tag_list = soup.select('#chartListObj tr .wrap_song_info a[href*=playSong]')
#id가 chartListObj의 자손 중 tr인 것의 자손 중에 클래스명이 wrap_song_info인 것의
#  자손 중에 a태그 에서 href값이 playSong을 포함하는 것
for idx, tag in enumerate(tag_list, 1):
    print(idx, tag.text)


# html.paser는 닫히지 않은 태그는 처리 못함 -> lxml 사용
params = {
'q': 'EPA:BRNTB',
'startdate': 'Jan 01, 2016',
'enddate': 'Jun 02, 2016',
}
html = requests.get('https://www.google.com/finance/historical', params=params).text
soup = BeautifulSoup(html, 'lxml') #'html.parser')
for tr_tag in soup.select('#prices > table > tr'):
    row = [td_tag.text.strip() for td_tag in tr_tag.select('th, td')]
    print(row)

#연습문제 - reddit main page crawling
request_headers = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'http://news.naver.com/main/home.nhn', # 뉴스홈
}
html = requests.get('https://www.reddit.com', headers =request_headers).text
soup = BeautifulSoup(html, 'lxml')
tag_list = soup.select('#siteTable .top-matter .title a[data-event-action="title"]')
for i in tag_list:
    print(i.text)
