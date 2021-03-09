# import module
import telebot
from telebot import types
import random
import datetime
import platform
import os
from sys import platform as _platform



# import file
import peribahasa
import menu_reply
import emojis


def save_log(message, command_user):
	tanggal = datetime.datetime.now()
	tanggal = tanggal.strftime('%d-%B-%Y')

	userId = message.chat.id
	username = message.chat.first_name
	text_information = f'{tanggal}, {userId}, {username}, {command_user}\n'
	save_data_log = open('data.txt', 'a')
	save_data_log.write(text_information)
	save_data_log.close()

#@peribahasa_bot

# TELEGRAM BOT TOKEN
bot = telebot.TeleBot(peribahasa.BOT_TOKEN, parse_mode = None)

# ---------- BOT MENU ----------
# bot reply : perkenalan
@bot.message_handler(commands = [f'{peribahasa.commands_telebot[0]}']) # /start
def sentStartInfo(message):
	# get user info
	print(f"User ID  : {message.from_user.id}")
	print(f"Username : {message.from_user.first_name}")
	print(f"Message  : {message.text}")
	save_log(message, f'{peribahasa.commands_telebot[0]}')
	#------------------------------------
	user = message.from_user.first_name
	#bot.reply_to(message, f'{menu_reply.botGreetings()} {user} {emojis.handWaves()}.\n{menu_reply.botStart()}')
	floathing_button = types.InlineKeyboardMarkup()
	user_information = types.InlineKeyboardButton('bicara dengan developer', url="telegram.me/zulfikriry")
	
	floathing_button.row(user_information)
	bot.send_message(message.chat.id, f'{menu_reply.botGreetings()} {user} {emojis.handWaves()}.\n{menu_reply.botStart()}', reply_markup = floathing_button )

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
	keyboard_button = types.ReplyKeyboardMarkup(row_width = 2)
	pepatah = types.KeyboardButton('Pepatah')
	bidal = types.KeyboardButton('Bidal')
	perumpamaan = types.KeyboardButton('Perumpamaan')
	tamsil = types.KeyboardButton('Tamsil')
	semboyan = types.KeyboardButton('Semboyan')

	keyboard_button.add(pepatah, bidal, perumpamaan, tamsil, semboyan)
	bot.send_message(message.chat.id, f'pilih peribahasa {emojis.pointing_hands[4]}', reply_markup = keyboard_button )

	bot.reply_to(message, menu_reply.botShowPeribahasa())

# bot reply : tampilkan pengertian dan contoh dari jenis peribahasa (yang diinput user)
@bot.message_handler(commands = [f'{peribahasa.commands_telebot[4]}']) # /peribahasa
def showPeribahasa(message):
	perintah = message.text[11:]
	bot.reply_to(message, peribahasa.getKategoriPeribahasa(perintah))


@bot.message_handler(func = lambda message: True)
def custom_message(message):
	print(f"User ID  : {message.from_user.id}")
	print(f"Username : {message.from_user.first_name}")
	print(f"Message  : {message.text}")

	save_log(message, message.text)
	if "hai" in message.text:
		user = message.from_user.first_name	
		bot.reply_to(message, f'{menu_reply.botGreetings()} {user} {emojis.handWaves()}.')

	elif "Pepatah" in message.text:
		bot.reply_to(message, f'pepatah')


# run the bot

if _platform == "linux" or _platform == "linux2":
	os.system("clear")
elif _platform == "darwin":
	os.system("clear")
else:
	os.system("cls")

print('-----------------------')
print('bot running !')
print(f"date :{datetime.datetime.now().strftime('%d-%B-%Y')}")
print(f'running on : {platform.system()}')
bot.polling()
