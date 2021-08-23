# import module
import random as rd
from telebot.apihelper import RETRY_ON_ERROR


# LIST EMOJIS
eyeglasses_emojis = ["🤓", "😎"]
pointing_hands = ["🤙", "👈", "👉", "👆", "👇", "☝️", "👍"]
other_emojis = ["📚", "📘", "📕"]

# COMMANDS DAN TOKEN BOT TELEGRAM
BOT_TOKEN = "1660574633:AAG4qU37ciBZp49Kc0OX4GAWH3GUeLyCCUw"
# ERROR_MESSAGE = "Peribahasa tidak ditemukan"
bot_commands = [
	"start",
	"halo",
	"menu",
	"jenis",
	"pengertian",
	"lapor",
	"peribahasa_bidal",
	"peribahasa_pepatah",
	"peribahasa_perumpamaan",
	"peribahasa_tamsil",
	"peribahasa_semboyan",
	"apa_itu_peribahasa",
	"apa_itu_pepatah",
	"apa_itu_bidal",
	"apa_itu_perumpamaan",
	"apa_itu_tamsil",
	"apa_itu_semboyan",
	"semua",
	"semua_pepatah",
	"semua_bidal",
	"semua_perumpamaan",
	"semua_tamsil",
	"semua_semboyan",
]


# FUNCTIONS EMOJIS
def happy_emoji():
	# menghasilkan 1 (random) happy emoji
	happy_emojis = ["😃", "😄", "😁", "🙂", "🤗"]
	return rd.choice(happy_emojis)


def sad_emoji():
	# menghasilkan 1 (random) sad emoji
	sad_emojis = ["😔", "😢", "😰", "😥", "😓"]
	return rd.choice(sad_emojis)


def waving_hand():
	waving_hands = ["👋", "🤚", "🖐", "✋", "🙌"]
	# menghasilkan 1 (random) waving hands emoji
	return rd.choice(waving_hands)


def print_line():
	# print 20 garis lurus (-) tanpa spasi
	line = "\u2500" * 20

	return line


def bot_start():
	# reply dari bot saat pertama dimulai (distart)
	tentang_bot = f"""Saya adalah bot Peribahasa Indonesia.\
		\nSaya bertugas memberikan informasi\
		\ntentang peribahasa Indonesia, untuk\
		\nmenambah pengetahuan kakak {happy_emoji()}.\
		\n\nPilih /menu untuk melihat daftar perintah
		"""
	return tentang_bot


def bot_show_menu():
	# mereply daftar menu bot ke user (/menu)
	list_menu = f"""{other_emojis[2]} Daftar Perintah {other_emojis[2]}\
		\n/halo = Menyapa bot\
		\n/pengertian = Kumpulan pengertian\
		\n/menu = Daftar seluruh perintah\
		\n/jenis = Melihat peribahasa berdasarkan jenis\
		\n/semua = Melihat semua peribahasa (A - Z)\
		\n/lapor = Bicara ke developer\
		"""
	return list_menu


def bot_show_jenis(command):
	# mereply daftar jenis-jenis peribahasa ke user (/jenis)
	list_peribahasa = f"""{other_emojis[2]} Jenis - Jenis Peribahasa {other_emojis[2]}\
		\n/peribahasa_pepatah\
		\n/peribahasa_bidal\
		\n/peribahasa_perumpamaan\
		\n/peribahasa_tamsil\
		\n/peribahasa_semboyan\
		"""
	return list_peribahasa


def show_pilihan_pengertian():
	# mereply daftar pengertian-pengertian ke user (/pengertian)
	list_pengertian = f"""{other_emojis[2]} Pengertian - Pengertian {other_emojis[2]}\
		\n/apa_itu_peribahasa\
		\n/apa_itu_pepatah\
		\n/apa_itu_bidal\
		\n/apa_itu_perumpamaan\
		\n/apa_itu_tamsil\
		\n/apa_itu_semboyan\
		"""
	return list_pengertian


# mereply (pengertian) apa itu peribahasa ke user
def get_pengertian_peribahasa():
	pengertian = f"""{other_emojis[0]} Peribahasa {other_emojis[0]}\
	\nMenurut Kamus Besar Bahasa Indonesia,\
	\nPeribahasa adalah kelompok kata atau\
	\nkalimat yang tetap susunannya, dan\
	\nbiasanya mengiaskan maksud tertentu.\
	\n(https://kbbi.web.id/)\
	"""
	return pengertian


