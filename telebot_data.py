# import module
import random as rd


# LIST EMOJIS
eyeglasses_emojis = ["🤓" ,"😎"]
pointing_hands = ["🤙", "👈", "👉", "👆", "👇", "☝️", "👍"]

# COMMANDS DAN TOKEN BOT TELEGRAM
BOT_TOKEN = "1660574633:AAG4qU37ciBZp49Kc0OX4GAWH3GUeLyCCUw"
bot_commands = ['start', 'hi', 'menu', 'jenis', 'peribahasa', 'pengertian', 'lapor']

# EMOJIS FUNCTIONS
def happy_emoji():
	happy_emojis = ["😃", "😄", "😁", "😊", "😇", "🙂", "🤗"]
	# menghasilkan 1 (random) happy emoji
	return rd.choice(happy_emojis)


def sad_emoji():
	sad_emojis = ["😔", "🙁", "😢", "😨", "😰", "😥", "😓"]
	# menghasilkan 1 (random) sad emoji
	return rd.choice(sad_emojis)


def waving_hand():
	waving_hands = ["👋", "🤚", "🖐", "✋", "🙌"]
	# menghasilkan 1 (random) waving hands emoji
	return rd.choice(waving_hands)


def bot_start():
	# reply dari bot saat pertama dimulai (distart)
	tentang_bot = f'''Saya adalah bot Peribahasa Indonesia.\
	\nSaya bertugas memberikan informasi\
	\ntentang peribahasa Indonesia, untuk\
	\nmenambah pengetahuan kakak {happy_emoji()}.\
	\n\nPilih /menu untuk melihat daftar perintah
	'''
	return tentang_bot


def bot_greetings():
	# mereply user (secara random) saat disapa (/hi)
	greets = []
	open_halo = open("txt_files/halo.txt")
	read_halo = open_halo.readlines()
	for isi in read_halo:
		greets.append(isi.strip())
	return rd.choice(greets)


def bot_show_menu():
	# mereply daftar menu bot ke user (/menu)
	list_menu = f'''DAFTAR PERINTAH {pointing_hands[4]}\
	\n/pengertian = Pengertian peribahasa\
	\n/hi = Menyapa bot\
	\n/menu = Daftar seluruh perintah\
	\n/jenis = Jenis-jenis peribahasa\
	\n/lapor = Bicara ke developer\
	'''
	return list_menu 


def bot_show_peribahasa():
	# mereply daftar jenis-jenis peribahasa ke user (/jenis)
	list_peribahasa = f'''Jenis - Jenis Peribahasa {pointing_hands[4]}\
	\n/peribahasa_bidal\
	\n/peribahasa_pepatah\
	\n/peribahasa_perumpamaan\
	\n/peribahasa_tamsil\
	\n/peribahasa_semboyan\
	'''
	return list_peribahasa


def show_pengertian_peribahasa():
	# mereply (pengertian) apa itu peribahasa ke user (/pengertian)
	pengertian = f'''Apa Itu Peribahasa ?\
	\nMenurut Kamus Besar Bahasa Indonesia,\
	\nPeribahasa adalah kelompok kata atau\
	\nkalimat yang tetap susunannya, dan\
	\nbiasanya mengiaskan maksud tertentu.\
	'''
	return pengertian

def print_line():
	# menampilkan garis pembatas
	line = u'\u2500' * 20
	
	return line


def get_bidal():
	# menampilkan peribahasa bidal secara random
	peribahasa_bidal = []
	open_bidal = open("txt_files/bidal.txt")
	read_first_line = open_bidal.readline()
	read_bidal = open_bidal.readlines()[1:]
	for isi in read_bidal:
		peribahasa_bidal.append(isi.strip())
	random_bidal = "\n".join(rd.sample(peribahasa_bidal, 3))
	return (f'{read_first_line}\nNih kak, 3 Peribahasa Bidal {eyeglasses_emojis[1]}\n{print_line()}\n{random_bidal}')


def get_pepatah():
	# menampilkan peribahasa pepatah secara random
	peribahasa_pepatah = []
	open_pepatah = open("txt_files/pepatah.txt")
	read_first_line = open_pepatah.readline()
	read_pepatah = open_pepatah.readlines()[1:]
	for isi in read_pepatah:
		peribahasa_pepatah.append(isi.strip())
	random_pepatah = "\n".join(rd.sample(peribahasa_pepatah, 3))
	return (f'{read_first_line}\nNih kak, 3 Peribahasa Pepatah {eyeglasses_emojis[1]}\n{print_line()}\n{random_pepatah}')


def get_perumpamaan():
	# menampilkan peribahasa perumpamaan secara random
	peribahasa_perumpamaan = []
	open_perumpamaan = open("txt_files/perumpamaan.txt")
	read_first_line = open_perumpamaan.readline()
	read_perumpamaan = open_perumpamaan.readlines()[1:]
	for isi in read_perumpamaan:
		peribahasa_perumpamaan.append(isi.strip())
	random_perumpamaan = "\n".join(rd.sample(peribahasa_perumpamaan, 3))
	return (f'{read_first_line}\nNih kak, 3 Peribahasa Perumpamaan {eyeglasses_emojis[1]}\n{print_line()}\n{random_perumpamaan}')


def get_tamsil():
	# menampilkan peribahasa tamsil secara random
	peribahasa_tamsil = []
	open_tamsil = open("txt_files/tamsil.txt")
	read_first_line = open_tamsil.readline()
	read_tamsil = open_tamsil.readlines()[1:]
	for isi in read_tamsil:
		peribahasa_tamsil.append(isi.strip())
	random_tamsil = "\n".join(rd.sample(peribahasa_tamsil, 3))
	return (f'{read_first_line}\nNih kak, 3 Peribahasa Tamsil {eyeglasses_emojis[1]}\n{print_line()}\n{random_tamsil}')


def get_semboyan():
	# menampilkan peribahasa semboyan secara random
	peribahasa_semboyan = []
	open_semboyan = open("txt_files/semboyan.txt")
	read_first_line = open_semboyan.readline()
	read_semboyan = open_semboyan.readlines()[1:]
	for isi in read_semboyan:
		peribahasa_semboyan.append(isi.strip())
	random_semboyan = "\n".join(rd.sample(peribahasa_semboyan, 3))
	return (f'{read_first_line}\nNih kak, 3 Peribahasa Semboyan {eyeglasses_emojis[1]}\n{print_line()}\n{random_semboyan}')


def get_peribahasa(user_input):
	# cek kategori sesuai input user, lalu tampilkan contoh peribahasanya
	if 'bidal' in user_input.lower():
		result = get_bidal()
	elif 'pepatah' in user_input.lower():
		result = get_pepatah()
	elif 'perumpamaan' in user_input.lower():
		result = get_perumpamaan()
	elif 'tamsil' in user_input.lower():
		result = get_tamsil()
	elif 'semboyan' in user_input.lower():
		result = get_semboyan()
	else:
		result = (f'Peribahasa tidak ditemukan {sad_emoji()}')

	return result
