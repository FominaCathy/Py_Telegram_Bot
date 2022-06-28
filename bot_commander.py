
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
#from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import telegram
import logging

import todo_commander



def start(update, context):

    select_case  = str(f"Привет! Что будем делать?:\n"
                        "/work - работать \n "# ДЗ 9
                        "/game - играть (в крестики-нолики") # ДЗ 10

    context.bot.send_message(chat_id=update.effective_chat.id, text=select_case)



#для списка задач

def work(update, context):
    
    user  = update.effective_user.first_name
    input_menu  = str(f"МЕНЮ: \n "
                        "/todo - список дел на сегодня \n "
                        "/add - добавить дело \n"
                        "/del - укажите после комманды номер дела которое нужно удалить")

    context.bot.send_message(chat_id=update.effective_chat.id, text = input_menu)

def todo_list (update, context): # список дел на сегодня
    #result = "список дел"
    result = todo_commander.print_case()
    context.bot.send_message(chat_id=update.effective_chat.id, text = result)
    
def add_work(update, context):
    text = str(' '.join(context.args))
    if text =="": 
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"введите новое дело в формате: /add ваше новое дело")
    else:
        todo_commander.add_str(text)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Добавили новое дело: {text}")
    

def del_work(update, context):
    text = len(context.args)
    if len(context.args) != 1 or context.args[0].isdigit() != True: 
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"введите номер удаляемого дела: /del номер дела")
    #elif 
    else:
        text_input = todo_commander.delete_str(int(context.args[0]))
        
        context.bot.send_message(chat_id=update.effective_chat.id, text = text_input)
    




   
#def help(update, context):
#    input_menu  = str(f"/help - вывод меню \n "
#                        "/start - начало работы \n "
#                        "/sum - после команды укажите 2 числа, которые нужно сложить (/sum 123 23)")
#    context.bot.send_message(chat_id=update.effective_chat.id, text=input_menu)

#
#def sum(update, context):
#    msg = update.context.args #update.message.text 
#    item = msg.split()
#    input_txt = str(int(item[1]) + int(item[2]))
#
#    context.bot.send_message(chat_id=update.effective_chat.id, text=input_txt)
