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
    # print(api.access_token)ß
    #テキストメッセージの送信
    api.post_text_message(uuid.UUID(ROOM_ID),mes)
# for room in api.get_rooms():
    # api.post_text_message(room['uuid'], 'pythonから送信')
    # if room['uuid'] == '8058d5b2-dbe3-4737-b640-8dcd9d2dc9b3':
    # print(type(room['uuid']))