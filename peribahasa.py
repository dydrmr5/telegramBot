# --------------- TOKEN BOT TELEGRAM ---------------
bot_token = "1660574633:AAG4qU37ciBZp49Kc0OX4GAWH3GUeLyCCUw"
commands_telebot = ['start', 'hi', 'menu', 'jenis', 'peribahasa']

# ----- function-function untuk return jenis-jenis peribahasa -----
import random
import emojis

# function : print garis lurus
def printLine():
	return f'------------------------------------------------------------'

# function : return peribahasa bidal secara random
def getBidal():
	peribahasa_bidal = []
	open_bidal = open("txt_files/bidal.txt")
	read_bidal = open_bidal.readlines()
	for isi in read_bidal:
		peribahasa_bidal.append(isi.strip())
	random_bidal = "\n".join(random.sample(peribahasa_bidal, 3))
	return ("Nih kak, 3 Peribahasa Bidal {0}👇\n{1}\n{2}".format(emojis.eyeglasses_emojis[1] ,printLine(), random_bidal))

# function : return peribahasa pepatah secara random
def getPepatah():
	peribahasa_pepatah = []
	open_pepatah = open("txt_files/pepatah.txt")
	read_pepatah = open_pepatah.readlines()
	for isi in read_pepatah:
		peribahasa_pepatah.append(isi.strip())
	random_pepatah = "\n".join(random.sample(peribahasa_pepatah, 3))
	return ("Nih kak, 3 Peribahasa Pepatah {0}👇\n{1}\n{2}".format(emojis.eyeglasses_emojis[1], printLine(), random_pepatah))

# function : return peribahasa perumpamaan secara random
def getPerumpamaan():
	peribahasa_perumpamaan = []
	open_perumpamaan = open("txt_files/perumpamaan.txt")
	read_perumpamaan = open_perumpamaan.readlines()
	for isi in read_perumpamaan:
		peribahasa_perumpamaan.append(isi.strip())
	random_perumpamaan = "\n".join(random.sample(peribahasa_perumpamaan, 3))
	return ("Nih kak, 3 Peribahasa Perumpamaan {0}👇\n{1}\n{2}".format(emojis.eyeglasses_emojis[1], printLine(), random_perumpamaan))
