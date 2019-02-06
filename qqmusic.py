import requests
import json

mid = input('input mid：\n')
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid='+ mid +'&filename=C400'+ mid +'.m4a&guid=7349446525'
response = requests.get(url)    # 访问加密的网址
response = json.loads(response.text)
vkey = response['data']['items'][0]['vkey'] # 加密的参数
music_url = 'http://dl.stream.qqmusic.qq.com/C400'+ mid +'.m4a?vkey='+ vkey +'&guid=7349446525&uin=0&fromtag=66'
headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
response = requests.get(url=music_url, headers=headers, stream=True)
with open(mid +'.m4a', 'wb') as f:
    for chunk in response.iter_content(1024):
        f.write(chunk)
print(mid +'download complete\n')
