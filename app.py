import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import json
import AED
import CPR_AED_content
import teaching

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    'qooiF2Hw0Zldn5BxjgXbscZkEtS7s4LaYDIGNNZGPq7kDF+dtzMJn+Dj/dp/lqYqz6V2EHknCp4xXzAAxGp2z0anCf+wh0XyA2tQr2DBP/LgPmYO4SX4cM8UoZ5WKESZANQ1rtJLYADPVO1tyeu4tgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('225e7738ac10565ab2eb3545f23575c5')

# 監聽所有來自 /callback 的 Post Request


@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body

    # if(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    if msg == "119":
        call119(event)
    elif msg == "AED地圖":
        AEDgraph(event)
    elif msg == "分享":
        share(event)
    elif msg == "使用AED地圖":
        guide(event)
    elif msg == "如何使用AED地圖":
        guide(event)
    elif msg == "壓胸頻率":
        CPRfrequency(event)
    elif msg == "立刻急救":
        CPR_AED_content.CPR_AED_first(event)
    elif msg == "第二步驟":
        CPR_AED_content.CPR_AED_second(event)
    elif msg == "第三步驟":
        CPR_AED_content.CPR_AED_third(event)
    elif msg == "第四步驟":
        CPR_AED_content.CPR_AED_fourth(event)
    elif msg == "CPR+AED教學影音":
        teaching.teaching_video_first_step(event)
    else:
        profile(event)

    return 'OK2'


@handler.add(PostbackEvent)
def handle_postback(event):
    msg = event.postback.data
    if msg == '119':
        call119(event)
    elif msg == '如何使用AED地圖':
        guide(event)
    elif msg == 'share':
        share(event)
    elif msg == 'teaching_second':
        teaching.teaching_video_second_step(event)
    elif msg == 'teaching_third':
        teaching.teaching_video_third_step(event)
    elif msg == 'teaching_fourth':
        teaching.teaching_video_fourth_step(event)
    elif msg == 'finish':
        finish(event)
    elif msg == 'first_2':
        CPR_AED_content.CPR_AED_first_2(event)
    elif msg == 'third_2':
        CPR_AED_content.CPR_AED_third_2(event)
    elif msg == 'third_3':
        CPR_AED_content.CPR_AED_third_3(event)
    elif msg == 'fourth_2':
        CPR_AED_content.CPR_AED_fourth_2(event)
    elif msg == 'fourth_4':
        CPR_AED_content.CPR_AED_fourth_4(event)


@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    addr = event.message.address  # 地址
    msg = AED.make_flex_carousel(
        float(event.message.latitude), float(event.message.longitude))

    line_bot_api.reply_message(event.reply_token, msg)


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


def profile(event):
    if isinstance(event.source, SourceUser):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(
                text=profile.display_name + ' 不要亂搞'+chr(0x10001E)+chr(0x10001E)),
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Bot can't use profile API without user ID"))


def share(event):
    line_bot_api.reply_message(event.reply_token, [ImageSendMessage(original_content_url='https://i.imgur.com/K0O3ZPF.png',
                                                                    preview_image_url='https://i.imgur.com/K0O3ZPF.png'), TextSendMessage(text='請點選此連結\nhttps://line.me/R/nv/recommendOA/@059vkakz')])


