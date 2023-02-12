
import requests

headers = {"Authorization": "Bearer qooiF2Hw0Zldn5BxjgXbscZkEtS7s4LaYDIGNNZGPq7kDF+dtzMJn+Dj/dp/lqYqz6V2EHknCp4xXzAAxGp2z0anCf+wh0XyA2tQr2DBP/LgPmYO4SX4cM8UoZ5WKESZANQ1rtJLYADPVO1tyeu4tgdB04t89/1O/w1cDnyilFU=", "Content-Type": "application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-e44ce475794c21f111c747f837018714',
                       headers=headers)

print(req.text)
