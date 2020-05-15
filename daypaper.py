import requests
import json
import time

url = 'https://oapi.dingtalk.com/robot/send?access_token=53a5a9db50790c5c9468170930262d6b79c8669583b996da40dae5df2b4400e3'

obj = dict(msgtype="text", text=dict(content='@所有人'+
                                             '\n实战日报: ' + time.strftime('%Y-%m-%d', time.localtime(time.time()))+
                                             '\n各位还在局点的实战同学请将每日研判案件录入到“实战运营平台”（当日研判案件均需录入）;'+
                                             '\n平台链接如下：'+
                                             '\nhttp://vcs.gts.terminus.io/project/user-arrangement'+
                                             '\n实战日报如下:'+
                                             '\nhttp://vcs.gts.terminus.io/dashboard/quickbi-report'+
                                             '\n辛苦各位同学啦！'))
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)
