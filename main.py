# import module
import datetime
import logging
import os
import platform
from sys import platform as _platform

import telebot
from telebot import types

# import file
import telebot_data as td

# TELEGRAM BOT TOKEN
bot = telebot.TeleBot(td.BOT_TOKEN, parse_mode=None)


def save_log(message, user_command):
    # menyimpan info aktivitas user ke data.txt
    tanggal = datetime.datetime.now()
    tanggal = tanggal.strftime("%d-%B-%Y")

    user_id = message.chat.id
    username = message.chat.first_name
    text_info = f"{tanggal}, {user_id}, {username}, {user_command}\n"
    save_data_log = open("data.txt", "a")
    save_data_log.write(text_info)
    save_data_log.close()


# bot commands = /start
@bot.message_handler(commands=[f"{td.bot_commands[0]}"])
def get_user_info(message):
    # dapatkan info user
    print(f"User ID  : {message.from_user.id}")
    print(f"Username : {message.from_user.first_name}")
    print(f"Command  : {message.text}")
    save_log(message, f"{td.bot_commands[0]}")

    user = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"{td.bot_greetings()} {user} {td.waving_hand()}.\n{td.bot_start()}",
    )


# bot commands = /hi
@bot.message_handler(commands=[f"{td.bot_commands[1]}"])
def sent_greets(message):
    user = message.from_user.first_name
    bot.reply_to(message, f"{td.bot_greetings()} {user} {td.waving_hand()}.")


# bot commands = /menu
@bot.message_handler(commands=[f"{td.bot_commands[2]}"])
def sent_info(message):
    bot.reply_to(message, td.bot_show_menu())


# bot commands = /jenis
@bot.message_handler(commands=[f"{td.bot_commands[3]}"])
def set_keyboard_button(message):
    keyboard_button = types.ReplyKeyboardMarkup(row_width=2)
    pepatah = types.KeyboardButton("Pepatah".capitalize())
    bidal = types.KeyboardButton("Bidal".capitalize())
    perumpamaan = types.KeyboardButton("Perumpamaan".capitalize())
    tamsil = types.KeyboardButton("Tamsil".capitalize())
    semboyan = types.KeyboardButton("Semboyan".capitalize())
    menu = types.KeyboardButton("Menu".capitalize())

    keyboard_button.add(pepatah, bidal, perumpamaan, tamsil, semboyan, menu)
    bot.reply_to(
        message,
        td.bot_show_peribahasa(td.bot_commands[3]),
        reply_markup=keyboard_button,
    )


# bot commands = /peribahasa
@bot.message_handler(commands=[f"{td.bot_commands[4]}"])
def show_peribahasa(message):
    perintah = message.text[11:]
    bot.reply_to(message, td.get_peribahasa(perintah))


# bot commands = /pengertian
@bot.message_handler(commands=[f"{td.bot_commands[5]}"])
def show_pengertian(message):
    bot.reply_to(message, td.show_pengertian_peribahasa())


# bot commands = /lapor
@bot.message_handler(commands=[f"{td.bot_commands[6]}"])
def report_to_dev(message):
    button = types.InlineKeyboardMarkup()
    dev_info = types.InlineKeyboardButton(
        "Lapor ke Developer", url="telegram.me/zulfikriry"
    )

    button.row(dev_info)
    bot.reply_to(
        message,
        f"Bila ada masalah, kritik ataupun saran,\nsampaikan ke developer ya kak {td.happy_emoji()}.",
        reply_markup=button,
    )


# bot commands = /peribahasa_bidal
@bot.message_handler(commands=[f"{td.bot_commands[7]}"])
def show_peribahasa_bidal(message):
    try:
        bot.reply_to(message, td.get_bidal())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.error(f"error: {error_message}")


# bot commands = /peribahasa_peatah
@bot.message_handler(commands=[f"{td.bot_commands[8]}"])
def show_peribahasa_pepatah(message):
    try:
        bot.reply_to(message, td.get_pepatah())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.error(f"error : {error_message}")


@bot.message_handler(commands=[f"{td.bot_commands[9]}"])
def show_peribahasa_perumpamaan(message):
    try:
        bot.reply_to(message, td.get_pepatah())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.error(f"error: {error_message}")


@bot.message_handler(commands=[f"{td.bot_commands[10]}"])
def show_peribahasa_tamsil(message):
    try:
        bot.reply_to(message, td.get_tamsil())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.error(f"error: {error_message}")


@bot.message_handler(commands=[f"{td.bot_commands[11]}"])
def show_peribahasa_semboyan(message):
    try:
        bot.reply_to(message, td.get_semboyan())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.error(f"error : {error_message}")


@bot.message_handler(func=lambda message: True)
def custom_messages(message):
    print(f"User ID  : {message.from_user.id}")
    print(f"Username : {message.from_user.first_name}")
    print(f"Message  : {message.text}")
    save_log(message, message.text)

    if "Bidal" in message.text:
        bot.reply_to(message, f"{td.get_bidal()}")
    elif "Pepatah" in message.text:
        bot.reply_to(message, f"{td.get_pepatah()}")
    elif "Perumpamaan" in message.text:
        bot.reply_to(message, f"{td.get_perumpamaan()}")
    elif "Tamsil" in message.text:
        bot.reply_to(message, f"{td.get_tamsil()}")
    elif "Semboyan" in message.text:
        bot.reply_to(message, f"{td.get_semboyan()}")
    elif "Menu" in message.text:
        bot.reply_to(message, f"{td.bot_show_menu()}")


# check time periode (AM or PM)
"""
AM = start from 00:00 to 11:59
PM = 12:00 to 23:59
"""
current_time = datetime.datetime.now().strftime("%H:%M")
if current_time <= str("11:59"):
    time_periode = "AM"
else:
    time_periode = "PM"


try:
    """
    get platform of machine
    linux for linux kernel
    darwin for macOs
    NT for windows"""

    if _platform in ["linux", "linux2", "darwin"]:
        os.system("clear")
    else:
        os.system("cls")
        # print bot running info on terminal

    print(td.print_line())
    print(
        f"""@peribahasa_bot is running !\
        \nDate : {datetime.datetime.now().strftime('%d %B %Y')}\
        \nTime : {datetime.datetime.now().strftime('%H:%M')} {time_periode}\
        \nRunning on : {platform.system()}"""
    )
    print(td.print_line())

    bot.polling()
except Exception as error:
    logging.error("error : %s" % error)
except BaseException as error_base_exception:
    logging.error("error : %s" % error_base_exception)
except KeyboardInterrupt as keyboard:
    logging.error("error keyboard interrupt : %s" % keyboard)
