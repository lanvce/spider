import time
#图像识别模块
from PIL import Image
import pytesseract
#导入excel模块
import xlwt
from selenium import webdriver
import requests
import pymysql

global count

driver = webdriver.Chrome()
def get_main_page():

    res=driver.get('http://my.yingjiesheng.com/xuanjianghui.html')
    #res.encoding='gbk'
    #print(res.text)
    #可选行业
    time.sleep(2)


    value=input("请输入需要选择地行业序号：")
    key_word=input("请输入搜索关键字：")

    #行业选择框
    options=driver.find_elements_by_xpath('.//select/option[@value="%s"]' %value)[0]
    options.click()
    time.sleep(1)

    #关键字搜索框
    keyword=driver.find_element_by_name('word')
    keyword.send_keys(key_word)
    time.sleep(1)

    #搜索框
    submit=driver.find_element_by_name('submit')
    submit.click()
    time.sleep(2)

    page_sum=len(driver.find_element_by_xpath('.//div[@class="rows page"]').find_elements_by_tag_name('a')[2:-2])+1
    return page_sum


def parse_page(count):

    res=driver.find_elements_by_tag_name('tr')[1:]
    for item in res:


        city =item.find_elements_by_xpath('.//td')[0].text
        date=item.find_elements_by_xpath('.//td')[1].text

        #时间是图片格式 有趣 用tesseract模块识别
        time_link=item.find_elements_by_xpath('.//td')[2].find_element_by_tag_name('img').get_attribute('src')

        image=requests.get(time_link)
        with open ('one.png','wb') as f :
            f.write(image.content)
        time.sleep(2)
        realtime=pytesseract.image_to_string(Image.open('one.png'),lang='chi_sim')
        if realtime==None:
            realtime='已取消'

        company=item.find_elements_by_xpath('.//td')[3].text
        school = item.find_elements_by_xpath('.//td')[4].text
        classroom= item.find_elements_by_xpath('.//td')[5].text
        #取属性 用get_attribute
        detail=item.find_elements_by_xpath('.//td')[6].find_element_by_xpath('./a').get_attribute('href')

        # adict = {
        #     '城市':city,
        #     '日期':date,
        #     '具体时间':realtime,
        #     '公司':company,
        #     '学校':school,
        #     '教室':classroom,
        #     '详情链接':detail
        # }
        # print( adict)
        # colomn_name=['城市','日期','具体时间','公司','学校','教室','详情链接']
        # colomn_data=[city,date,realtime,company,school,classroom,detail]
        # print(colomn_data)
        # book=xlwt.Workbook()
        # sheet1=book.add_sheet('lectures',cell_overwrite_ok=False)
        # for x,y in zip(range(len(colomn_name)),colomn_name):
        #     sheet1.write(0,x,y)
        #
        #
        # print("正在存取第%s条数据。。。" %count)
        # #开始写入数据
        #
        # for i,j in zip(range(len(colomn_data)),colomn_data):
        #     sheet1.write(count,i,j)
        #
        # book.save('lectures.xls')
        #
        # count+=1


def hangye_info():
    option_list = {0:'全部行业', 25:'高校应届生专场招聘会', 18:'银行', 19:'证券、基金、保险及投资理财类', 10:'快速消费品', 24:'食品、农业、轻工类', 20:'制造、装备、电气及自动化设备', 8:'建筑、房地产、工程类', 5:'会计师事务所、财务公司',4:'化工、生物、制药、医疗、医院', 15:'石油、钢铁、电力、能源、烟草', 14:'汽车行业', 11:'零售、贸易、家具',12:'旅游、服装、餐饮、娱乐、酒店', 13:'媒体、公关、广告', 9:'交通、物流', 3:'互联网', 2:'电子、家电、电器',1:'电信、移动及通信设备', 21:'咨询公司、律所、人力资源类', 6:'计算机软件', 7:'计算机硬件', 16:'芯片、半导体',23:'高校、教育机构', 17:'研究所、国家机关、事业单位', 22:'其他'}
    #排序一下
    r=sorted(option_list.keys())
    #print(option_list)
    for i in r:
        print(i,':',option_list[i])


def get_next_page():
    next=driver.find_element_by_xpath('.//div[@class="rows page"]').find_elements_by_tag_name('a')[-2]
    tail=driver.find_element_by_xpath('.//div[@class="rows page"]').find_elements_by_tag_name('a')[-1]

    if next!=tail:
        next.click()



if __name__=="__main__":
    print("以下是行业所对应的序号：")
    hangye_info()
    count=1
    page_sum=get_main_page()
    for i in range(page_sum):
        parse_page(count)
        get_next_page()


