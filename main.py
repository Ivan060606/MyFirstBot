from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5961608915:AAHPK4_QMlnYQC2aMZq58a1iqwRX8OdM3Tg')
updater = Updater(token='5961608915:AAHPK4_QMlnYQC2aMZq58a1iqwRX8OdM3Tg')
dispather = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Привет, {update.effective_user.first_name}!')

def text(update, context):
    text = update.message.text.split()
    list = []
    fragment = 'абв'
    for elem in text:
        if fragment not in elem:
            list.append(elem)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))

start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, text)

dispather.add_handler(start_handler)
dispather.add_handler(message_handler)

updater.start_polling()
updater.idle()