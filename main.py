from secrets import botToken
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from random import randint

updater = Updater(token=botToken)
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="What's up nigga?")


def echo(bot, update):
    stickers = bot.getStickerSet(name='TalkToMe').stickers
    bot.send_sticker(chat_id=update.message.chat_id, sticker=stickers[randint(0,len(stickers))])

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.all, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
updater.start_polling()
