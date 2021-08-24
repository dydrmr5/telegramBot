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
    text_info = "%s, %s, %s, %s\n" % (tanggal, user_id, username, user_command)
    save_data_log = open("data.txt", "a")
    save_data_log.write(text_info)
    save_data_log.close()


# bot commands = /start
@bot.message_handler(commands=[f"{td.bot_commands[0]}"])
def get_user_info(message):
    # dapatkan info user
    print(
        """User ID : %s\
        \nUsername : %s\
        \nCommand : %s""" % (message.from_user.id, message.from_user.first_name, message.text)
    )
    save_log(message, "%s" % td.bot_commands[0])

    user = message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Halo kak {user} {td.waving_hand()}.\n{td.bot_start()}",
    )


# bot commands = /hi
@bot.message_handler(commands=[f"{td.bot_commands[1]}"])
def sent_greets(message):
    user = message.from_user.first_name
    bot.reply_to(message, f"Halo kak {user} {td.waving_hand()}.")


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
        td.bot_show_jenis(td.bot_commands[3]),
        reply_markup=keyboard_button,
    )


# bot commands = /pengertian
@bot.message_handler(commands=[f"{td.bot_commands[4]}"])
def show_pengertian(message):
    keyboard_button = types.ReplyKeyboardMarkup(row_width=1)
    pengertian = types.KeyboardButton("Pengertian".capitalize())
    menu = types.KeyboardButton("Menu".capitalize())

    keyboard_button.add(pengertian, menu)
    bot.reply_to(
        message,
        td.show_pilihan_pengertian(),
        reply_markup=keyboard_button,
    )


# bot commands = /lapor
@bot.message_handler(commands=[f"{td.bot_commands[5]}"])
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
@bot.message_handler(commands=[f"{td.bot_commands[6]}"])
def show_peribahasa_bidal(message):
    try:
        bot.reply_to(message, td.get_bidal())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.basicConfig(level=logging.error)
        logging.error("error: %s" % error_message)


# bot commands = /peribahasa_pepatah
@bot.message_handler(commands=[f"{td.bot_commands[7]}"])
def show_peribahasa_pepatah(message):
    try:
        bot.reply_to(message, td.get_pepatah())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.basicConfig(level=logging.error)
        logging.error("error: %s" % error_message)


@bot.message_handler(commands=[f"{td.bot_commands[8]}"])
def show_peribahasa_perumpamaan(message):
    try:
        bot.reply_to(message, td.get_perumpamaan())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.basicConfig(level=logging.error)
        logging.error("error: %s" % error_message)


@bot.message_handler(commands=[f"{td.bot_commands[9]}"])
def show_peribahasa_tamsil(message):
    try:
        bot.reply_to(message, td.get_tamsil())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.basicConfig(level=logging.error)
        logging.error("error: %s" % error_message)


@bot.message_handler(commands=[f"{td.bot_commands[10]}"])
def show_peribahasa_semboyan(message):
    try:
        bot.reply_to(message, td.get_semboyan())
    except Exception as error_message:
        bot.reply_to(message, td.ERROR_MESSAGE)
        logging.basicConfig(level=logging.error)
        logging.error("error: %s" % error_message)


@bot.message_handler(commands=[f"{td.bot_commands[11]}"])
def show_pengertian_peribahasa(message):
    bot.reply_to(message, td.get_pengertian_peribahasa(), disable_web_page_preview=True)


@bot.message_handler(commands=[f"{td.bot_commands[12]}"])
def show_pengertian_pepatah(message):
    bot.reply_to(message, td.get_pengertian_pepatah(), disable_web_page_preview=True)


@bot.message_handler(commands=[f"{td.bot_commands[13]}"])
def show_pengertian_bidal(message):
    bot.reply_to(message, td.get_pengertian_bidal(), disable_web_page_preview=True)


@bot.message_handler(commands=[f"{td.bot_commands[14]}"])
def show_pengertian_perumpamaan(message):
    bot.reply_to(message, td.get_pengertian_perumpamaan(), disable_web_page_preview=True)


@bot.message_handler(commands=[f"{td.bot_commands[15]}"])
def show_pengertian_tamsil(message):
    bot.reply_to(message, td.get_pengertian_tamsil(), disable_web_page_preview=True)


@bot.message_handler(commands=[f"{td.bot_commands[16]}"])
def show_pengertian_semboyan(message):
    bot.reply_to(message, td.get_pengertian_semboyan(), disable_web_page_preview=True)


@bot.message_handler(commands=[f"{td.bot_commands[17]}"])
def show_semua_peribahasa(message):
    keyboard_button = types.ReplyKeyboardMarkup(row_width=1)
    semua = types.KeyboardButton("Semua".capitalize())
    menu = types.KeyboardButton("Menu".capitalize())

    keyboard_button.add(semua, menu)
    bot.reply_to(
        message,
        td.show_pilihan_semua(),
        reply_markup=keyboard_button,
    )


@bot.message_handler(commands=[f"{td.bot_commands[18]}"])
def show_semua_peribahasa(message):
    bot.reply_to(message, td.show_semua_pepatah())


@bot.message_handler(commands=[f"{td.bot_commands[19]}"])
def show_semua_peribahasa(message):
    bot.reply_to(message, td.show_semua_bidal())


@bot.message_handler(commands=[f"{td.bot_commands[20]}"])
def show_semua_peribahasa(message):
    bot.reply_to(message, td.show_semua_perumpamaan())


@bot.message_handler(commands=[f"{td.bot_commands[21]}"])
def show_semua_peribahasa(message):
    bot.reply_to(message, td.show_semua_tamsil())


@bot.message_handler(commands=[f"{td.bot_commands[22]}"])
def show_semua_peribahasa(message):
    bot.reply_to(message, td.show_semua_semboyan())


@bot.message_handler(func=lambda message: True)
def custom_messages(message):
    print(
        """User ID : %s\
        \nUsername : %s\
        \nCommand : %s""" % (message.from_user.id, message.from_user.first_name, message.text)
    )
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
    elif "Pengertian" in message.text:
        bot.reply_to(message, f"{td.show_pilihan_pengertian()}")
    elif "Semua" in message.text:
        bot.reply_to(message, f"{td.show_pilihan_semua()}")
    elif "Jenis" in message.text:
        bot.reply_to(message, f"{td.bot_show_jenis()}")


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
        """@peribahasa_bot is running !\
        \nDate : %s\
        \nTime : %s %s\
        \nRunning on : %s""" % (datetime.datetime.now().strftime('%d %B %Y'), datetime.datetime.now().strftime('%H:%M'), time_periode, platform.system())
    )
    print(td.print_line())

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('server is running!'.upper())
    bot.polling()
except Exception as error:
    logging.basicConfig(level=logging.error)
    logging.error("error : %s" % error)
except BaseException as error_base_exception:
    logging.basicConfig(level=logging.error)
    logging.error("error : %s" % error_base_exception)
except KeyboardInterrupt as keyboard:
    logging.basicConfig(level=logging.error)
    logging.error("error keyboard interrupt : %s" % keyboard)
