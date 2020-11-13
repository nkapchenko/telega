from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging #debug
from config import TOKEN

# parse bot
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

# set debug logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Dixit bot, the game!")


# define start handler
start_handler = CommandHandler('start', start)
# add it to bot
dispatcher.add_handler(start_handler)


#start the bot
if __name__ == '__main__':
    updater.start_polling()

