import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)


from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi(
    'qooiF2Hw0Zldn5BxjgXbscZkEtS7s4LaYDIGNNZGPq7kDF+dtzMJn+Dj/dp/lqYqz6V2EHknCp4xXzAAxGp2z0anCf+wh0XyA2tQr2DBP/LgPmYO4SX4cM8UoZ5WKESZANQ1rtJLYADPVO1tyeu4tgdB04t89/1O/w1cDnyilFU=')

with open("new_menu.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image(
        "richmenu-e44ce475794c21f111c747f837018714", "image/jpeg", f)
