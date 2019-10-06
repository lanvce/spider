import urllib.request
import json
#urlopen接受一个字符串为参数
r=urllib.request.urlopen('http://httpbin.org/get')
#读取response内容
text=r.read()
print(text)
#打印状态码，message
print(r.status,r.reason)


#返回内容为json，load函数读取
obj=json.loads(text)
print(obj)
#r.headers是一个HttpMessage对象
for k,v in r.headers._headers:
    print('%s：%s'%(k,v))

ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
   'AppleWebKit/537.36 (KHTML, like Gecko)' \
   ' Chrome/75.0.3770.142 Safari/537.36'

req=urllib.request.Request('http://httpbin.org/user-agent')
req.add_header("User-Agent",ua)
#接受一个urllib.request.Request对象为参数
r=urllib.request.urlopen(req)
resp=json.load(r)
print("user-agent:",resp["user-agent"])




# auth_handler=urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='httpbin auth',
#                           uri='/basic-auth/mzs/12345',
#                           user='mzs',
#                           passwd='12345'
#                                )
# opener=urllib.request.build_opener(auth_handler)
# urllib.request.install_opener(opener)
# r=urllib.request.urlopen("http://httpbin.org")



#使用get参数
params=urllib.parse.urlencode({'spam':1,'eggs':2,'bacon':3})
url='http://httpbin.org/get?%s'%params
with urllib.request.urlopen(url) as f:
     print(json.load(f))


#使用post方法
data=urllib.parse.urlencode({'name':'mzs','age':30})
data=data.encode()
with urllib.request.urlopen("http://httpbin.org/post",data) as f :
    print(json.load(f))

#使用代理ip请求远程url
proxy_hangler=urllib.request.ProxyHandler({'http':'http://mzs.com:41801'})
#proxy_auth_handler=urllib.request.ProxyBasicAuthHandler() 用于要登录的代理ip
opener=urllib.request.build_opener(proxy_hangler)
r=opener.open('http://httpbin.org/ip')
print(r.read())


#urlparse模块
urllib.parse.urlparse