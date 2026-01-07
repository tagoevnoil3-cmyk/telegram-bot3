import telebot
import os
TOKEN = os.getenn"8057069793:AAGUfWr8OVPZKOCPX34JvMUk9eaBTf5jXHg"
if not TOKEN:
	raise ValueError("BOT_TOKEN" is not set")                                      
	bot = telebot.Telebot(TOKEN)
	@bot.messsage_handler(commands=['start']) 
	def start(message):
		bot.send_messssage(message.chat.id."Бот раотает") 
		bot.infinity_polling()

