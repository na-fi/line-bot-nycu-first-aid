from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import json

line_bot_api = LineBotApi(
    'qooiF2Hw0Zldn5BxjgXbscZkEtS7s4LaYDIGNNZGPq7kDF+dtzMJn+Dj/dp/lqYqz6V2EHknCp4xXzAAxGp2z0anCf+wh0XyA2tQr2DBP/LgPmYO4SX4cM8UoZ5WKESZANQ1rtJLYADPVO1tyeu4tgdB04t89/1O/w1cDnyilFU=')


def CPR_AED_first(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/TqtZtsc.png', preview_image_url='https://i.imgur.com/TqtZtsc.png')

    msg2 = TextSendMessage(
        text=first_1(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data="first_2")
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def CPR_AED_first_2(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/YoNKhEV.png', preview_image_url='https://i.imgur.com/YoNKhEV.png')

    msg2 = TextSendMessage(
        text=first_2(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="第二步驟", text="第二步驟")
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def first_1():
    string = '① 拍打病患並大聲喊：「你還好嗎？」'
    return string


def first_2():
    string = '② 以跪姿並朝病患左右仔細觀察有沒有正常呼吸，胸膛有沒有起伏，此步驟盡量不超過十秒⚠。\n\n📝 即使心跳還沒停止，進行CPR通常不會造成嚴重的身體危害，所以應該積極進行CPR。'
    return string


def CPR_AED_second(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/9phm7ct.png', preview_image_url='https://i.imgur.com/9phm7ct.png')

    msg2 = TextSendMessage(
        text=second_1(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="第三步驟", text="第三步驟")
                ),
            ]
        )
    )

    line_bot_api.reply_message(
        event.reply_token, [msg1, msg2])


def second_1():
    string = '① 如果身旁都沒有人，就要大喊「救命」以尋求旁人幫忙\n\n② 指定一人幫忙撥打119報案\n\n③ 指定另一人立刻將附近的AED拿過來。'
    return string


def CPR_AED_third(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/DLUQvDS.png', preview_image_url='https://i.imgur.com/DLUQvDS.png')

    # msg2 = AudioSendMessage(
    #     original_content_url='https://fshuen.github.io/ym_nctu-line-bot/20min_120bpm_compress.mp3', duration=1200000)
    msg2 = TextSendMessage(
        text=third_1(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data="third_2")
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token, [msg1, msg2])


def CPR_AED_third_2(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/KXSwlqa.png', preview_image_url='https://i.imgur.com/KXSwlqa.png')

    # msg2 = AudioSendMessage(
    #     original_content_url='https://fshuen.github.io/ym_nctu-line-bot/20min_120bpm_compress.mp3', duration=1200000)
    msg2 = TextSendMessage(
        text=third_2(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data="third_3")
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token, [msg1, msg2])


def CPR_AED_third_3(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/txP3Eub.png', preview_image_url='https://i.imgur.com/txP3Eub.png')

    msg2 = TextSendMessage(text='參考壓胸頻率👇')

    msg3 = AudioSendMessage(
        original_content_url='https://fshuen.github.io/ym_nctu-line-bot/20min_120bpm_compress.mp3', duration=1200000)
    msg4 = TextSendMessage(
        text=third_3(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="第四步驟", text="第四步驟")
                ),
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token, [msg1, msg2, msg3, msg4])


def third_1():
    string = '① 兩膝打開與肩同寬，跪在患者身側，膝蓋盡量靠近患者身體。'
    return string


def third_2():
    string = '② 將你的慣用手的手掌根，放在患者兩乳頭連線的中間。\n\n③ 另一隻手掌交疊於第一隻手的手背上。'
    return string


def third_3():
    string = '④ 手肘打直，肩膀前傾，使肩膀位於雙手的正上方。\n\n⑤ 壓的深度至少5公分\n\n⑥ 每分鐘100到120下(約每秒2下)\n\n⑦ 確保每次胸部回彈至原來厚度。'
    return string


def CPR_AED_fourth(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/5pBjcK2.png', preview_image_url='https://i.imgur.com/5pBjcK2.png')

    msg2 = TextSendMessage(
        text=fourth_1(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data='fourth_2')
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def CPR_AED_fourth_2(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/tEhe5Nn.png', preview_image_url='https://i.imgur.com/tEhe5Nn.png')

    msg2 = TextSendMessage(
        text=fourth_2(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="下一步", data='fourth_4')
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def CPR_AED_fourth_4(event):
    msg1 = ImageSendMessage(
        original_content_url='https://i.imgur.com/GCPbLWU.png', preview_image_url='https://i.imgur.com/GCPbLWU.png')

    msg2 = TextSendMessage(
        text=fourth_4(),
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="完成", data='finish')
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def fourth_1():
    string = '① 開 : 打開AED，按下開關。'
    return string


def fourth_2():
    string = '② 貼 : 依照圖示貼上貼片。\n③ 插 : 將電極插入電極插孔。'
    return string


def fourth_4():
    string = '④ 電 : AED會依據所分析的心律，用語音告訴你是否需要進行去顫電擊。'
    return string