def get_pengertian_pepatah():
	pengertian = f"""{other_emojis[0]} Pepatah {other_emojis[0]}\
	\nPepatah adalah jenis peribahasa yang\
	\nberisikan nasihat atau ajaran. Nasihat\
	\natau ajaran dalam pepatah biasanya\
	\nberasal dari orang-orang terdahulu.\
	\n(https://dosenbahasa.com/)\
	"""
	return pengertian


def get_pengertian_bidal():
	pengertian = f"""{other_emojis[0]} Bidal {other_emojis[0]}\
	\nBidal adalah jenis peribahasa yang memiliki\
	\nrima dan irama. Bidal sebenarnya termasuk\
	\ndalam jenis puisi lama, tetapi karena\
	\nbentuknya peribahasa maka dapat juga\
	\ndikategorikan sebagai salah satu jenis peribahasa.\
	\n(https://dosenbahasa.com/)\
	"""
	return pengertian


def get_pengertian_perumpamaan():
	pengertian = f"""{other_emojis[0]} Perumpamaan {other_emojis[0]}\
	\nPerumpamaan adalah jenis peribahasa yang\
	\nMengungkapkan suatu kondisi tertentu.\
	\nCiri khas dari peribahasa perumpamaan yaitu\
	\npenggunaan kata seperti, bagai, dan bagaikan.\
	\n(https://dosenbahasa.com/)\
	"""
	return pengertian


def get_pengertian_tamsil():
	pengertian = f"""{other_emojis[0]} Tamsil {other_emojis[0]}\
	\nTamsil/ibarat adalah jenis peribahasa\
	\nyang berfungsi untuk menunjukkan ataupun\
	\nmenyatakan perbandingan tentang suatu hal.\
	\n(https://dosenbahasa.com/)\
	"""
	return pengertian


def get_pengertian_semboyan():
	pengertian = f"""{other_emojis[0]} Semboyan {other_emojis[0]}\
	\nSemboyan adalah peribahasa dengan bentuk\
	\nkalimat, frasa ataupun kata yang digunakan\
	\nsebagai pedoman dan prinsip hidup seseorang\
	\nataupun sekelompok orang.\
	\n(https://dosenbahasa.com/)\
	"""
	return pengertian


def get_bidal():
	# menampilkan peribahasa bidal secara random
	peribahasa_bidal = []
	open_bidal = open("txt_files/bidal.txt")
	read_bidal = open_bidal.readlines()
	for isi in read_bidal:
		makna = isi.replace('x', '\n')
		peribahasa_bidal.append(makna.strip())
	random_bidal = "\n".join(rd.sample(peribahasa_bidal, 1))
	return f"{other_emojis[0]} Peribahasa Bidal {other_emojis[0]}\n{print_line()}\n{random_bidal}"


def get_pepatah():
	# menampilkan peribahasa pepatah secara random
	peribahasa_pepatah = []
	open_pepatah = open("txt_files/pepatah.txt")
	read_pepatah = open_pepatah.readlines()
	for isi in read_pepatah:
		makna = isi.replace('x', '\n')
		peribahasa_pepatah.append(makna.strip())
	random_pepatah = "\n".join(rd.sample(peribahasa_pepatah, 1))
	return f"{other_emojis[0]} Peribahasa Pepatah {other_emojis[0]}\n{print_line()}\n{random_pepatah}"


def get_perumpamaan():
	# menampilkan peribahasa perumpamaan secara random
	peribahasa_perumpamaan = []
	open_perumpamaan = open("txt_files/perumpamaan.txt")
	read_perumpamaan = open_perumpamaan.readlines()
	for isi in read_perumpamaan:
		makna = isi.replace('x', '\n')
		peribahasa_perumpamaan.append(makna.strip())
	random_perumpamaan = "\n".join(rd.sample(peribahasa_perumpamaan, 1))
	return f"{other_emojis[0]} Peribahasa Perumpamaan {other_emojis[0]}\n{print_line()}\n{random_perumpamaan}"