def flexbyJSON(event):
    bubble_string = """
        {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "mega",
            "direction": "rtl",
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/XOU7kUz.png",
                    "flex": 1,
                    "position": "relative",
                    "margin": "0px",
                    "align": "center",
                    "gravity": "center",
                    "size": "full",
                    "aspectMode": "fit",
                    "offsetTop": "0px",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#F89D2B"
                }
                ],
                "spacing": "0px",
                "margin": "0px",
                "borderWidth": "0px",
                "justifyContent": "center",
                "alignItems": "center",
                "offsetTop": "0px",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "paddingAll": "0px",
                "cornerRadius": "none",
                "backgroundColor": "#F89D2B",
                "flex": 1
            }
            },
            {
            "type": "bubble",
            "size": "mega",
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/9qvdZb3.png",
                    "flex": 1,
                    "position": "relative",
                    "margin": "0px",
                    "align": "center",
                    "gravity": "center",
                    "size": "full",
                    "aspectMode": "fit",
                    "offsetTop": "0px",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#F89D2B"
                }
                ],
                "spacing": "0px",
                "margin": "0px",
                "borderWidth": "0px",
                "justifyContent": "center",
                "alignItems": "center",
                "offsetTop": "0px",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "paddingAll": "0px",
                "cornerRadius": "none",
                "backgroundColor": "#F89D2B",
                "flex": 1
            }
            },
            {
            "type": "bubble",
            "size": "mega",
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/lRUbSsC.png",
                    "flex": 1,
                    "position": "relative",
                    "margin": "0px",
                    "align": "center",
                    "gravity": "center",
                    "size": "full",
                    "aspectMode": "fit",
                    "offsetTop": "0px",
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#F89D2B"
                }
                ],
                "spacing": "0px",
                "margin": "0px",
                "borderWidth": "0px",
                "justifyContent": "center",
                "alignItems": "center",
                "offsetTop": "0px",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "paddingAll": "0px",
                "cornerRadius": "none",
                "backgroundColor": "#F89D2B",
                "flex": 1
            }
            }
        ]
        }
    """
    message = FlexSendMessage(
        alt_text="hello", contents=json.loads(bubble_string.encode("utf-8")))
    line_bot_api.reply_message(event.reply_token, message)


def sendQuickreply(event):
    try:
        message = TextSendMessage(
            text='請選擇',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="AED地圖", text="AED地圖")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="衛教知識", text="衛教知識")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="119", text="119")
                    ),
                    QuickReplyButton(
                        action=DatetimePickerAction(label="label3",
                                                    data="data3",
                                                    mode="date")
                    ),
                    QuickReplyButton(
                        action=CameraAction(label="label4")
                    ),
                    QuickReplyButton(
                        action=CameraRollAction(label="label5")
                    ),
                    QuickReplyButton(
                        action=LocationAction(label="label6")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='error'))


def call119(event):
    message = TemplateSendMessage(
        alt_text='確定要撥打119?',
        template=ConfirmTemplate(
            text="確定要撥打119?",
            actions=[
                URITemplateAction(
                    label="是",
                    uri='tel:119'
                ),
                MessageTemplateAction(
                    label="先不要",
                    text="我不會再亂玩了"
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def AEDgraph(event):
    message = TextSendMessage(
        text='傳送目前位置',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=PostbackAction(label="使用說明", data='如何使用AED地圖')
                ),
                QuickReplyButton(
                    action=LocationAction(label="點此傳送目前位置")
                ),

            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def guide(event):
    bubble_string = """
        {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "size": "giga",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/bT69s6t.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "gravity": "center",
                        "align": "center"
                    }
                    ],
                    "paddingAll": "0px",
                    "spacing": "lg",
                    "justifyContent": "center"
                }
                },
                {
                "type": "bubble",
                "size": "giga",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/o5rmht8.png",
                        "size": "full",
                        "aspectMode": "cover",
                        "gravity": "center",
                        "align": "center"
                    }
                    ],
                    "paddingAll": "0px",
                    "spacing": "lg",
                    "justifyContent": "center"
                }
                },
                {
                "type": "bubble",
                "size": "giga",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "size": "full",
                        "aspectMode": "cover",
                        "gravity": "center",
                        "align": "center",
                        "url": "https://i.imgur.com/6FE7XXs.png"
                    }
                    ],
                    "paddingAll": "0px",
                    "spacing": "lg",
                    "justifyContent": "center"
                }
                }
            ]
        }
    """
    msg1 = FlexSendMessage(
        alt_text="AED地圖使用說明", contents=json.loads(bubble_string.encode("utf-8")))
    msg2 = TextSendMessage(
        text='傳送目前位置',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="使用說明", text="如何使用AED地圖")
                ),
                QuickReplyButton(
                    action=LocationAction(label="點此傳送目前位置")
                ),

            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, [msg1, msg2])


def CPRfrequency(event):
    line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='參考壓胸頻率👇'), AudioSendMessage(
        original_content_url='https://fshuen.github.io/ym_nctu-line-bot/20min_120bpm_compress.mp3', duration=1200000), TextSendMessage(text='① 按壓深度至少5公分\n② 每分鐘按壓100~120次\n③ 確保每次胸部完全彈回'), TextSendMessage(text='❗ 每30次按壓後施予2次人工呼吸，每次吹氣時間超過1秒')])


def finish(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(
        text='以上資料來源:\n衛生福利部公共場所AED急救資訊網\nhttps://tw-aed.mohw.gov.tw/'))


