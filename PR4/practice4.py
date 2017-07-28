import os
from PIL import Image
import requests
image_url = ('https://ee5817f8e2e9a2e34042-3365e7f0719651e5b'
'8d0979bce83c558.ssl.cf5.rackcdn.com/python.png')
image = requests.get(image_url).content # 서버응답을 받아, 파일내용 획득
filename = os.path.basename(image_url) # URL에서 파일명 획득 -> basename 함수는  url에서 마지막 파일 이름만 return
with open(filename, 'wb') as f:
    f.write(image)
#품질 낮추기
with Image.open(filename) as f:
    f.save('python_quality_40.jpg', quality = 50) # 원래 배경이 투명색. jpg에서는 검정색으로 변환됨.
    print(f.size)
"""
from IPython.display import Image
Image(filename='python.pngd')
"""
#jpg로 바꿀때 배경색 지정하기
WHITE = (255, 255, 255) # RGB color
with Image.open('python.png') as im:
    im.save('python3.jpg', quality=80) # quality 옵션은 jpg에서만 유효
    im.save('python3_another.png')
    with Image.new('RGBA', im.size, WHITE) as canvas:
# alpha채널(투명)을 살리며, canvas 베이스에 im를 합성
        canvas_im = Image.alpha_composite(canvas, im) #canvas를 만들고 그 위에  im을 합성
        canvas_im.save('python3_bg_white.jpg')
#이미지 모드 : RGB, RGBA, CMYK

#이미지를 용량으로 줄이기
"""
resize(size, resample=0) : 가로세로 비율 무시
thumbnail(size, resample = 3) : 원본 비율 유지
"""

with Image.open('python.png') as im:
    print('current size : {}'.format(im.size))
    im.thumbnail((300, 300)) # 원본을 변경 -> 인자는 튜플 1개
    im.save('python3_thumb.png') # png format

#이미지 이어 붙이기

WHITE = (255, 255, 255)
with Image.open('python.png') as im1:
    with Image.open('python3.jpg') as im2:
    # 이미지 2개를 세로로 이어서 붙일려고 합니다.
        width = max(im1.width, im2.width)
        height = sum([im1.height, im2.height])
        size = (width, height)

        with Image.new('RGB', size, WHITE) as canvas:
            canvas.paste(im1, box=(0, 0)) # left/top 지정
            canvas.paste(im2, box=(0, im1.height)) # left/top 지정
            canvas.save('canvas.jpg')