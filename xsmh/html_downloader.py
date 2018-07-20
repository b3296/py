'''
html_downloader.py 上面爬虫流程图中的[下载器]
负责对指定的 URL 网页内容进行下载获取，这里只是简单处理了 HTTP CODE 200，实质应该依据 400、500 等分情况进行重试等机制处理。
'''
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import requests
class HtmlDownLoader(object):
	def download(self, url):
		if url is None:
		    return None
		cookie = '''ASP.NET_SessionId=brtji3ormf5zglzfuh2wst2k;__jsluid=222db9de6ac9a662618de277b296373c;signDate=2018-5-29'''  
		data={
		    'ASP.NET_SessionId':'brtji3ormf5zglzfuh2wst2k',
		    '__jsluid':'222db9de6ac9a662618de277b296373c',
		    'signDate':'2018-5-29'
		}
		postdata=urllib.parse.urlencode(data).encode('utf8')    
		header={
		    'User-Agent':'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicrodMessenger/4.5.255',
			'Cookie':cookie
		}
		response = requests.get(url,headers=header).text
		return response
		if response.getcode() != 200:
		    return None
		return response.read()



