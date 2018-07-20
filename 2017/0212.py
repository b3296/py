# coding : utf-8
# import urllib.request
# if __name__ == '__main__':
# 	url = "http://www.whatismyip.com.tw/"
# 	proxy = {'http':'139.224.135.94:80'}
# 	proxy_support = urllib.request.ProxyHandler(proxy)
# 	opener = urllib.request.build_opener(proxy_support)
# 	opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
# 	urllib.request.install_opener(opener) 
# 	response = urllib.request.urlopen(url)
# 	html = response.read().decode("utf-8")
# 	print(html)
# from urllib import request
# from http import cookiejar
# if __name__ == '__main__':
# 	cookie = cookiejar.CookieJar()
# 	handler = request.HTTPCookieProcessor(cookie)
# 	opener = request.build_opener(handler)
# 	response = opener.open("http://www.jobbole.com/wp-admin/admin-ajax.php")
# 	for item in cookie :
# 		print('name :',item.name)
# 		print('value :',item.value)
# 	#print(cookie)
# from urllib import request
# from http import cookiejar
# if __name__ == '__main__':
# 	filename = 'cookie.txt'
# 	cookie = cookiejar.MozillaCookieJar(filename)
# 	handler = request.HTTPCookieProcessor(cookie)
# 	opener = request.build_opener(handler)
# 	response = opener.open("http://www.baidu.com")
# 	cookie.save(ignore_discard=True, ignore_expires=True)
from urllib import request
from http import cookiejar
if __name__ == '__main__':
	filename = 'cookie.txt'
	cookie = cookiejar.MozillaCookieJar(filename)
	cookie.load(filename,ignore_discard=True,ignore_expires=True)
	handler = request.HTTPCookieProcessor(cookie)
	opener = request.build_opener(handler)
	req = request.Request("http://www.baidu.com")
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
	response = opener.open(req)
	html = response.read().decode("utf-8")
	print(html)