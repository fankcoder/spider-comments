# -*- coding:utf-8 -*-
import requests
import re
import json

def loginWeb(url):
    referer = "https://www.appannie.com/account/login/?_ref=header"
    user_agent = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0")
    headers = {"User-Agent":user_agent,
                "Referer":referer,
                "Host":"www.appannie.com",
                'Connection':'keep-alive',
                #'Content-Type':'application/x-www-form-urlencoded',
                'Accept':'application/json, text/plain,*/*',
                'Accept-Encoding':'gzip, deflate, sdch',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'X-NewRelic-ID':'VwcPUFJXGwEBUlJSDgc=',
                'X-Requested-With':'XMLHttpRequest',
                #'X-CSRFToken':''
                }

    urlogin = "https://www.appannie.com/account/login/"
    s  = requests.Session()
    s.get(urlogin,headers=headers)
    csrftoken = s.cookies['csrftoken']
    postdata = {
            'csrfmiddlewaretoken':csrftoken,
            'next':'/dashboard/home/',
            'username':'f@.com',
            'password':'syqc',
            }
    
    s.headers=headers
    login_response = s.post(url=urlogin,data=postdata)
    if not 200 <= login_response.status_code < 300:
        raise Exception("Error while logging in, code: %d" % (response. status_code))
    else:
        print "login success..."
    headers["X-CSRFToken"] = csrftoken
    r = s.get(url=url,headers=headers)
    if not 200 <= r.status_code < 300:
        raise Exception("Error while download website, code:%d" % (r.status_code))
    else:
        return r.content

def matchRe(content):
    decodejson = json.loads(content)
    rowslist = decodejson["data"]["rows"]

    system = 'ios'
    version = []
    rate = []
    title = []
    author = []
    text = []
    tanslate = ""
    date = []
    country = []

    for each in rowslist:
        version.append(each["version"])
        rate.append(each["rating"])
        title.append(each["title"])
        author.append(each["author"])
        text.append(each["content"])
        date.append(each["date"])
        country.append(each["country"]["code"])

    commentDict = dict(system=system,version=version,rate=rate,
                        title=title,author=author,text=text,
                        tanslate=tanslate,date=date,country=country)
    print "create Dict done..."
    return commentDict

def saveToExcel(comment):
    system,version,rate,title,author,text,tanslate,date,country = (comment["system"],
            comment["version"],comment["rate"],comment["title"],comment["author"],
            comment["text"],comment["tanslate"],comment["date"],comment["country"])

    import xlwt

    efile = xlwt.Workbook()
    table = efile.add_sheet('Sheet1')
    table.write(0,0,u'平台')
    table.write(0,1,u'版本')
    table.write(0,2,u'评分rate')
    table.write(0,3,u'review标题')
    table.write(0,4,u'reviewer作者')
    table.write(0,5,u'review正文')
    table.write(0,6,u'中文简单描述')
    table.write(0,7,u'时间')
    table.write(0,8,u'国家')

    for num,each in enumerate(version):
        index = num +1
        table.write(index,0,system)
        table.write(index,1,version[num])
        table.write(index,2,rate[num])
        table.write(index,3,title[num])
        table.write(index,4,author[num])
        table.write(index,5,text[num])
        table.write(index,6,tanslate)
        table.write(index,7,date[num])
        table.write(index,8,country[num])

    efile.save('comments.xls')

def savefile(content):
    f = open('index.html','wb')
    f.write(content)
    f.close()

if __name__ == '__main__':
    indexUrl = "https://www.appannie.com"
    #commentUrl="https://www.appannie.com/apps/ios/app/hi-words-a-new-word-search-puzzle-game/reviews/table/?date=2015-10-12~2016-01-02&orderby=&desc=t&page=1&limit=10"
    commentUrl="https://www.appannie.com/apps/ios/app/wordfall-most-addictive-words/reviews/table/?date=2015-01-29~2015-12-21&orderby=&desc=t&page=1&limit=200"
    content = loginWeb(commentUrl)
    commentDate = matchRe(content)
    saveToExcel(commentDate)
    #savefile(content)
