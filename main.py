from flask import Flask, request
import telegram
import os

TOKEN = os.environ["
          8421413550:AAExUX-mxbEo2zaYK3yeX3jaRgd-L-p5y00
        "]
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"You said: {text}")
    return 'ok'

if __name__ == '__main__':
    app.run()
