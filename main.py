# import module dan file
import telebot
import random
import peribahasa
import menu_reply
import emojis

# TELEGRAM BOT TOKEN
bot = telebot.TeleBot(peribahasa.bot_token, parse_mode = None)

# ---------- BOT MENU ----------
# bot reply : perkenalan
@bot.message_handler(commands = [f'{peribahasa.commands_telebot[0]}']) # /start
def sentStartInfo(message):
	#get information user
	print(f"User ID  : {message.from_user.id}")
	print(f"Username : {message.from_user.first_name}")
	print(f"Message  : {message.text}")
	#------------------------------------
	user = message.from_user.first_name
	bot.reply_to(message, f'{menu_reply.botGreetings()} {user} {emojis.handWaves()}.\n{menu_reply.botStart()}')

# bot reply : greetings/menyapa
@bot.message_handler(commands = [f'{peribahasa.commands_telebot[1]}']) # /hi
def sentGreets(message):
	user = message.from_user.first_name
	bot.reply_to(message, f'{menu_reply.botGreetings()} {user} {emojis.handWaves()}.')

# bot reply : menu (daftar menu bot)
@bot.message_handler(commands = [f'{peribahasa.commands_telebot[2]}']) # /menu
def sentInfo(message):
	bot.reply_to(message, menu_reply.botShowMenu())

# bot reply : tampilkan menu (jenis-jenis) peribahasa
@bot.message_handler(commands = [f'{peribahasa.commands_telebot[3]}']) # /jenis
def sentMenu(message):
	bot.reply_to(message, menu_reply.botShowPeribahasa())

# bot reply : tampilkan pengertian dan contoh dari jenis peribahasa (yang diinput user)
@bot.message_handler(commands = [f'{peribahasa.commands_telebot[4]}']) # /peribahasa
def showPeribahasa(message):
	perintah = message.text[11:]
	bot.reply_to(message, peribahasa.getKategoriPeribahasa(perintah))






print('Bot is RUNNING')

bot.polling()
