import pandas as pd
import numpy as np
import math
from linebot.models import *
import json

data = pd.read_csv("./AED_location.csv")
data = data.fillna("-")
# =====================================================================


def calculate(A, B):
    ra = 6378137  # radius of equator: meter
    rb = 6356755  # radius of polar: meter
    flatten = 0.003353

    radLatA = np.radians(A[0])
    radLonA = np.radians(A[1])
    radLatB = np.radians(B[0])
    radLonB = np.radians(B[1])

    pA = np.arctan(rb / ra * np.tan(radLatA))
    pB = np.arctan(rb / ra * np.tan(radLatB))

    x = np.arccos(np.multiply(np.sin(pA), np.sin(
        pB)) + np.multiply(np.multiply(np.cos(pA), np.cos(pB)), np.cos(radLonA - radLonB)))
    c1 = np.multiply((np.sin(x) - x), np.power((np.sin(pA) +
                                                np.sin(pB)), 2)) / np.power(np.cos(x / 2), 2)
    c2 = np.multiply((np.sin(x) + x), np.power((np.sin(pA) -
                                                np.sin(pB)), 2)) / np.power(np.sin(x / 2), 2)
    dr = flatten / 8 * (c1 - c2)
    distance = 0.001 * ra * (x + dr)
    return distance


# =====================================================================
def AEDLocation(lati, longi):
    target = np.array([lati, longi])
    # print(data["地點LAT", "地點LNG"])
    AED_latitude = data["地點LAT"].to_numpy()
    AED_longitude = data["地點LNG"].to_numpy()

    Dis = []
    for i in range(AED_latitude.shape[0]):
        Dis.append(
            calculate(np.array([AED_latitude[i], AED_longitude[i]]), target))

    Distance = pd.Series(Dis)
    # print(Distance.nsmallest(5).index[0])
    nearest = Distance.nsmallest(10).index
    # print(data.iloc[2][19])
    message = ""
    for i in range(10):
        message = message + data.iloc[nearest[i]][0]

        if(data.iloc[nearest[i]][9] != "-"):
            message = message + "\nAED放置地點: " + str(data.iloc[nearest[i]][9])

        if(data.iloc[nearest[i]][19] != "-"):
            message = message + "\n開放時間: " + str(data.iloc[nearest[i]][19])

        message = message + "\n距離: " + \
            str(math.floor(Distance[nearest[i]]*1000)) + "公尺\n\n"

    distance = []
    for i in range(10):
        distance.append(Distance[nearest[i]])
    return message, nearest, distance


# USAGE:
# msg, index = AEDLocation(22.99546960869026, 120.21004385692507)
# print(msg)
# print(index)

def eachLiff(string, location, address, place, tele, workday, sat, sun, PS, distance, latitude, longitude):

    if(string != ""):
        string = string + ""","""

    string += """
    {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "weight": "bold",
                "size": "22px",
                "text": " """

    string += location

    string += """ ",
                "flex": 1,
                "align": "center",
                "wrap": true,
                "adjustMode": "shrink-to-fit",
                "gravity": "center"
            },
            {
                "type": "separator"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "地址",
                        "color": "#aaaaaa",
                        "size": "md",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": " """
    string += address
    string += """ ",
                        "wrap": true,
                        "color": "#666666",
                        "size": "md",
                        "flex": 5
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "AED位置",
                        "color": "#aaaaaa",
                        "size": "md",
                        "flex": 2
                    },
                    {
                        "type": "text",
                        "text": " """
    string += place
    string += """ ",
                        "wrap": true,
                        "color": "#666666",
                        "size": "md",
                        "flex": 5
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "聯繫電話",
                        "color": "#aaaaaa",
                        "size": "md",
                        "flex": 2
                    },
                    {
                        "type": "text",
                        "text": " """
    string += tele
    string += """ ",
                        "wrap": true,
                        "color": "#666666",
                        "size": "md",
                        "flex": 5
                    }
                    ]
                }
        """

    if ((workday[0] != "-" and workday[1] != "-") or (workday[0] != "-" and workday[1] != "-") or (workday[0] != "-" and workday[1] != "-")):
        string += """
                ,
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "開放時間",
                        "color": "#aaaaaa",
                        "size": "md",
                        "flex": 2
                    },
                    {
                        "type": "text",
                        "text": " """
        if(workday[0] != "-" and workday[1] != "-"):
            string += """周一至周五\\n""" + workday[0] + \
                """ ~ """ + workday[1]

        if(sat[0] != "-" and sat[1] != "-"):
            string += """\\n""" + """周六""" + sat[0] + """ ~ """ + sat[1]

        if(sun[0] != "-" and sun[1] != "-"):
            string += """\\n""" + """周日""" + sun[0] + """ ~ """ + sun[1]

        string += """ ",
                        "wrap": true,
                        "color": "#666666",
                        "size": "md",
                        "flex": 5
                    }
                    ]
                }
        """

    if (PS != "-"):
        string += """
                ,
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "備註",
                        "color": "#aaaaaa",
                        "size": "md",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": " """
        string += PS

        string += """ ",
                        "wrap": true,
                        "color": "#666666",
                        "size": "md",
                        "flex": 5
                    }
                    ]
                }
        """

    string += """
                ,
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "距離",
                        "color": "#aaaaaa",
                        "size": "md",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": " """
    string += distance
    string += """ ",
                        "wrap": true,
                        "color": "#666666",
                        "size": "md",
                        "flex": 5
                    }
                    ]
                }
                ]
            }
            ]
        },
            "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "button",
                    "style": "primary",
                    "height": "sm",
                    "action": {
                        "type": "uri",
                        "label": "點此前往",
                        "uri": "https://www.google.com.tw/maps/dir//"""
    string += latitude + """,""" + longitude

    string += """/"
                    }
                }
            ]
            }
        }
    """
    return string


def make_flex_carousel(x, y):
    msg, nearest, distance = AEDLocation(x, y)
    finalstr = """
        {
            "type": "carousel",
            "contents": [
    """

    tmp = ""
    for i in range(10):
        # preprocessing the ducking time
        workday = [str(data.iloc[nearest[i]][13]),
                   str(data.iloc[nearest[i]][14])]
        sat = [str(data.iloc[nearest[i]][15]), str(data.iloc[nearest[i]][16])]
        sun = [str(data.iloc[nearest[i]][17]), str(data.iloc[nearest[i]][18])]

        if(workday[0] == "00:00" and workday[1] == "00:00"):
            workday[0] = workday[1] = "-"
        if(sat[0] == "00:00" and sat[1] == "00:00"):
            sat[0] = sat[1] = "-"
        if(sun[0] == "00:00" and sun[1] == "00:00"):
            sun[0] = sun[1] = "-"
        # end of preprocessing
        tmp = eachLiff(tmp, str(data.iloc[nearest[i]][0]), str(data.iloc[nearest[i]][3]), str(data.iloc[nearest[i]][9]), data.iloc[nearest[i]][20], workday, sat, sun, data.iloc[nearest[i]][19], str(
            math.floor(distance[i]*1000)) + "公尺", str(data.iloc[nearest[i]][10]), str(data.iloc[nearest[i]][11]))

    finalstr += tmp

    finalstr += """
            ]
        }
    """
    # print(finalstr)

    message = FlexSendMessage(
        alt_text="附近AED資訊", contents=json.loads(finalstr.encode("utf-8"), strict=False))

    return message


print(make_flex_carousel(22.99546960869026, 120.21004385692507))
# print(eachLiff(""))
