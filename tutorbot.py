from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import time
from tqdm.contrib.telegram import tqdm 
import logging
TOKEN = '5317967624:AAHmCMJ2iNkLXuPiPA2k6CylUuUj70PPUJs'

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Functions
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi!")

def answer(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Be loud!")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# def runtqdm(update: Update, context: CallbackContext):
#     for i in tqdm(range(10), token=TOKEN, chat_id=update.effective_chat.id):
#         pass

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

#handlers
start_handler = CommandHandler('start', start)
question_handler = CommandHandler('help', answer)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# tqdm_handler = CommandHandler('tqdm', runtqdm)
caps_handler = CommandHandler('caps', caps)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(question_handler)
dispatcher.add_handler(echo_handler)
# dispatcher.add_handler(tqdm_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()