def sendFlex(event):  # 彈性配置
    try:
        bubble = BubbleContainer(
            direction='ltr',  # 項目由左向右排列
            header=BoxComponent(  # 標題
                layout='vertical',
                contents=[
                    TextComponent(text='冰火飲料', weight='bold', size='xxl'),
                ]
            ),
            hero=ImageComponent(  # 主圖片
                url='https://i.imgur.com/3sBRh08.jpg',
                size='full',
                aspect_ratio='792:555',  # 長寬比例
                aspect_mode='cover',
            ),
            body=BoxComponent(  # 主要內容
                layout='vertical',
                contents=[
                    TextComponent(text='評價', size='md'),
                    BoxComponent(
                        layout='baseline',  # 水平排列
                        margin='md',
                        contents=[
                            IconComponent(
                                size='lg', url='https://i.imgur.com/GsWCrIx.png'),
                            TextComponent(text='25   ', size='sm',
                                          color='#999999', flex=0),
                            IconComponent(
                                size='lg', url='https://i.imgur.com/sJPhtB3.png'),
                            TextComponent(text='14', size='sm',
                                          color='#999999', flex=0),
                        ]
                    ),
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(
                                        text='營業地址:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(
                                        text='台北市信義路14號', color='#666666', size='sm', flex=5)
                                ],
                            ),
                            SeparatorComponent(color='#0000FF'),
                            BoxComponent(
                                layout='baseline',
                                contents=[
                                    TextComponent(
                                        text='營業時間:', color='#aaaaaa', size='sm', flex=2),
                                    TextComponent(
                                        text="10:00 - 23:00", color='#666666', size='sm', flex=5),
                                ],
                            ),
                        ],
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xxl',
                        contents=[
                            ButtonComponent(
                                style='primary',
                                height='sm',
                                action=URIAction(
                                    label='電話聯絡', uri='tel:0987654321'),
                            ),
                            ButtonComponent(
                                style='secondary',
                                height='sm',
                                action=URIAction(
                                    label='查看網頁', uri="http://www.e-happy.com.tw")
                            )
                        ]
                    )
                ],
            ),
            footer=BoxComponent(  # 底部版權宣告
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@ehappy studio 2019',
                                  color='#888888', size='sm', align='center'),
                ]
            ),
        )
        message = FlexSendMessage(alt_text="彈性配置範例", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


def imagemap_message(event):
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/BfTFVDN.jpg",
        alt_text='最新的合作廠商有誰呢？',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                # 家樂福
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                # 生活市集
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                # 阿瘦皮鞋
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                # 塔吉特千層蛋糕
                link_uri="https://tw.shop.com/search/%E5%A1%94%E5%90%89%E7%89%B9",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                # 亞尼克生乳捲
                link_uri="https://tw.shop.com/search/%E4%BA%9E%E5%B0%BC%E5%85%8B",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    line_bot_api.reply_message(event.reply_token, message)


def buttons_message(event):
    message = TemplateSendMessage(
        alt_text='好消息來囉～',
        template=ButtonsTemplate(
            thumbnail_image_url="https://pic2.zhimg.com/v2-de4b8114e8408d5265503c8b41f59f85_b.jpg",
            title="是否要進行抽獎活動？",
            text="輸入生日後即獲得抽獎機會",
            actions=[
                DatetimePickerTemplateAction(
                    label="請選擇生日",
                    data="input_birthday",
                    mode='date',
                    initial='1990-01-01',
                    max='2019-03-10',
                    min='1930-01-01'
                ),
                MessageTemplateAction(
                    label="看抽獎品項",
                    text="有哪些抽獎品項呢？"
                ),
                URITemplateAction(
                    label="119",
                    uri='tel:0948748474'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def Confirm_Template(event):

    message = TemplateSendMessage(
        alt_text='是否註冊成為會員？',
        template=ConfirmTemplate(
            text="是否註冊成為會員？",
            actions=[
                PostbackTemplateAction(
                    label="馬上註冊",
                    text="現在、立刻、馬上",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="查詢其他功能",
                    text="查詢其他功能"
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def Carousel_Template(event):
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


def image_carousel_message1(event):
    message = TemplateSendMessage(
        alt_text='圖片旋轉木馬',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="http://img.juimg.com/tuku/yulantu/110709/222-110F91G31375.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)


##########
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
