import re
import urllib,urllib2
import cookielib
from bs4 import BeautifulSoup

#url = 'https://www.appannie.com'
url = 'https://www.appannie.com/account/login/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
values={'csrfmiddlewaretoken':'NlWYZJFBkhMSSuc2rjrR6AbDbp4oEbNj',
        'next':'/dashboard/home/',
        'username':'jennifer_hao@tianqiifo.com',
        'password':'tianqi123',
        'remember_user':''
}
data=urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()
print page

'''
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
            'username':'jennifer_hao@tianqiifo.com',
            'password':'tianqi123'
        })
loginUrl = 'https://www.appannie.com/account/login/?_ref=header'
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
gradeUrl = 'https://www.appannie.com/apps/ios/app/crush-letters-new-challenging/reviews/?date=2014-10-01~2014-12-31'
#result = opener.open(gradeUrl)
#print result.read()

#response = opener.open(request)
#print request.read()
'''
