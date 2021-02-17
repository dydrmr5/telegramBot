# import modules and files
import telebot
import random
import peribahasa
import menu_reply

# TELEGRAM BOT TOKEN
bot = telebot.TeleBot("1660574633:AAG4qU37ciBZp49Kc0OX4GAWH3GUeLyCCUw", parse_mode = None)

# ---------- main menu ----------
# bot reply : greetings/menyapa
@bot.message_handler(commands = ['hi'])
def sentGreets(message):
	user = message.from_user.first_name
	bot.reply_to(message, f'{menu_reply.botGreetings()} {user} 👋')

# bot reply : menu (daftar menu bot)
@bot.message_handler(commands = ['menu'])
def sentInfo(message):
	bot.reply_to(message, menu_reply.botShowMenu())

# bot reply : tampilkan menu (jenis-jenis) peribahasa
@bot.message_handler(commands = ['jenis'])
def sentMenu(message):
	bot.reply_to(message, menu_reply.botShowPeribahasa())


# ---------- menu (jenis-jenis) peribahasa ----------
# bot reply : pilih jenis peribahasa menu
@bot.message_handler(commands = ['peribahasa'])
def showPeribahasa(message):
	perintah = message.text[11:]
	if 'bidal' in perintah.lower():
		bot.reply_to(message, peribahasa.getBidal())
	elif 'pepatah' in perintah.lower():
		bot.reply_to(message, peribahasa.getPepatah())
	elif 'perumpamaan' in perintah.lower():
		bot.reply_to(message, peribahasa.getPerumpamaan())
	else:
		bot.reply_to(message, 'Peribahasa tidak ditemukan 😔')






print('Bot is RUNNING')
bot.polling()
