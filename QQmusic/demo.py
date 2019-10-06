#https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E4%BC%A4%E5%BF%83%E5%A4%AA%E5%B9%B3%E6%B4%8B
#可以抓包 破解js 但是很难 因为有加密文件
import json
import re
import requests
from selenium import webdriver
driver=webdriver.Chrome()
url='https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E4%BC%A4%E5%BF%83%E5%A4%AA%E5%B9%B3%E6%B4%8B'
def get_url():
    driver.get(url)
    #5s内元素加载完毕 为最长等待时间 智能等待
    driver.implicitly_wait(5)
    data=driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/span[1]/a').get_attribute(
        'href'
    )
    #会报错，程序运行比歌单记载速度快
    print(data)
    data={'mid':data}
    return data

def get_music(data):
    url='http://www.douqq.com/qqmusic/qqapi.php'
    req=requests.post(url,data=data).text
    #反序列化
    req=json.loads(req)
    req=req.replace('\/\/','//').replace('\/','/')
    print(req)
    rg=re.compile('"mp3_l":"(.*?)",')
    rs=re.findall(rg,req)
    print(rs)

def go():
    data=get_url()
    get_music(data)

go()