import random

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
	list_menu = '''
	/hi = Menyapa bot\
	\n/menu = Daftar seluruh menu\
	\n/jenis = Jenis-jenis peribahasa\
	'''
	return list_menu 

# function tampilkan daftar (jenis-jenis) peribahasa (/peribahasa)
def botShowPeribahasa():
	list_peribahasa = '''
	/peribahasa_bidal\n\
	/peribahasa_pepatah\n\
	/peribahasa_perumpamaan
	'''
	return list_peribahasa
