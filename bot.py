import telebot
import os
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    button1 = types.KeyboardButton("📝 Подать объявление")
    button2 = types.KeyboardButton("📜 Правила")
    button3 = types.KeyboardButton("❓ Помощь")

    keyboard.add(button1)
    keyboard.add(button2, button3)

    bot.send_message(
        message.chat.id,
        "🏠 Отдам Даром Краснодар\n\n"
        "Здесь можно бесплатно отдать вещи тем, кому они нужны.\n\n"
        "Выберите действие:",
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda message: message.text == "📝 Подать объявление")
def create_ad(message):

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    categories = [
        "👕 Одежда",
        "👶 Детские вещи",
        "🛋 Мебель",
        "📱 Электроника",
        "📚 Книги",
        "🍽 Посуда",
        "🔧 Другое"
    ]

    for category in categories:
        keyboard.add(types.KeyboardButton(category))

    bot.send_message(
        message.chat.id,
        "Выберите категорию:",
        reply_markup=keyboard
    )


bot.infinity_polling()
