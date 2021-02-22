# import module dan file
import random
import emojis

# --------------- TOKEN BOT TELEGRAM DAN COMMANDS ---------------
bot_token = "1660574633:AAG4qU37ciBZp49Kc0OX4GAWH3GUeLyCCUw"
commands_telebot = ['start', 'hi', 'menu', 'jenis', 'peribahasa', 'pengertian']

# ----- function-function untuk return jenis-jenis peribahasa -----


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

# function : return pengertian dan contoh peribahasa pepatah secara random
def getPepatah():
	peribahasa_pepatah = []
	open_pepatah = open("txt_files/pepatah.txt")
	read_first_line = open_pepatah.readline()
	read_pepatah = open_pepatah.readlines()[1:]
	for isi in read_pepatah:
		peribahasa_pepatah.append(isi.strip())
	random_pepatah = "\n".join(random.sample(peribahasa_pepatah, 3))
	return ("{0}\nNih kak, 3 Peribahasa Pepatah {1}👇\n{2}\n{3}".format(read_first_line, emojis.eyeglasses_emojis[1], printLine(), random_pepatah))

# function : return pengertian dan contoh peribahasa perumpamaan secara random
def getPerumpamaan():
	peribahasa_perumpamaan = []
	open_perumpamaan = open("txt_files/perumpamaan.txt")
	read_first_line = open_perumpamaan.readline()
	read_perumpamaan = open_perumpamaan.readlines()[1:]
	for isi in read_perumpamaan:
		peribahasa_perumpamaan.append(isi.strip())
	random_perumpamaan = "\n".join(random.sample(peribahasa_perumpamaan, 3))
	return ("{0}\nNih kak, 3 Peribahasa Perumpamaan {1}👇\n{2}\n{3}".format(read_first_line, emojis.eyeglasses_emojis[1], printLine(), random_perumpamaan))

# function : return pengertian dan contoh peribahasa tamsil/idiom secara random
def getTamsil():
	peribahasa_tamsil = []
	open_tamsil = open("txt_files/tamsil.txt")
	read_first_line = open_tamsil.readline()
	read_tamsil = open_tamsil.readlines()[1:]
	for isi in read_tamsil:
		peribahasa_tamsil.append(isi.strip())
	random_tamsil = "\n".join(random.sample(peribahasa_tamsil, 3))
	return ("{0}\nNih kak, 3 Peribahasa Tamsil {1}👇\n{2}\n{3}".format(read_first_line, emojis.eyeglasses_emojis[1], printLine(), random_tamsil))

# function : return pengertian dan contoh peribahasa semboyan secara random
def getSemboyan():
	peribahasa_semboyan = []
	open_semboyan = open("txt_files/semboyan.txt")
	read_first_line = open_semboyan.readline()
	read_semboyan = open_semboyan.readlines()[1:]
	for isi in read_semboyan:
		peribahasa_semboyan.append(isi.strip())
	random_semboyan = "\n".join(random.sample(peribahasa_semboyan, 3))
	return ("{0}\nNih kak, 3 Peribahasa Semboyan {1}👇\n{2}\n{3}".format(read_first_line, emojis.eyeglasses_emojis[1], printLine(), random_semboyan))

# function : get kategori peribahasa sesuai input (perintah) user,
# lalu return function pengertian dan contoh peribahasa 
def getKategoriPeribahasa(user_input):
	if 'bidal' in user_input.lower():
		result = getBidal()
	elif 'pepatah' in user_input.lower():
		result = getPepatah()
	elif 'perumpamaan' in user_input.lower():
		result = getPerumpamaan()
	elif 'tamsil' in user_input.lower():
		result = getTamsil()
	elif 'semboyan' in user_input.lower():
		result = getSemboyan()
	else:
		result = ('Peribahasa tidak ditemukan kak {}'.format(emojis.sad()))

	# return result
	return result
