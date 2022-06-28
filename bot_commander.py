
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

import telegram
import logging

import todo_commander



def start(update, context):    
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
    

