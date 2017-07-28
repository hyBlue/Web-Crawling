import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
ep_url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1093&weekday=tue'
html = requests.get(ep_url).text
soup = BeautifulSoup(html, 'html.parser')



for idx, tag in enumerate(soup.select('.wt_viewer img')):
    if idx == 0 :
        img_url = tag['src']
        img_name = os.path.basename(img_url)
        headers = {'Referer': ep_url}
        img_data = requests.get(img_url, headers=headers).content
        with open('base.jpg', 'wb') as f:
            f.write(img_data)
    else:
        img_url = tag['src']
        img_name = os.path.basename('new.jpg')
        headers = {'Referer': ep_url}
        img_data = requests.get(img_url, headers=headers).content
        with open(img_name, 'wb') as new:
            new.write(img_data)
        with Image.open('base.jpg') as base:
            with Image.open('new.jpg') as new:
                width =  max(base.width, new.width)
                height = sum([base.height, new.height])
                with Image.new('RGB', (width, height),(255,255,255) ) as canvas:
                    canvas.paste(base, box = (0,0))
                    canvas.paste(new, box = (0, base.height))
                    canvas.save('base.jpg')

