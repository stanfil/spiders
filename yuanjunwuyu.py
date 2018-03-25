import requests
import re
import os

homepage = 'http://comic.kukudm.com/comiclist/2036/index.htm'

# indexpage = '(http://comic3.kukudm.com/comiclist/2036/*?/)1.htm'
res = requests.get(homepage)
res.encoding = 'gbk'
res = res.text
pages = re.findall(r'(http://comic3.kukudm.com/comiclist/2036/\d*?/)1.htm', res)
titles = re.findall(r"href='/comiclist/2036/\d*?/\d\.htm' target='_blank'>(源君物语.*?)</A>", res)
c = 0
for hua in pages:
    if c < 120:
        print(c)
        c += 1;
        continue
    if not os.path.isdir(titles[c]):
        os.mkdir(titles[c])
    print(titles[c])
    url = hua + '1.htm'
    res = requests.get(url)
    res.encoding = 'gbk'
    cnt = re.findall(r'共(\d*?)页',res.text)
    if cnt:
        cnt = cnt[0]
    else:
        continue
    for i in range(int(cnt)):
        url = hua + str(i+1) +'.htm'
        text = requests.get(url)
        text.encoding = 'gbk'
        text = text.text
        img_url = re.findall(r"<img src='(.*?\.jpg)",text)
        if(img_url):
            img_url = img_url[0]
        else:
            continue
        # img = re.findall(r"<img src='"+r'\+m201304d\+"(.*?\.jpg)',text)[0]
        img_url = 'http://n.1whour.com/'+img_url[12:]
        addr = titles[c]+'/'+str(i+1)+'.jpg'
        if os.path.isfile(addr):
            print('pass')
            continue
        img = requests.get(img_url).content
        fp = open(addr, 'wb')
        fp.write(img)
        fp.close()
        print(addr)
    c += 1
