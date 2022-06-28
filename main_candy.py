#На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# ход = сумма конфет // (28+1) - остаток от деления

from asyncio.log import logger
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import telegram
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import bot_commander

logger = logging.getLogger('logger')
case_lever = logging.getLogger('case_lever')
logger.info = 2021
BEGIN, CANDY = range(2)

bot = telegram.Bot('5549395398:AAG75bKf059jORftOlNHwAb1YpAJu0rU5tg')

updater = Updater(token='5549395398:AAG75bKf059jORftOlNHwAb1YpAJu0rU5tg', use_context=True)
dispatcher = updater.dispatcher

def game (update, context): # 
    
    task = str("На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга."
                "За один ход можно забрать не более чем 28 конфет." 
                "Все конфеты достаются сделавшему последний ход. " )
    context.bot.send_message(chat_id=update.effective_chat.id, text = task)
      
    context.bot.send_message(chat_id=update.effective_chat.id, text = "Ты готов?: да/нет")
    return BEGIN


def begin (update, context): # 
    
    if str(update.message.text).lower() == 'да':
        keyboard = [['Простой', 'Сложный']]
        markup_key = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard=True)

        context.bot.send_message(chat_id=update.effective_chat.id, text = "Выбери уровень: Простой/Сложный",reply_markup=markup_key,)
        
        case_lever.info = markup_key

        lever = str("введите кол-во конфет, которое берете (от 1 до 28): ")
        context.bot.send_message(chat_id=update.effective_chat.id, text = lever)
    
        return CANDY
    else:
        ConversationHandler.END




def candy (update, context):
    user = update.message.from_user  # определяем пользователя
  
    stack_candy = int(logger.info)

    step_game = int(update.message.text)

    lever = str("введите кол-во конфет, которое берете (от 1 до 28): ")
    context.bot.send_message(chat_id=update.effective_chat.id, text = lever)

 
    if (step_game == stack_candy)and(step_game < 29): # игрок забирает остатки конфет
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"{user.first_name}, ты выиграл! Поздавляю!")
        return ConversationHandler.END
    elif (stack_candy - step_game)<29 : # ход бота и конфет 28 и меньше - тогда бот выиграл
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"{user.first_name}, я выиграл!")
        return ConversationHandler.END
    else:
        stack_candy = stack_candy - step_game
        step_bot =  stack_candy%29
        msg = f"мой ход: {step_bot}. \n В куче осталось {(stack_candy - step_bot)}" #ход бота
        context.bot.send_message(chat_id=update.effective_chat.id, text = msg)
        stack_candy -= step_bot #определяем остаток конфет в куче
        logger.info =  stack_candy   

def end(update, _):
       
    user = update.message.from_user  # определяем пользователя
    update.message.reply_text("заход в END")
    # Заканчиваем игру
    return ConversationHandler.END


candy_handler = ConversationHandler(
        entry_points=[CommandHandler('game', game)],
        states= {
            BEGIN: [MessageHandler(Filters.text, begin)], 
            CANDY: [MessageHandler(Filters.text, candy)]
                },
        fallbacks=[CommandHandler('end', end)],
    )

dispatcher.add_handler(candy_handler)

print('start bot')
updater.start_polling()
updater.idle()
