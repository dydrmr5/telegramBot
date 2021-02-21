# --------------- TOKEN BOT TELEGRAM DAN COMMANDS ---------------
bot_token = "1660574633:AAG4qU37ciBZp49Kc0OX4GAWH3GUeLyCCUw"
commands_telebot = ['start', 'hi', 'menu', 'jenis', 'peribahasa', 'pengertian']

# ----- function-function untuk return jenis-jenis peribahasa -----
import random
import emojis

# function : print garis lurus
def printLine():
	return f'------------------------------------------------------------'

# function : return pengertian dan contoh peribahasa bidal secara random
def getBidal():
	peribahasa_bidal = []
	open_bidal = open("txt_files/bidal.txt")
	read_first_line = open_bidal.readline()
	read_bidal = open_bidal.readlines()[1:]
	for isi in read_bidal:
		peribahasa_bidal.append(isi.strip())
	random_bidal = "\n".join(random.sample(peribahasa_bidal, 3))
	return ("{0}\nNih kak, 3 Peribahasa Bidal {1}👇\n{2}\n{3}".format(read_first_line, emojis.eyeglasses_emojis[1] ,printLine(), random_bidal))

# function : return peribahasa pepatah secara random
def getPepatah():
	peribahasa_pepatah = []
	open_pepatah = open("txt_files/pepatah.txt")
	read_first_line = open_pepatah.readline()
	read_pepatah = open_pepatah.readlines()
	for isi in read_pepatah:
		peribahasa_pepatah.append(isi.strip())
	random_pepatah = "\n".join(random.sample(peribahasa_pepatah, 3))
	return ("{0}\nNih kak, 3 Peribahasa Pepatah {1}👇\n{2}\n{3}".format(read_first_line, emojis.eyeglasses_emojis[1], printLine(), random_pepatah))

# function : return peribahasa perumpamaan secara random
def getPerumpamaan():
	peribahasa_perumpamaan = []
	open_perumpamaan = open("txt_files/perumpamaan.txt")
	read_first_line = open_perumpamaan.readline()
	read_perumpamaan = open_perumpamaan.readlines()
	for isi in read_perumpamaan:
		peribahasa_perumpamaan.append(isi.strip())
	random_perumpamaan = "\n".join(random.sample(peribahasa_perumpamaan, 3))
	return ("{0}\nNih kak, 3 Peribahasa Perumpamaan {1}👇\n{2}\n{3}".format(read_first_line, emojis.eyeglasses_emojis[1], printLine(), random_perumpamaan))
