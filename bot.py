import telebot
import os
print("TOKEN = 8057069793:AAGUfWr8OVPZKOCPX34JvMUk9eaBTf5jXHg",os.getenv("BOT.TOKEN"))
if not TOKEN:
	raise ValueError("BOT_TOKEN" is not set")                                      
	bot = telebot.Telebot(TOKEN)
	@bot.messsage_handler(commands=['start']) 
	def start(message):
		bot.send_messssage(message.chat.id."Бот раотает") 
		bot.infinity_polling()


