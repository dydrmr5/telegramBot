import random
import emojis

# function first reply bot saat start (/start)
def botStart():
	tentang_bot = '''Saya adalah bot Peribahasa Indonesia {0}.\
	\nSaya bertugas untuk memberikan informasi\
	\ntentang Peribahasa kepada kakak, agar\
	\nkakak mendapat pengetahuan baru dan\
	\nPeribahasa kita akan terus terlestarikan {1}.\
	\n\nApa itu Peribahasa ? {2}\
	\nMenurut Kamus Besar Bahasa Indonesia (KBBI),\
	Peribahasa adalah kelompok kata atau kalimat\
	yang tetap susunannya, biasanya mengiaskan\
	maksud tertentu kak (dalam peribahasa termasuk\
	juga bidal, ungkapan, dan perumpamaan).\
	\n\nKetik /menu untuk melihat seluruh perintah kak
	'''.format(emojis.happy(), emojis.waving_hands[4], emojis.pointing_hands[4])
	return tentang_bot

# function random reply (balasan) bot (/hi)
def botGreetings():
	greets = []
	open_halo = open("txt_files/halo.txt")
	read_halo = open_halo.readlines()
	for isi in read_halo:
		greets.append(isi.strip())
	return random.choice(greets)

# function tampilkan bot main menu (/menu)
def botShowMenu():
	list_menu = '''LIST SELURUH MENU {}\
	\n/hi = Menyapa bot\
	\n/menu = Daftar seluruh menu\
	\n/jenis = Jenis-jenis peribahasa\
	'''.format(emojis.pointing_hands[4])
	return list_menu 

# function tampilkan daftar (jenis-jenis) peribahasa (/peribahasa)
def botShowPeribahasa():
	list_peribahasa = '''JENIS-JENIS PERIBAHASA {}\
	\n/peribahasa_bidal\
	\n/peribahasa_pepatah\
	\n/peribahasa_perumpamaan\
	\n/peribahasa_tamsil\
	\n/peribahasa_semboyan\
	'''.format(emojis.pointing_hands[4])
	return list_peribahasa
