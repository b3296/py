# coding : utf-8
from urllib import request
from bs4 import BeautifulSoup
if __name__ == '__main__':
 	download_url = "http://www.biqukan.com/1_1094/5403177.html"
 	head = {}
 	head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
 	req = request.Request(url=download_url,headers=head)
 	response = request.urlopen(req)
 	content = response.read().decode("gbk","ignore")
 	soup_text = BeautifulSoup(content,'lxml')
 	texts = soup_text.find_all(id = 'content', class_ = 'showtxt')
 	#print(str(texts))
 	soup_text = BeautifulSoup(str(texts),'lxml')
 	print(soup_text.div.text.replace('\xa0',''))
