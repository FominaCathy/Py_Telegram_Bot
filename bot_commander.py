
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
#from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import telegram
import logging
import calculer


def start(update, context):
    # `bot.send_message` это метод Telegram API
    # `update.effective_chat.id` - определяем `id` чата, 
    # откуда прилетело сообщение 
    select_case  = str(f"Привет! Что будем делать?:\n"
                        "/work - работать \n "
                        "/calc - считать \n "
                        "/game - играть (в крестики-нолики")

    context.bot.send_message(chat_id=update.effective_chat.id, text=select_case)

def hello(update, context):


    user  = update.effective_user.first_name
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Здравствуй, {user}")
    
def help(update, context):
    input_menu  = str(f"/help - вывод меню \n "
                        "/start - начало работы \n "
                        "/sum - после команды укажите 2 числа, которые нужно сложить (/sum 123 23)")
    context.bot.send_message(chat_id=update.effective_chat.id, text=input_menu)


def sum(update, context):
    msg = update.context.args #update.message.text 
    item = msg.split()
    input_txt = str(int(item[1]) + int(item[2]))

    context.bot.send_message(chat_id=update.effective_chat.id, text=input_txt)

def work(update, context):

    user  = update.effective_user.first_name
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ну давай поработаем, {user}")

def calc  (update, context):
    #calc_text = context #update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"что считать?")

    
    #print (calc_text)
    #context.bot.send_message(chat_id=update.effective_chat.id, text=f"{calc_text}")

def message (update, context):
    result = calculer.calculer(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{update.message.text} = {result}")

    #return update.message.text