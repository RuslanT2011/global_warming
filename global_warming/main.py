import telebot
from bot_logic import global_warming_briefly, global_warming_all
import random
import os

bot = telebot.TeleBot("8553695172:AAEkEsDcE1gSWiHktAzjNKFLveIKDQyTqYA")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, для краткого изучения информации о глобальном потеплении можете ввести /global_warming_briefly, для полной сводки - /global_warming_all, также вы можете подробно изучить, к чему может привести глобальное потепление по команде /the_consequences")

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

# Запускаем бота
bot.polling()