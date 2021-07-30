## Bot Telegram Peribahasa Indonesia
[![license](https://img.shields.io/github/license/ctrlbzul/telegramBot?style=for-the-badge)](LICENSE)
[![python testing](https://img.shields.io/github/workflow/status/ctrlbzul/telegramBot/TelegramBot-testing?label=python%20testing&style=for-the-badge)](https://github.com/ctrlbzul/telegramBot/actions/workflows/python-app.yml)
[![code-testing-bot](https://img.shields.io/github/workflow/status/ctrlbzul/telegramBot/CodeQL?label=code%20analysis&style=for-the-badge)](https://github.com/ctrlbzul/telegramBot/actions/workflows/codeql-analysis.yml)
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Menurut Kamus Besar Bahasa Indonesia (KBBI), peribahasa adalah kelompok kata atau kalimat yang tetap susunannya, biasanya mengiaskan maksud tertentu (dalam peribahasa termasuk juga bidal, ungkapan, dan perumpamaan).
<br/>Bot telegram peribahasa Indonesia ([@peribahasa_bot](https://t.me/peribahasa_bot)) ini merupakan bot yang saya buat untuk skripsi, demi menyelesaikan pendidikan di jenjang Strata 1 (S1). [@peribahasa_bot](https://t.me/peribahasa_bot) dihadirkan sebagai media informasi peribahasa Indonesia yang di dalamnya terdapat lebih dari 60 peribahasa yang sudah dikelompokkan berdasarkan jenis-jenisnya yaitu pepatah, bidal, perumpamaan, tamsil dan semboyan untuk memudahkan pengguna dalam menemukan peribahasa yang dibutuhkan.[@peribahasa_bot](https://t.me/peribahasa_bot) diharapkan dapat memberi informasi sekaligus pembelajaran yang bermanfaat peribahasa Indonesia.

## System Requirements
to runn @peribahasa_bot, u need requirements below:
 - Python 3.x version with pip and [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) installed.

## Installation
- python3 installation (Ubuntu)
  - install supporting softwares
  ```bash
  sudo apt-get install software-properties-common
  ```
  - adding PPA deadsnakes
  ```bash
  sudo add-apt-repository ppa:deadsnakes/ppa
  ```
  - installing python3 (version python3.8)
  ```bash
  sudo apt-get install python3.8
  ```
  note : you can install the newer version of python by typing version of python (3.9)
- python3 installation (Windows)
  - on windows, you can install the python installer by visit [the python website](https://www.python.org/downloads/)

- pyTelegramBotAPI installation
  ```bash
  pip install pyTelegramBotAPI
  ```
- other installation
  you can install from ```requirements.txt``` by typing
  ```bash
  pip install -r requirements.txt
  ```

## How to Run @peribahasa_bot
after python3, pip and pyTelegramBotApi installed, run the telebot program by :
```bash
python3 main.py
```

## Features Update
for information updates or adding more features,  you can see at [issue by labeled enhacement](https://github.com/ctrlbzul/telegramBot/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)
