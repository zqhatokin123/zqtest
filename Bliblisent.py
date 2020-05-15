import requests
import json
import time

url = 'https://oapi.dingtalk.com/robot/send?access_token=1c965502f344ee770a74099bde75c7b8a25283da185cb33f868191c900269b1a'
# 半佛，朱一旦，大骚,罗翔说刑法,毕导THU,何同学
bili_ids = ['37663924','437316738','390461123','517327498','254463269','163637592','254463269']
yesterday = time.time()-60*60*24*5  # 3天前

obj = {
    "msgtype": "text", 
    "text": {
        "content": 'B站:'+time.strftime('%Y-%m-%d',time.localtime(time.time())),
    }
}
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)



for bid in bili_ids:
    bili_url = 'https://api.bilibili.com/x/space/arc/search?mid='+bid+'&pn=1&ps=25&jsonp=jsonp'

    r = requests.get(bili_url)
    videos = r.json()['data']['list']['vlist']
    for video in videos:
        if(video['created']>yesterday):
            print(video['title'],video['description'],video['author'])
            print(video['created'])
            obj = {
                "msgtype": "link", 
                "link": {
                    "text": video['description']+'B站', 
                    "title": video['title'], 
                    "picUrl": 'http:'+video['pic'], 
                    "messageUrl": "https://www.bilibili.com/video/av%s" %(video['aid'])
                }
            }
            requests.post(url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(obj)
            )
