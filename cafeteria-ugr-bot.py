#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Bot para obtener el menú de las cafeterías de la UGR
# que estén relacionadas con Grupo Gómez Moreno

from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url(option):
    url = 'http://www.grupogonzalezmoreno.es/' + option + '.pdf'

    return url

def bbaa(bot, update):
    url = get_url('bbaa')
    chat_id = update.message.chat_id
    bot.sendDocument(chat_id=chat_id, document=url)

def fyl(bot, update):
    url = get_url('fyl')
    chat_id = update.message.chat_id
    bot.sendDocument(chat_id=chat_id, document=url)

def etsag(bot, update):
    url = get_url('etsag')
    chat_id = update.message.chat_id
    bot.sendDocument(chat_id=chat_id, document=url)

def empresariales(bot, update):
    url = get_url('empresariales')
    chat_id = update.message.chat_id
    bot.sendDocument(chat_id=chat_id, document=url)

def ccsalud(bot, update):
    url = get_url('ccsalud')
    chat_id = update.message.chat_id
    bot.sendDocument(chat_id=chat_id, document=url)

def farmacia(bot, update):
    url = get_url('farmacia')
    chat_id = update.message.chat_id
    bot.sendDocument(chat_id=chat_id, document=url)

def main():
	token_file = open("token.txt", "r")

	token = Updater(token_file.read(), use_context=True)
	dp = token.dispatcher

	token_file.close()
	
	dp.add_handler(CommandHandler('bbaa',bbaa))
	dp.add_handler(CommandHandler('fyl',fyl))
	dp.add_handler(CommandHandler('etsag',etsag))
	dp.add_handler(CommandHandler('empresariales',empresariales))
	dp.add_handler(CommandHandler('ccsalud',ccsalud))
	dp.add_handler(CommandHandler('farmacia',farmacia))

	token.start_polling()
	token.idle()

if __name__ == '__main__':
    main()