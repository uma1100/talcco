#!/usr/bin/env python
# coding: utf-8

import requests
import json
from datetime import datetime
import bocco_it as b_i
import random

# APIキー
APIKEY = "API_KEY"
APPID = "APP_ID"


#ループ処理
# while True:
    # メッセージを入力
def send_text(mes,angle):
    # send_text = input()
    # リクエストボディ(JSON形式)
    send_data = {
        "language": "ja-JP",
        "botId": "Chatting",
        "appId": APPID,
        "voiceText": "",
        "appSendTime": "",
        "clientData": {
            "option": {
                "nickname": "ユカイ",
                "nicknameY": "ユカイ",
                "place": "東京"
            },
        },
        }

    # リクエストヘッダ
    headers = {'Context-type': 'application/json'}

    # リクエストURL
    url = "https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY={}".format(APIKEY)
    # endと入力すると終了
    if "おわり" in mes:
        print("おしゃべりを終了します。")
        return

    send_data['voiceText'] = mes
    # 送信時間を取得
    send_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    send_data['appSendTime'] = send_time

    # メッセージを送信
    r = requests.post(url, data=json.dumps(send_data), headers=headers)
    # レスポンスデータから返答内容を取得
    return_data = r.json()
    return_message = return_data['systemText']['expression']
    # print(return_message)
    print(angle)
    # RIGHT
    if 60 <= angle <= 90:
        b_i.send_bocco('/hack \n RIGHT 100')
    # CENTER
    elif 90 < angle < 105:
        b_i.send_bocco('/hack \n UP 100 \n DOWN 100 \n LED 0 0 100 10')
    # LEFt
    elif 105 <= angle <= 125:
        b_i.send_bocco('/hack \n LEFT 100')
    else:
        R = int(random.uniform(0,100))
        G = int(random.uniform(0,100))
        B = int(random.uniform(0,100))
        # 色の設定
        led_color = "LED "+ R + " " + G + " " + B + "20"
        b_i.send_bocco('/hack \n ' + led_color + '\n random')
    b_i.send_bocco(return_message)
    requests.get('https://script.google.com/macros/s/SCRIPT_ID/exec?text='+return_message)
    return