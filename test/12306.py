from splinter.browser import Browser
b = Browser(driver_name="chrome")
url = 'https://kyfw.12306.cn/otn/leftTicket/init'
b = Browser(driver_name="chrome")
b.visit(url)
b.find_by_text(u"登录").click()
b.fill("loginUserDTO.user_name","xxxx")
b.fill("userDTO.password","xxxx")
b.cookies.all()
{u'BIGipServerotn': u'1977155850.38945.0000',
u'JSESSIONID': u'0A01D97598F459F751C4AE8518DBFB300DA7001B67',
u'__NRF': u'95D48FC2E0E15920BFB61C7A330FF2AE',
u'_jc_save_fromDate': u'2018-02-22',
u'_jc_save_fromStation': u'%e5%b0%9a%e5%bf%97',
u'_jc_save_toStation': u'%e6%9d%ad%e5%b7%9e',
u'current_captcha_type': u'Z'}
b.cookies.add({"_jc_save_fromStation":"%e5%b0%9a%e5%bf%97"})
添加出发日期
b.cookies.add({"_jc_save_fromDate":"2018-02-22"})
添加目的地
b.cookies.add({u'_jc_save_toStation':'%e6%9d%ad%e5%b7%9e'})
b.reload()
b.find_by_text(u"查询").click()
autoSearchTime=1000