#import controller

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
#from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import telegram
import logging
import bot_commander
import calculer

bot = telegram.Bot('5549395398:AAG75bKf059jORftOlNHwAb1YpAJu0rU5tg')

updater = Updater(token='5549395398:AAG75bKf059jORftOlNHwAb1YpAJu0rU5tg', use_context=True)
dispatcher = updater.dispatcher

# TODO 
def begin (update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"считаем {context}")

def cancel(update, context):
     # Заканчиваем разговор.
    update.message.reply_text('чтобы вызвать меню - набери /start')
    return ConversationHandler.END   

start_handler = CommandHandler('start', bot_commander.start)
dispatcher.add_handler(start_handler)

hello_handler = CommandHandler('hello', bot_commander.hello)
dispatcher.add_handler(hello_handler)

help_handler = CommandHandler('help', bot_commander.help)
dispatcher.add_handler(help_handler)

cancel_handler = CommandHandler('cancel', cancel)
dispatcher.add_handler(cancel_handler)

work_handler = CommandHandler('work', bot_commander.work)
dispatcher.add_handler(work_handler)

calc_handler = ConversationHandler(  
                entry_points=[CommandHandler('calc', bot_commander.calc)],
                states={begin: [MessageHandler(Filters.text, bot_commander.message),"что считаем"]},
                fallbacks=[CommandHandler('cancel', cancel)]

)


dispatcher.add_handler(calc_handler)

message_handler = MessageHandler(Filters.text, bot_commander.message)
dispatcher.add_handler(message_handler)


print('start bot')
updater.start_polling()

#controller.run()