'''
spider_main.py 上面爬虫流程图中的[调度器]
面向对象写法，调度器负责循环从 UrlManager 获取爬取链接，然后交给 HtmlDownLoader 下载，然后把下载内容交给 HtmlParser 解析，然后把有价值数据输出给 HtmlOutput 进行应用。
'''
import url_manager
import html_downloader
import html_parser
import html_output
import time
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import orm
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.out_put = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        while True:
            try:
                if count == 1:
                    url = rootUrl
                    name = '目录'
                else:    
                    url = "http://y89.fanmugua.net/Home/Detail?novelId=64&novelTitleNo="+ str(count) + '&referralId='
                    name = count
                print("craw %d : %s" % (count, url))
                html_content = self.downloader.download(url)
                soup = BeautifulSoup(html_content, "html.parser", from_encoding='utf-8')
                #titleTag = soup.select('div[class="col title"]')
                #title= titleTag[0].string
                print(soup)
                with open("./html/%s.html" % name, "w",encoding="utf-8") as f_out: 
                    f_out.write(html_content) 
                if count >= 1:
                    break
                count = count + 1
            except Exception as e:
                print("craw failed!\n"+str(e))

if __name__ == "__main__":
    rootUrl = "http://y89.fanmugua.net/Home/NovelIndex?NovelId=64"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)



