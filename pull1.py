import requests

#r = requests.get('https://www.appannie.com')
referer = "https://www.appannie.com/account/login/?_ref=header"
user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/36.0.1985.143 Safari/537.36")
host = 'www.appannie.com'
headers = {"User-Agent":user_agent,"Referer":referer,"Host":host}
urlindex = "https://www.appannie.com"

urlogin = "https://www.appannie.com/account/login/"
postdata = {
        #'csrfmiddlewaretoken':'NlWYZJFBkhMSSuc2rjrR6AbDbp4oEbNj',
        'next':'/dashboard/home/',
        'username':'jennifer_hao@tianqiinfo.com',
        'password':'tianqi123',
        }
#postdata={'csrfmiddlewaretoken':'NlWYZJFBkhMSSuc2rjrR6AbDbp4oEbNj&next=%2Fdashboard%2Fhome%2F&username=jennifer_hao%40tianqiinfo.com&password=tianqi123'}
'''
csrfmiddlewaretoken:NlWYZJFBkhMSSuc2rjrR6AbDbp4oEbNj
next:/dashboard/home/
username:jennifer_hao@tianqiinfo.com
password:tianqi123
'''
s = requests.Session()
login_res = s.post(urlogin,data=postdata,headers=headers)

if login_res.status_code == 200:
    print "login successfully"
else:
    print login_res.status_code
'''
response = requests.get(urlogin,headers=headers)
print response.content

f = open('index.html','wb')
f.write(response.content)
f.close()
'''
