import requests
#import json
from Get_code_Tools import get_code
from fake_useragent import UserAgent


def get_image():
    code_url = 'http://www.yundama.com/index/captcha?'
    image=s.get(code_url)
    with open("code.jpg",'wb') as f:
        #写入的不是response 必须是content
        f.write(image.content)

    code=get_code('code.jpg')
    #print("code:",code)
    return code
   
def login(code):
    form={
        #不能用空格
        "username":"lanvce",
        "password":"mzs199847",
        "utype": '1',
        "vcode":code

    }
    login_url='http://www.yundama.com/index/login?'
    response=s.get(login_url,headers=headers,params=form)
    #print(response)
    return response



if __name__=="__main__":

    headers = {
        "User-Agent": UserAgent().chrome
    }
    s = requests.Session()
    #print(s)
    base_url='http://www.yundama.com'

    res=s.get(base_url,headers=headers)
    code=get_image()
    print("验证码是:",code)
    response=login(code)
    print(response.text)
