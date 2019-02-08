from skpy import Skype
import requests
import random

r = requests.get('https://quotes.rest/qod.json')
try:
    quote_author = r.json()['contents']['quotes'][0]['author']
except KeyError:
    quote_author = None
try:
    quote = r.json()['contents']['quotes'][0]['quote']
except KeyError:
    quote = None

templates = ['Assalamuwalaikum, Good morning all :) \n',
             'Assalamuwalaikum, Good Morning B-) \n',
             'Assalamuwalaikum, Suprovaaaaaaaat team :D \n',
             'Assalamuwalaikum, Good morning team :D \n']
if quote is not None and quote_author is not None:
    msg_body = random.choice(templates)+'Here\'s a nice quote to start your day with:\n' + "\"" + quote + "\""+' By: '+quote_author
else:
    msg_body = random.choice(list(enumerate(templates)))[1]
sk = Skype("username", "passwd")
ch = sk.chats.chat('rahiv')
ch.sendMsg(msg_body)
