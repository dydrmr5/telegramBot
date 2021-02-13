# import modules and file
import telebot
import random
import peribahasa

# TELEGRAM BOT TOKEN
bot = telebot.TeleBot("1660574633:AAG4qU37ciBZp49Kc0OX4GAWH3GUeLyCCUw", parse_mode = None)

# bot : reply/greetings
@bot.message_handler(commands = ['hi'])
def sentMsg(message):
	user = message.from_user.first_name
	bot.reply_to(message, f'{peribahasa.botGreetings()} {user} 👋')

# bot : show menu
@bot.message_handler(commands = ['help'])
def sentInfo(message):
	bot.reply_to(message, peribahasa.showMenu())

# bot : show peribahasa menu
@bot.message_handler(commands = ['menu'])
def showMenu(message):
  bot.reply_to(message, peribahasa.menu_peribahasa)

# bot : choose peribahasa menu
@bot.message_handler(commands = ['peribahasa'])
def showPeribahasa(message):
	perintah = message.text[11:]
	if 'bidal' in perintah.lower():
		bot.reply_to(message, peribahasa.showBidal())
	elif 'pepatah' in perintah.lower():
		bot.reply_to(message, peribahasa.showPepatah())
	elif 'perumpamaan' in perintah.lower():
		bot.reply_to(message, peribahasa.showPerumpamaan())
	else:
		bot.reply_to(message, 'Peribahasa tidak ditemukan 😔')






print('Bot is RUNNING')
bot.polling()
