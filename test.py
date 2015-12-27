import cookielib
filename ='hello.txt'
cookie = cookielib.MozillaCookieJar(filename)
cookie.save(ignore_discard=True, ignore_expires=True)

