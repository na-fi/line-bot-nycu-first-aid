from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

line_bot_api = LineBotApi(
    'qooiF2Hw0Zldn5BxjgXbscZkEtS7s4LaYDIGNNZGPq7kDF+dtzMJn+Dj/dp/lqYqz6V2EHknCp4xXzAAxGp2z0anCf+wh0XyA2tQr2DBP/LgPmYO4SX4cM8UoZ5WKESZANQ1rtJLYADPVO1tyeu4tgdB04t89/1O/w1cDnyilFU=')


def teaching_video_first_step(event):
    msg1 = VideoSendMessage(original_content_url='https://fshuen.github.io/ym_nctu-line-bot/first_step.mp4',
                            preview_image_url='https://i.imgur.com/VfjIqO5.jpg', tracking_id='TrackId')
    msg2 = TextSendMessage(
        text='第一步驟 : 「叫」',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data="teaching_second")
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def teaching_video_second_step(event):
    msg1 = VideoSendMessage(original_content_url='https://fshuen.github.io/ym_nctu-line-bot/2.mp4',
                            preview_image_url='https://i.imgur.com/cRMSFCa.jpg', tracking_id='TrackId')
    msg2 = TextSendMessage(
        text='第二步驟 : 「叫」',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data="teaching_third")
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def teaching_video_third_step(event):
    msg1 = VideoSendMessage(original_content_url='https://fshuen.github.io/ym_nctu-line-bot/3.mp4',
                            preview_image_url='https://i.imgur.com/K1rgN7b.jpg', tracking_id='TrackId')
    msg2 = TextSendMessage(
        text='第三步驟 : 「壓」',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data="teaching_fourth")
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def teaching_video_fourth_step(event):
    msg1 = VideoSendMessage(original_content_url='https://fshuen.github.io/ym_nctu-line-bot/4.mp4',
                            preview_image_url='https://i.imgur.com/SBiuW6G.jpg', tracking_id='TrackId')
    msg2 = TextSendMessage(
        text='第四步驟 : 「電」',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="完成", data="finish")
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])
