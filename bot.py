import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🏠 Отдам Даром Краснодар\n\n"
        "Добро пожаловать!\n\n"
        "Здесь можно бесплатно отдать вещи тем, кому они нужны.\n\n"
        "Нажмите кнопку ниже, чтобы подать объявление."
    )


bot.infinity_polling()
