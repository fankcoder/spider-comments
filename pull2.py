import requests
import re
import json

url = "https://www.appannie.com"
urlogin = "https://www.appannie.com/account/login/"

referer = "https://www.appannie.com/account/login/?_ref=header"
user_agent = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0")

headers = {"User-Agent":user_agent,
            "Referer":referer,
            "Host":"www.appannie.com",
            'Connection':'keep-alive',
            'Content-Type':'application/x-www-form-urlencoded',
            }

response = requests.get(urlogin,headers=headers)
#print response.cookies
s  = requests.Session()
s.get(urlogin,headers=headers)
csrftoken = s.cookies['csrftoken']
print csrftoken

'''
reg = r"name='csrfmiddlewaretoken' value='(.*)' />"
pattern = re.compile(reg)
result = pattern.findall(response.content)
xsrf = result[0]
print xsrf
'''

postdata = {
        'csrfmiddlewaretoken':csrftoken,
        #'csrftoken':xsrf,
        'next':'/dashboard/home/',
        'username':'jennifer_hao@info.com',
        'password':'123',
        }

#r = requests.post(url=urlogin,data=postdata,headers=headers)
#print r.status_code
s.headers=headers
login_response = s.post(url=urlogin,data=postdata)
print login_response.status_code
#print s.headers
r= s.get(url=url,headers=headers)
print r.status_code
#print r.content

f = open('index.html','wb')
f.write(r.content)
f.close()

