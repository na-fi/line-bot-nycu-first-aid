# 圖文選單test
import requests
import json
headers = {"Authorization": "Bearer qooiF2Hw0Zldn5BxjgXbscZkEtS7s4LaYDIGNNZGPq7kDF+dtzMJn+Dj/dp/lqYqz6V2EHknCp4xXzAAxGp2z0anCf+wh0XyA2tQr2DBP/LgPmYO4SX4cM8UoZ5WKESZANQ1rtJLYADPVO1tyeu4tgdB04t89/1O/w1cDnyilFU=", "Content-Type": "application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "主選單",
    "areas": [
        {
            "bounds": {"x": 0, "y": 0, "width": 1144, "height": 489},
            "action": {"type": "message", "text": "使用AED地圖"}
        },
        {
            "bounds": {"x": 0, "y": 490, "width": 1144, "height": 490},
            "action": {"type": "message", "text": "壓胸頻率"}
        },
        {
            "bounds": {"x": 0, "y": 981, "width": 1144, "height": 498},
            "action": {"type": "message", "text": "CPR+AED教學影音"}
        },
        {
            "bounds": {"x": 0, "y": 1480, "width": 1144, "height": 206},
            "action": {"type": "message", "text": "分享"}
        },
        {
            "bounds": {"x": 1145, "y": 0, "width": 1355, "height": 845},
            "action": {"type": "message", "text": "119"}
        },
        {
            "bounds": {"x": 1145, "y": 846, "width": 1350, "height": 840},
            "action": {"type": "message", "text": "立刻急救"}
        }
    ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers, data=json.dumps(body).encode('utf-8'))

print(req.text)
# with open("https://imgur.com/HsYRHsT", 'rb') as f:
#     line_bot_api.set_rich_menu_image("richmenu-8571519ee1e7d354720ab6c0215dd75a", "image/jpg", f)
