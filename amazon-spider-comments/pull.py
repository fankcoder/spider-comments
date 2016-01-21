# -*- coding:utf-8 -*-
import requests
import re
import json
from bs4 import BeautifulSoup

def downWeb(url):
    #referer = "https://www.appannie.com/account/login/?_ref=header"
    user_agent = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0")
    headers = {"User-Agent":user_agent,
                #"Referer":referer,
                #"Host":"www.appannie.com",
                #'Connection':'keep-alive',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                #'Accept-Encoding':'gzip, deflate, sdch',
                #'Accept-Language':'zh-CN,zh;q=0.8',
                #'X-NewRelic-ID':'VwcPUFJXGwEBUlJSDgc=',
                #'X-Requested-With':'XMLHttpRequest',
                }
    r = requests.get(url,headers=headers)
    return r.content

def matchRe(content):
    system = 'amazon'
    rate = []
    title = []
    author = []
    text = []
    tanslate = ""
    date = []
    
    soup = BeautifulSoup(content)
    comments = soup.find(id="cm_cr-review_list")
    comment = comments.find_all("div","a-section review")
    for each in comment:
        rate.append(each.i.span.get_text().split()[0])
        title.append(each.find_all("a", class_="review-title")[0].get_text().encode('utf-8'))
        author.append(each.find_all("a", class_="author")[0].get_text().encode('utf-8'))
        text.append(each.find_all("span", class_="review-text")[0].get_text().encode('utf-8'))
        date.append(each.find_all("span", class_="review-date")[0].get_text().encode('utf-8'))

    #re_rate = re.compile('''''')
    commentDict =  dict(system=system,rate=rate,
                        title=title,author=author,text=text,
                        tanslate=tanslate,date=date)
    print "comments download successful..."
    return commentDict

def saveToExcel(comment):
    system,rate,title,author,text,tanslate,date = (comment["system"],
            comment["rate"],comment["title"],comment["author"],
            comment["text"],comment["tanslate"],comment["date"])

    import xlwt

    efile = xlwt.Workbook()
    table = efile.add_sheet('Sheet1')
    table.write(0,0,u'平台')
    table.write(0,1,u'评分rate')
    table.write(0,2,u'review标题')
    table.write(0,3,u'reviewer作者')
    table.write(0,4,u'review正文')
    table.write(0,5,u'中文简单描述')
    table.write(0,6,u'时间')

    for num,each in enumerate(rate):
        index = num +1
        table.write(index,0,system)
        table.write(index,1,rate[num])
        table.write(index,2,title[num])
        table.write(index,3,author[num])
        table.write(index,4,text[num])
        table.write(index,5,tanslate)
        table.write(index,6,date[num])

    efile.save('crush.xls')
    print "save successful..."

def savefile(content):
    f = open('comments.txt','w')
    f.write(content)
    f.close()

if __name__ == '__main__':
    indexUrl = "http://www.amazon.com/Crush-Letters-Challenging-Search-Puzzle/product-reviews/B00JPVPX2A/ref=cm_cr_pr_paging_btm_next_9?ie=UTF8&amp;amp;showViewpoints=1&amp;amp;sortBy=recent&amp;amp;pageNumber=9"
    content = downWeb(indexUrl)
    comments = matchRe(content)
    savefile = saveToExcel(comments)
    #savefile(comments)
