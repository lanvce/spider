import requests

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
     'Chrome/75.0.3770.142 Safari/537.36'

headers = {
    'User-Agent': ua
    #'Accept': text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    #'Accept-Encoding': gzip, deflate, br
    #'Accept-Language': zh-CN,zh;q=0.9,en;q=0.8
    #'Cache-Control': max-age=0
    #'Connection': 'keep-alive'
    #'Cookie': fvlid=15673392426551GLwzfGdFQ; sessionid=77FF0F2E-D9B8-4C3D-B6D6-2FC036E040E8%7C%7C2019-09-01+20%3A00%3A44.661%7C%7Cwww.baidu.com; autoid=a2a43099f0b250aa04ca9b5ccd21debe; area=610113; ahpau=1; __ah_uuid_ng=c_77FF0F2E-D9B8-4C3D-B6D6-2FC036E040E8; sessionuid=77FF0F2E-D9B8-4C3D-B6D6-2FC036E040E8%7C%7C2019-09-01+20%3A00%3A44.661%7C%7Cwww.baidu.com; sessionip=111.20.192.214; sessionvid=551BC7D1-7B58-4C4E-B0D0-BFDF2F2FD210; pvidchain=102410,102410; ahpvno=17; ref=www.baidu.com%7C0%7C0%7C0%7C2019-09-02+14%3A08%3A57.853%7C2019-09-01+20%3A00%3A44.661
    #'Host'=club.autohome.com.cn
    #'Upgrade':''-Insecure-Requests: 1

}

r=requests.get('https://club.autohome.com.cn/bbs/thread/0682da758120fbb8/82601920-1.html',headers=headers).text
print(r)