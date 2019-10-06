import requests



#get请求
r=requests.get('http://httpbin.org/get')
print(r.status_code,r.reason)
print(r.text)
#带参数的get
r=requests.get('http://httpbin.org/get',params={'a':'1','b':'2'})
print('带参数的get请求：',r.json())


#post请求
r=requests.post('http://httpbin.org/post',data={'a':'1','b':'2'})
print('post请求：',r.json())


#自定义headers请求

ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
   'AppleWebKit/537.36 (KHTML, like Gecko)' \
   ' Chrome/75.0.3770.142 Safari/537.36'

headers={
    'User-Agent':ua

}

r=requests.get('http://httpbin.org/headers',headers=headers)
print('自定义headers请求：',r.json())


#带cookies的请求
cookies=dict(userid='1324',token='xxxxx')
r=requests.get('http://httpbin.org/cookies',cookies=cookies)
print('带cookies的请求：',r.json())

#Basic-auth认证请求 (自己定义的用户名 密码）
r=requests.get('http://httpbin.org/basic-auth/mzs/12345',
               auth=('mzs','12345'))
print('Basic-auth认证请求：',r.json())


#返回特定状态码
bad_r=requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
#bad_r.raise_for_status()
#抛出状态码400以上的异常

#创建Session对象
import requests
s=requests.Session()
#session对象会保存服务器返回的set-cokies头信息的内容
s.get('http://httpbin.org/cookies/set/userid/1234')
s.get('http://httpbin.org/cookies/set/token/xxxxx')
#下一次请求会将本地所有的cookies信息添加到请求头信息中
r=s.get('http://httpbin.org/cookies')
print('检查session中的cookies',r.json())


#requests中使用代理
print('不使用代理：',requests.get('http://httpbin.org/ip').json())
print('使用代理：',requests.get(
    'http:httpbin.org/ip',
    proxies={'http:''http://iguye.com:41801'}
     ).json())

r=requests.get('http://httpbin.org/delay/4',timeout=5)
print(r.text)
