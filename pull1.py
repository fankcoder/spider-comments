import requests

#r = requests.get('https://www.appannie.com')
referer = "https://www.appannie.com/account/login/?_ref=header"
user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/36.0.1985.143 Safari/537.36")
headers = {"User-Agent":user_agent,"Referer":referer}
urlindex = "https://www.appannie.com"

urlogin = "https://www.appannie.com/account/login/"
postdata = {
        'csrfmiddlewaretoken':'klm8fUeXX5qMjPevjoxuit5cFQP3hfaV',
        'next':'/dashboard/home/',
        'username':'jennifer_hao@tianqiifo.com',
        'password':'tianqi123',
        }
s = requests.Session()
login_res = s.post(urlogin,data=postdata,headers=headers)

if login_res.status_code == 200:
    print "login successfully"
else:
    pass#print login_res.text

response = login_res.get(url,headers=headers)
#response = requests.get(url,headers=headers)
print response.content

f = open('index.html','wb')
f.write(response.content)
f.close()
