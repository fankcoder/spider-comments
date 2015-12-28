import requests

#r = requests.get('https://www.appannie.com')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = "https://www.appannie.com/dashboard/home/"
urlogin = "https://www.appannie.com/account/login/"
postdata = {
        'csrfmiddlewaretoken':'klm8fUeXX5qMjPevjoxuit5cFQP3hfaV',
        'next':'/dashboard/home/',
        'username':'jennifer_hao@tianqiifo.com',
        'password':'tianqi123',
        }
s = requests.Session()
s.post(urlogin,data=postdata,headers=headers)
response = s.get(url,headers=headers)
print response.content

