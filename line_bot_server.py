from flask import Flask, request
import json
# import LINE Message API 
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    # get msg
    body = request.get_data(as_text=True)
    try:
        # Convert to json format
        json_data = json.loads(body)
        
        # channel access token
        access_token = 'your channel access token'
        
        # LINE Channel secret
        secret = 'your channel secret'

        # check access_token
        line_bot_api = LineBotApi(access_token)

        # check secret
        handler = WebhookHandler(secret)     

        # add header
        signature = request.headers['X-Line-Signature']

        # handle msg & header
        handler.handle(body, signature)

        # get replyToken (Used when returning)
        tk = json_data['events'][0]['replyToken']

        # get input type
        type = json_data['events'][0]['message']['type']
        
        # if input type == text
        if type=='text':
            # get msg
            reply = json_data['events'][0]['message']['text']
        else:
            reply = 'some error'
            
        # return
        line_bot_api.reply_message(tk,TextSendMessage(reply))
    except:
        print(body)
    # Webhook verification
    return 'OK'

if __name__ == "__main__":
    app.run()
