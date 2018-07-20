import requests
import json
import urllib.request
#headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1','Cookie':u'_md_ClientID=1blg0ut6859c000000; CNZZDATA1267429993=1032526601-1518314007-http%253A%252F%252Fmrksys.com%252F%7C1518314007; cn_1268153473_dplus=%7B%22distinct_id%22%3A%20%2215f9ed46649295-0d54e3eef92a15-474a0521-15f900-15f9ed4664a6b7%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201518317389%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201518317389%7D%7D; UM_distinctid=15f9ed46649295-0d54e3eef92a15-474a0521-15f900-15f9ed4664a6b7; aliyungf_tc=AQAAAKx67hpJmA4AkKvFc8q6s8NbpiXD; zcstyj_tyj=zRXW+0qLehyiwQ3uM5KK8A==; zcstyj_first=1; CNZZDATA1261687942=1972613237-1510195136-null%7C1519439238; fromsource=zt-gq-wap518; SERVERID=7fd8d7a645d89e38c54e0380bc80f4e4|1519442420|1519442168; tg=1010,180224','Referer': 'http://www.wsloan.com/m/tg/0/16-app/?s=zt-gq-wap518','Connection': 'keep-alive','Upgrade-Insecure-Requests': 1}
# headers={'Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Upgrade-Insecure-Requests': '1','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9','Cookie': '_md_ClientID=1blg0ut6859c000000; CNZZDATA1267429993=1032526601-1518314007-http%253A%252F%252Fmrksys.com%252F%7C1518314007'}
# r = requests.post('http://www.demlution.com/capi/v1/dmhome/send_token',data=json.dumps({"mobile":"13008153639","type":"signup"}),headers=headers)
# Req=urllib.request.Request(url,headers=headers)

flag = True
i = 0
while flag:
	i += 1
	headers={'Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Upgrade-Insecure-Requests': '1','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9','Cookie': '_md_ClientID=1blg0ut6859c000000; CNZZDATA1267429993=1032526601-1518314007-http%253A%252F%252Fmrksys.com%252F%7C1518314007'}
	r = requests.post('http://www.demlution.com/capi/v1/dmhome/send_token',data=json.dumps({"mobile":"13008153639","type":"signup"}),headers=headers)
	print(r.text)
	if i >10:
		flag = False