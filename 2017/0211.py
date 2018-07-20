# -*- coding: UTF-8 -*-
# from urllib import request

# if __name__ == "__main__":
# 	response = request.urlopen("http://www.fanyi.baidu.com/")	
# 	html = response.read()
# 	html = html.decode("utf-8")
# 	print(html)
# import urllib.request
# import chardet
# r=urllib.request.urlopen("http://fanyi.baidu.com")
# h=r.read()
# c=chardet.detect(h)
# hend=h.decode(c['encoding'])
# print(hend)
# print(h)
# -*- coding: UTF-8 -*-
# from urllib import request
# from urllib import parse
# import json

# if __name__ == "__main__":
#     #对应上图的Request URL
#     Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
#     #创建Form_Data字典，存储上图的Form Data
#     head={}
#     head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
#     Form_Data = {}
#     Form_Data['type'] = 'AUTO'
#     Form_Data['i'] = 'Jack'
#     Form_Data['doctype'] = 'json'
#     Form_Data['xmlVersion'] = '1.8'
#     Form_Data['keyfrom'] = 'fanyi.web'
#     Form_Data['ue'] = 'ue:UTF-8'
#     Form_Data['action'] = 'FY_BY_CLICKBUTTON'
#     #使用urlencode方法转换标准格式
#     data = parse.urlencode(Form_Data).encode('utf-8')
#     req=request.Request(Request_URL,headers=head)
#     #传递Request对象和转换完格式的数据
#     response = request.urlopen(Request_URL,data)
#     #读取信息并解码
#     html = response.read().decode('utf-8')
#     #使用JSON
#     translate_results = json.loads(html)
#     #找到翻译结果
#     #translate_results = translate_results['translateResult'][0][0]['tgt']
#     #打印翻译信息
#     print("翻译的结果是：%s" % translate_results)
from urllib import request
#访问网址
url = 'http://www.iqiyi.com'
#这是代理IP
proxy = {'http':'106.46.136.112:808'}
#创建ProxyHandler
proxy_support = request.ProxyHandler(proxy)
#创建Opener
opener = request.build_opener(proxy_support)
#添加User Angent
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
#安装OPener
request.install_opener(opener)
#使用自己安装好的Opener
response = request.urlopen(url,100)
#读取相应信息并解码
html = response.read().decode("utf-8")
#打印信息
print(html)