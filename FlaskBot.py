from flask import Flask, request, app
import flask
from flask_sslify import SSLify
import telebot
from telebot import types
import re
from Currency_defs import *
import time

# URL = 'https://api.telegram.org/bot535143387:AAFXwFzA7w8u7yG7HZUQslYPUBl5H_a7DE4/setWebhook?url=https://bdda6a79' \
      '.ngrok.io/ '
EURO = 'eur/usd 💶'
POUND = 'gbp/usd  💷 '
YEN = 'jpy/usd 💴'
# app = Flask(__name__)
# sslify = SSLify(app)

bot = telebot.TeleBot('535143387:AAFXwFzA7w8u7yG7HZUQslYPUBl5H_a7DE4')


# bot.set_webhook(URL)


@bot.message_handler(commands=['start'])
def start_message(message):  # Название функции не играет никакой роли, в принципе
    markup = types.ReplyKeyboardMarkup()
    markup.row(EURO,POUND,YEN)
    markup.row('gold', 'silver', 'platinum', 'oil Brent ⛽')
    bot.send_message(message.chat.id, "Choose currency:", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    print(message.text.strip())
    if message.text == EURO:
        bot.send_message(message.chat.id, get_currency('eur-usd'), parse_mode='markdown')
    elif message.text == YEN:
        bot.send_message(message.chat.id, get_currency('jpy-usd'), parse_mode='markdown')
    elif message.text.strip(' ') == POUND.strip(' '):
        bot.send_message(message.chat.id, get_currency('gbp-usd'), parse_mode='markdown')
    elif message.text == 'gold':
        bot.send_message(message.chat.id, get_commodities('gold'), parse_mode='markdown')
    elif message.text == 'silver':
        bot.send_message(message.chat.id, get_commodities('silver'), parse_mode='markdown')
    elif message.text == 'platinum':
        bot.send_message(message.chat.id, get_commodities('platinum'), parse_mode='markdown')
    elif message.text == 'oil Brent ⛽':
        bot.send_message(message.chat.id, get_commodities('brent-oil'), parse_mode='markdown')
    else:
    	markup = types.ReplyKeyboardMarkup()
    	markup.row(EURO,POUND,YEN)
    	markup.row('gold', 'silver', 'platinum', 'oil Brent ⛽')
    	bot.send_message(message.chat.id, "Choose currency from keyboard:", reply_markup=markup)	



# # @app.route('/', methods=["POST"])
# def post():
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)
#     return '<h1>Ebali v rotyaru vsex flask i python<h1>'


# # @app.route('/', methods=["GET"])
# def get():
#     return '<h1>Ebali v rotyaru vsex flask i python<h1>'


if __name__ == '__main__':
    try:
        # app.run(port=8080)
        bot.remove_webhook()
        bot.polling()
    except ConnectionError:
        pass
