import requests

#r = requests.get('https://www.appannie.com')
referer = "https://www.appannie.com/account/login/?_ref=header"
user_agent = ("Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0")
headers = {"User-Agent":user_agent,"Referer":referer}
urlindex = "https://www.appannie.com"

urlogin = "https://www.appannie.com/account/login/"
postdata = {
        #'csrfmiddlewaretoken':'klm8fUeXX5qMjPevjoxuit5cFQP3hfaV',
        #'csrftoken':'klm8fUeXX5qMjPevjoxuit5cFQP3hfaV',
        #'csrftoken':'1oTcTGnulpFQqZlu0H7uE6Ih7VUorqYc',
        'csrfmiddlewaretoken':'1oTcTGnulpFQqZlu0H7uE6Ih7VUorqYc',
        'next':'/dashboard/home/',
        'username':'jennifer_hao@tianqiinfo.com',
        'password':'tianqi123',
        }
s = requests.Session()

login_res = s.post(urlogin,data=postdata,headers=headers)

if login_res.status_code == 200:
    print "login successfully"
else:
    print login_res.status_code

response = requests.get(urlogin,headers=headers)
print response.content
'''
f = open('index.html','wb')
f.write(response.content)
f.close()
'''