def get_tamsil():
	# menampilkan peribahasa tamsil secara random
	peribahasa_tamsil = []
	open_tamsil = open("txt_files/tamsil.txt")
	read_tamsil = open_tamsil.readlines()
	for isi in read_tamsil:
		makna = isi.replace('x', '\n')
		peribahasa_tamsil.append(makna.strip())
	random_tamsil = "\n".join(rd.sample(peribahasa_tamsil, 1))
	return f"{other_emojis[0]} Peribahasa Tamsil {other_emojis[0]}\n{print_line()}\n{random_tamsil}"


def get_semboyan():
	# menampilkan peribahasa semboyan secara random
	peribahasa_semboyan = []
	open_semboyan = open("txt_files/semboyan.txt")
	read_semboyan = open_semboyan.readlines()
	for isi in read_semboyan:
		makna = isi.replace('x', '\n')
		peribahasa_semboyan.append(makna.strip())
	random_semboyan = "\n".join(rd.sample(peribahasa_semboyan, 1))
	return f"{other_emojis[0]} Peribahasa Semboyan {other_emojis[0]}\n{print_line()}\n{random_semboyan}"


def show_pilihan_semua():
# mereply daftar jenis-jenis peribahasa ke user (/jenis)
	list_pilihan = f"""{other_emojis[2]} Tampilkan Semua Peribahasa {other_emojis[2]}\
		\n/semua_pepatah\
		\n/semua_bidal\
		\n/semua_perumpamaan\
		\n/semua_tamsil\
		\n/semua_semboyan\
		"""
	return list_pilihan


def show_semua_pepatah():
	# menampilkan semua peribahasa pepatah berurutan (A-Z)
	pepatah = []
	with open("txt_files/pepatah.txt") as txt_pepatah:
		for isi in txt_pepatah.readlines():
			txt_pepatah = isi.replace('x', '\n')
			pepatah.append(txt_pepatah)

	pepatah.sort()
	sorted_pepatah = '\n'.join(map(str, pepatah))
	return f"{other_emojis[2]} Semua Peribahasa Pepatah {other_emojis[2]}\n{print_line()}\n{sorted_pepatah}"


def show_semua_bidal():
	# menampilkan semua peribahasa bidal berurutan (A-Z)
	bidal = []
	with open("txt_files/bidal.txt") as txt_bidal:
		for isi in txt_bidal.readlines():
			txt_bidal = isi.replace('x', '\n')
			bidal.append(txt_bidal)

	bidal.sort()
	sorted_bidal = '\n'.join(map(str, bidal))
	return f"{other_emojis[2]} Semua Peribahasa Bidal {other_emojis[2]}\n{print_line()}\n{sorted_bidal}"


def show_semua_perumpamaan():
	# menampilkan semua peribahasa perumpamaan berurutan (A-Z)
	perumpamaan = []
	with open("txt_files/perumpamaan.txt") as txt_perumpamaan:
		for isi in txt_perumpamaan.readlines():
			txt_perumpamaan = isi.replace('x', '\n')
			perumpamaan.append(txt_perumpamaan)

	perumpamaan.sort()
	sorted_perumpamaan = '\n'.join(map(str, perumpamaan))
	return f"{other_emojis[2]} Semua Peribahasa Perumpamaan {other_emojis[2]}\n{print_line()}\n{sorted_perumpamaan}"


def show_semua_tamsil():
	# menampilkan semua peribahasa tamsil berurutan (A-Z)
	tamsil = []
	with open("txt_files/tamsil.txt") as txt_tamsil:
		for isi in txt_tamsil.readlines():
			txt_tamsil = isi.replace('x', '\n')
			tamsil.append(txt_tamsil)

	tamsil.sort()
	sorted_tamsil = '\n'.join(map(str, tamsil))
	return f"{other_emojis[2]} Semua Peribahasa Tamsil {other_emojis[2]}\n{print_line()}\n{sorted_tamsil}"


def show_semua_semboyan():
	# menampilkan semua peribahasa semboyan berurutan (A-Z)
	semboyan = []
	with open("txt_files/semboyan.txt") as txt_semboyan:
		for isi in txt_semboyan.readlines():
			txt_semboyan = isi.replace('x', '\n')
			semboyan.append(txt_semboyan)

	semboyan.sort()
	sorted_semboyan = '\n'.join(map(str, semboyan))
	return f"{other_emojis[2]} Semua Peribahasa Semboyan {other_emojis[2]}\n{print_line()}\n{sorted_semboyan}"
