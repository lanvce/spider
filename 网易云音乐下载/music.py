from tkinter import *
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
def download():
    #https://music.163.com/playlist?id=2891076560

    header={
        'Host':'music.163.com',
        'Rcfcrcr':'https://music.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

    }
    #url=entry.get()
    url='https://music.163.com/playlist?id=2744373134'
    res=requests.get(url,headers=header).text
    #创建对象 解析网页
    r=BeautifulSoup(res,"html.parser")

    #创建id
    music_dict={}
    result=r.find('ul',{'class','f-hide'}).find_all('a')
    #print(result)
    for music in result:
        #print(music)
        music_name=music.text
        music_id=music.get('href').strip('/song?id=').replace("\""," ")

        music_dict[music_id]=music_name
    print(music_dict)

    for song_id in music_dict:
        song_url="https://music.163.com/song/media/outer/url?id=%s"%song_id
        path="D:\\pycharm\storages\spider\网易云音乐下载\songs\%s.mp3"%music_dict[song_id]
        print(song_url)

        #添加数据
        text.insert(END,"正在下载:%s"%music_dict[song_id])
        #文本框向下滚动
        text.see(END)
        text.update()
        #下载歌曲
        urlretrieve(song_url,path)
#创建窗口
root=Tk()
#标题
root.title("网易云音乐")
#窗口大小
root.geometry("550x400")
#窗口显示位置
root.geometry("+550+230")
#标签控件
label=Label(root,text="请输入要下载的歌单url:",font=('华文行楷',15))
#定位标签显示的位置
label.grid()  #默认row=0,column=0
#输入框
entry=Entry(root,font=('微软雅黑',20))
entry.grid(row=0,column=1)

#列表框控价
text=Listbox(root,font=('微软雅黑',15),width=45,height=10)
#columnspan组件跨越的列数
text.grid(row=1,columnspan=2)
#点击按钮
button=Button(root,text="开始下载",font=('微软雅黑',10),command=download)
#sticky 对齐方式
button.grid(row=2,column=0,sticky=W)
button1=Button(root,text="退出",font=('微软雅黑',10),command=root.quit) #点击触发的方法
button1.grid(row=2,column=1,sticky=E)
#显示窗口
root.mainloop()

#搭建界面
