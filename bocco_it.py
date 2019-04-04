import bocco
import uuid
API_KEY = "API_KEY"
MAIL = 'mail address'
PASS = 'pass'
ROOM_ID = 'ROOM_ID'

def send_bocco(mes):
    print(mes)
    api = bocco.api.Client('ACCESS TOKEN')

    api = bocco.api.Client.signin(API_KEY, MAIL, PASS)
    # print(api.access_token)
    #テキストメッセージの送信
    api.post_text_message(uuid.UUID(ROOM_ID),mes)