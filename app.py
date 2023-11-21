from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from bs4 import BeautifulSoup

app = Flask(__name__)

# 設定 Line Bot 的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('gIS4eSAOyETZv18tiyNcT4ZZ6274L9UuhLjSowpDjuqYf4dFCNB37+saXJfI1FSr85uiKqqrhteAxVCD3Yjalx/4zC3rshDGfm1/xZXIZmf4pFY2HYnRLs3LqbNiJAmBXAIOwCqSEZTqqnzNa8mfkwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('04279870980e7421fbf1b27cc03165c2')

line_bot_api.push_message('U2032ae75254e026706d91546f58b9af1', TextSendMessage(text='你可以開始了'))
# 綁定 Line Bot 的 Webhook URL
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # 取得 request 的 body
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理收到的訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    reply_text = f"你說了：{text}"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))


if __name__ == "__main__":
    # 設定 Flask 監聽的 port，這裡設定為 8081，預設port為5000
    app.run()

    