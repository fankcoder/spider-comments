##ios游戏评论爬虫

朋友的游戏公司需要分析游戏评论，于是托我写了这个爬虫程序。

### 安装&运行
详见
amazon-spider-comments/README.md
appannie-spider-comments/README.md

### 介绍&说明
分别对amazon(亚马逊)和appannie(app安妮)上的游戏评论爬取。

#### amazon(requests + BeautifulSoup + xlwt)

同一ip地址在短时间内大量的请求amazon服务器，会强制跳转到验证码页面，经过验证码确认后才可继续正常访问

针对这个厉害的防爬虫机制，采用了简单的睡觉策略。。
```
if type(comments) == type(None):
    print "try page",realpage,"again..."
    time.sleep(3)
```
这个方法虽然没啥含金量但还算有用，大量请求后短暂休息几秒又可以继续爬了，看来亚马逊服务器的智商也不是很高嘛^_^

PS:其实这里更好的方法是用代理ip，不过由于手头没有好的代理ip,网上搜的代理ip质量又参差不齐，外加朋友急需，也没时间测试,就使用了偷懒办法

#### appannie(requests + xlwt + 用户登录模拟 + Ajax模拟)
并没有直接对appannie爬取，经分析找出该网站api地址，如果能直接获取数据则可以省大量精力，但访问api出现会三个大单词
```
ajax call only
```
于是程序模拟Ajax访问,在headers添加
```
'X-Requested-With':'XMLHttpRequest'
```
获取appannie数据还需要登录，以及验证csrftoken，具体方法详见代码
 
#### ------update------
修改了amazon的爬虫，改为多进程爬取，详见代码
amazon-spider-comments/multiplePull.py
