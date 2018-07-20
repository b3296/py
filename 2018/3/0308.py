# -*- coding : utf-8 -*-
from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import json
from PIL import Image
# def fetch_data(url):
#     req = request.Request(url)
#     req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
#     with request.urlopen(req) as f:
#     	data = f.read()
#     dictdata = json.loads(data.decode('utf-8'))
#     return dictdata
# # 测试
# URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
# data = fetch_data(URL)
# print(data)
# assert data['query']['results']['channel']['location']['city'] == 'Beijing'
# print('ok')    

# class MyHTMLParser(HTMLParser):

#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self, tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)

#     def handle_data(self, data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--', data, '-->')

#     def handle_entityref(self, name):
#         print('&%s;' % name)

#     def handle_charref(self, name):
#         print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')


# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('618.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w/2, h/2))
print('Resize image to: %sx%s' % (w/2, h/2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')