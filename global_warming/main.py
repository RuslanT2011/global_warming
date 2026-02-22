import telebot
from bot_logic import global_warming_briefly, global_warming_all, fighting, help
import random
import os

bot = telebot.TeleBot("8553695172:AAEkEsDcE1gSWiHktAzjNKFLveIKDQyTqYA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome=help()
    bot.reply_to(message, welcome)

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['global_warming_briefly'])
def send_text(message):
    text=global_warming_briefly()
    bot.reply_to(message, f"Вот краткая сводка: {text}")

@bot.message_handler(commands=['global_warming_all'])
def send_information(message):
    information=global_warming_all()
    bot.reply_to(message, f"Я предлагаю вам изучить информацию на одном из этих сайтов для изучения подробной информации: {information}")

@bot.message_handler(commands=['the_consequences'])
def send_consequences(message):
    consequences=random.choice(os.listdir('Static/Image'))
    with open(f'Static/Image/{consequences}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['fighting'])
def send_fighting(message):
    methods=fighting()
    bot.reply_to(message, f"Вот несколько способов борьбы с глобальным потеплением:        {methods}")

# Запускаем бота
bot.polling()