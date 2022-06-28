#import controller

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
import telegram
import bot_commander



bot = telegram.Bot('5549395398:AAG75bKf059jORftOlNHwAb1YpAJu0rU5tg')

updater = Updater(token='5549395398:AAG75bKf059jORftOlNHwAb1YpAJu0rU5tg', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', bot_commander.start)
dispatcher.add_handler(start_handler)

# список дел
work_handler = CommandHandler('work', bot_commander.work)
dispatcher.add_handler(work_handler)

todo_handler = CommandHandler('todo', bot_commander.todo_list)
dispatcher.add_handler(todo_handler)

add_handler = CommandHandler('add', bot_commander.add_work)
dispatcher.add_handler(add_handler)

del_handler = CommandHandler('del', bot_commander.del_work)
dispatcher.add_handler(del_handler)




print('start bot')
updater.start_polling()
updater.idle()
#controller.run()