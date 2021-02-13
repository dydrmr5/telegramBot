import random

# baca isi_bot.txt
def botGreetings():
  greets = []
  open_file_isi = open("isi_bot.txt")
  get_isi = open_file_isi.readlines()
  for isi in get_isi:
    greets.append(isi.strip())
  return random.choice(greets)

# baca list_perintah.txt
def showMenu():
  list_menu = '''
  /start = mulai bot\n/menu = tampilkan menu peribahasa\n/help = bantuan
  '''
  return list_menu 

# --------------------MENU PERIBAHASA-----------------------
menu_peribahasa = '''
/Peribahasa_Bidal\n/Peribahasa_Pepatah\n/Peribahasa_Perumpamaan
'''

# return 1 peribahasa bidal random
def showBidal():
  peribahasa_bidal = ['Ada budi ada talas. Ada budi ada balas.', 'Ikan sepat ikan gabus. Makin cepat makin bagus.', 'Maju terus pantang mundur.', 'Bersatu kita teguh, bercerai kita runtuh.', 'Sekali merdeka, tetap merdeka.']
  return random.choice(peribahasa_bidal)

# return 1 peribahasa pepatah random
def showPepatah():
  peribahasa_pepatah = ['Sehari selembar benang, lama-lama jadi kain', 'Air tenang menghanyutkan', 'Bagai bumi dan langit', 'Berjalan pelihara kaki, berkata pelihara lidah', 'Di mana ada kemauan, di situ ada jalan']
  return random.choice(peribahasa_pepatah)

# return 1 peribahasa perumpamaan random
def showPerumpamaan():
  peribahasa_perumpamaan = ['Bagai air di atas daun talas', 'Bagai anjing mengunyah tulang', 'Menepuk air di dulang terpercik muka sendiri', 'Sambil menyelam minum air', 'Belum beranak sudah berbesan']
  return random.choice(peribahasa_perumpamaan)
