# -*- coding: utf-8 -*-
"""15 занятие первая часть.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/155MZDEJLDt5S1_SBHJjBoW74sT4fKyBD
"""

pip install pyTelegramBotAPI

import telebot
token = '1224229009:AAGTPwdUO0Orgafshln4svSYsOjPSnj6nkg'

bot = telebot.TeleBot(token)
@bot.message_handler(content_types= ["text"])
def repeat_all_messages(message):
  bot.send_message(message.chat.id, message.text)

bot.infinity_polling()

import telebot
token = '1224229009:AAGTPwdUO0Orgafshln4svSYsOjPSnj6nkg'
import random

devizi = ["Ozon самый лучший на свете", " Озон молодец", "Как же хорошо работать в этой компании"]

bot = telebot.TeleBot(token)
@bot.message_handler(content_types= ["text"])
def repeat_ozon_message(message):
  if message.text == "Ozon":
    message.text = random.choice(devizi)
    bot.send_message(message.chat.id, message.text)



bot.infinity_polling()

Простой бот-будильник
Он может замедлять сообщения

