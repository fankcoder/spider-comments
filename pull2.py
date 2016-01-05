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
                'Content-Type':'application/x-www-form-urlencoded',
                }

    urlogin = "https://www.appannie.com/account/login/"
    s  = requests.Session()
    s.get(urlogin,headers=headers)
    csrftoken = s.cookies['csrftoken']
    postdata = {
            'csrfmiddlewaretoken':csrftoken,
            'next':'/dashboard/home/',
            'username':'jennifer_hao@info.com',
            'password':'123',
            }

    s.headers=headers
    login_response = s.post(url=urlogin,data=postdata)
    if not 200 <= login_response.status_code < 300:
        raise Exception("Error while logging in, code: %d" % (response. status_code))
    else:
        print "login success..."
    r = s.get(url=url,headers=headers)
    if not 200 <= r.status_code < 300:
        raise Exception("Error while download website, code:%d" % (r.status_code))
    else:
        return r.content

def matchRe(content):
    _version='''<span ng-cell-text="" class="ng-binding">(.*?)</span>'''
    title = """<h2 class="asset-name" js-expandable >.*?</h2>"""
    pattern = re.compile(title)
    test = pattern.findall(content)
    print test

    system = 'ios'
    version = ''
    rate = ''
    rtitle = ''
    tauthor = ''
    rtext = ''
    tanslate = ''
    date = ''
    country = ''
    commentDict = {}
    return commentDict

def saveToExcel():
    pass

def savefile(content):
    f = open('index.html','wb')
    f.write(content)
    f.close()

if __name__ == '__main__':
    indexUrl = "https://www.appannie.com"
    commentUrl = ("https://www.appannie.com/apps/ios/app/"
    "hi-words-a-new-word-search-puzzle-game/reviews/?date=2015-01-01~2015-12-31")
    content = loginWeb(commentUrl)
    commentDate = matchRe(content)
    #saveToExcel(commentDate)
    savefile(content)
