import discord
import random

ran_num = random.randint(1, 100)
ran_num = str(ran_num)


token = "XXXXXXXXXXXXXXXXXXXXXXXXXXтут надо ввести токенXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def bot_play_text(bot, event):
    if event.data["text"] == "/start":
        bot.send_text(chat_id=event.from_chat, text="Привет! Я бот для игры в угадай число. Начнём?")

def num_play(bot, event):
    if event.data["text"] == ran_num:
        bot.send_text(chat_id=event.from_chat, text="Прям в точку, чел харош")
    elif event.data["text"] > ran_num:
        bot.send_text(chat_id=event.from_chat, text="А вот нет число меньше.")
    elif event.data["text"] < ran_num:
        bot.send_text(chat_id=event.from_chat, text="да блин как ты не поймёшь число больше.")

def bot_play(bot, event):
    if event.data["callbackData"] == "call_btn_id_1":
        bot.send_text(chat_id=event.from_chat, text="Я загадал число от 1 до 100, угадаешь молодец если нет то рано или позно всё равно сможешь найти число.")
        bot.send_text(chat_id=event.from_chat, text="Ваше предположение?")

bot.run(token)
