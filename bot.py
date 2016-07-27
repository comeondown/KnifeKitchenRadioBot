from telegram import Emoji, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import subprocess

import logging

from RadioBot import RadioBot
	

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def get_radio(bot, update):
	radio_bot = RadioBot();
	bot.sendMessage(update.message.chat_id, text=radio_bot.get_message(), parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def start():
	token = '156016615:AAErzKgIHReyElffYGTepZf5pEF7-CMAFeg'
	updater = Updater(token)

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("radio", get_radio))
	dp.add_error_handler(error)

	updater.start_polling(clean=True)
	updater.idle()

if __name__=='__main__':
	start()