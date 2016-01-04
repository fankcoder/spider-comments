import requests
import re

urlogin = "https://www.appannie.com/account/login/"

referer = "https://www.appannie.com/account/login/?_ref=header"
user_agent = ("Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0")
headers = {"User-Agent":user_agent,"Referer":referer}

response = requests.get(urlogin,headers=headers)

reg = r"name='csrfmiddlewaretoken' value='(.*)' />"
pattern = re.compile(reg)
result = pattern.findall(response.content)
xsrf = result[0]

print xsrf
postdata = {
        #'csrfmiddlewaretoken':'klm8fUeXX5qMjPevjoxuit5cFQP3hfaV',
        'csrfmiddlewaretoken':xsrf,
        'next':'/dashboard/home/',
        'username':'jennifer_hao@tianqiinfo.com',
        'password':'tianqi123',
        }

r = requests.post(url=urlogin,data=postdata,headers=headers)
print r.status_code

f = open('index.html','wb')
f.write(response.content)
f.close()

