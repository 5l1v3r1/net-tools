# -*- coding: utf-8 -*-
# IRAN CYBER SECURITY GROUP
# REAL HACKERS MAKE SECURITY
# EDITORS ARE NOT PROGRAMMERS
# GOOD LUCK
import telebot
from telebot import *
import time
from time import ctime
import sys
import os
import sqlite3
from colorama import Fore, Style
b = Fore.BLUE
r = Fore.RED
g = Fore.GREEN
c = Fore.CYAN
w = Fore.WHITE
y = Fore.YELLOW
res = Style.RESET_ALL
import re, requests, time
import json
execfile("config.py")
reload(sys)
sys.setdefaultencoding("utf-8")
admin = [603064758]
TOKEN = "TOKEN"

def clear():
    gnu = "clear"
    windows = "cls"
    os.system([gnu, windows][os.name == "nt"])

bot = telebot.TeleBot(TOKEN)
db = sqlite3.connect("robot.db", check_same_thread=False)
try:
    db.execute("CREATE TABLE robot(userid PRIMARY KEY, username TEXT)")
    print("{} Table Created !".format(b))
except:
    print("")

clear()
print("{}>>> {} Robot Started {}[{}{}{}]{} <<<".format(g, b, y, r, ctime(), y, g))
print("{} Bot Username ~> {}{}\n{} Bot Id ~> {}{}\n{} Bot Name ~> {}{}".format(r, b, bot.get_me().username, r, b, bot.get_me().id, r, b, bot.get_me().first_name))
print("{} Bot Running ...".format(c))
print("{}=============================".format(c))



@bot.message_handler(content_types=["text"])
def whois(message):
    if re.match("[!/#]?whois (.*)", message.text):
        matches = re.match("[!/#]?whois (.*)", message.text).groups()
        print("{} Whois search for {} From {} ".format(y, matches[0], message.from_user.id))
        reqwho = requests.get("http://api.hackertarget.com/whois/?q={}".format(matches[0]))
        dlwho = open("{}-whois.txt".format(message.from_user.id), "w")
        dlwho.write(reqwho.content + "\n=================\n")
        dlwho.close()
        get_photo_whois = open("{}-whois.txt".format(message.from_user.id))
        bot.send_document(message.chat.id, get_photo_whois)
        get_photo_whois.close()
        bot.send_message(message.chat.id, reqwho.text)
    if re.match("[!/#]?lookup (.*)", message.text):
        matches = re.match("[!/#]?lookup (.*)", message.text).groups()
        print("{} lookup search for {} From {} ".format(y, matches[0], message.from_user.id))
        req = requests.get("http://api.hackertarget.com/dnslookup/?q={}".format(matches[0]))
        dl = open("{}-dnslookup.txt".format(message.from_user.id), "w")
        dl.write(req.content + "\n=================\n")
        dl.close()
        bot.send_document(message.chat.id, open("{}-dnslookup.txt".format(message.from_user.id)))
        bot.send_message(message.chat.id, req.text)
    if re.match("[!/#]?zone (.*)", message.text):
        matches = re.match("[!/#]?zone (.*)", message.text).groups()
        print("{} zone transfer search for {} From {} ".format(y, matches[0], message.from_user.id))
        req = requests.get("http://api.hackertarget.com/zonetransfer/?q={}".format(matches[0]))
        dl = open("{}-zone.txt".format(message.from_user.id), "w")
        dl.write(req.content + "\n=================\n")
        dl.close()
        bot.send_document(message.chat.id, open("{}-zone.txt".format(message.from_user.id)))
        bot.send_message(message.chat.id, req.text)
    if re.match("[!/#]?httpheaders (.*)", message.text):
        matches = re.match("[!/#]?httpheaders (.*)", message.text).groups()
        print("{} httpheaders search for {} From {} ".format(y, matches[0], message.from_user.id))
        req = requests.get("http://api.hackertarget.com/httpheaders/?q={}".format(matches[0]))
        dl = open("{}-HttpHeaders.txt".format(message.from_user.id), "w")
        dl.write(req.content + "\n=================\n")
        dl.close()
        bot.send_document(message.chat.id, open("{}-HttpHeaders.txt".format(message.from_user.id)))
        bot.send_message(message.chat.id, req.text)
    if re.match("[!/#]?ipinfo (.*)", message.text):
        matches = re.match("[!/#]?ipinfo (.*)", message.text).groups()
        print("{} ip info search for {} From {} ".format(y, matches[0], message.from_user.id))
        req = requests.get("http://ipinfo.io/{}/geo".format(matches[0]))
        js = json.loads(req.text)
        try:
            get_ip = js["ip"]
            get_city = js["city"]
            get_region = js["region"]
            get_country = js["country"]
            get_loc = js["loc"]
            get_loc_method = get_loc.split(',')
            if get_ip and get_city and get_region and get_country and get_loc:
                bot.send_location(message.chat.id, get_loc_method[0], get_loc_method[1])
                bot.send_message(message.chat.id, "🌐ip : `{}`\n🏠city : `{}`\n🔹region : `{}`\n🔹country : `{}`".format(get_ip, get_city, get_region, get_country), parse_mode="markdown")
            elif get_ip and get_city and get_region and get_country:
                bot.send_location(message.chat.id, get_loc_method[0], get_loc_method[1])
                bot.send_message(message.chat.id, "🌐ip : `{}`\n🏠city : `{}`\n🔹region : `{}`\n🔹country : `{}`".format(get_ip, get_city, get_regionget_country), parse_mode="markdown")
            elif get_ip and get_city and get_region:
                bot.send_location(message.chat.id, get_loc_method[0], get_loc_method[1])
                bot.send_message(message.chat.id, "🌐ip : `{}`\n🏠city : `{}`\n🔹region : `{}`".format(get_ip, get_city, get_region), parse_mode="markdown")
            elif get_ip and get_city:
                bot.send_location(message.chat.id, get_loc_method[0], get_loc_method[1])
                bot.send_message(message.chat.id, "🌐ip : `{}`\n🏠city : `{}`".format(get_ip, get_city), parse_mode="markdown")
            elif get_ip and get_country:
                bot.send_location(message.chat.id, get_loc_method[0], get_loc_method[1])
                bot.send_message(message.chat.id, "🌐ip : `{}`\n🔹country : `{}`".format(get_ip, get_country), parse_mode="markdown")
            elif get_ip and get_region:
                bot.send_location(message.chat.id, get_loc_method[0], get_loc_method[1])
                bot.send_message(message.chat.id, "🌐ip : `{}`\n🔹region : `{}`".format(get_ip, get_region), parse_mode="markdown")
            else:
                bot.reply_to(message, "*WTF BRO ? :D*")
        except:
            bot.reply_to(message, "*WTF BRO ? :D*", parse_mode="markdown")
        #dl = open("{}-HttpHeaders.txt".format(message.from_user.id), "w")
        #dl.write(req.content + "\n=================\n")
        #dl.close()
        #bot.send_document(message.chat.id, open("{}-HttpHeaders.txt".format(message.from_user.id)))
        #bot.send_message(message.chat.id, req.text)
    if re.match("[!/#]?tr (.*)", message.text):
        matches = re.match("[!/#]?tr (.*)", message.text).groups()
        print("{} Traceroute search for {} From {} ".format(y, matches[0], message.from_user.id))
        req = requests.get("https://api.hackertarget.com/mtr/?q={}".format(matches[0]), timeout=16)
        dl = open("{}-Traceroute.txt".format(message.from_user.id), "w")
        dl.write(req.content + "\n=================\n")
        dl.close()
        bot.send_document(message.chat.id, open("{}-Traceroute.txt".format(message.from_user.id)))
        bot.send_message(message.chat.id, req.text)
    if message.text == "/start":
        cid = message.chat.id
        markup = types.InlineKeyboardMarkup()
        b = types.InlineKeyboardButton("📍Help",callback_data='help')
        markup.add(b)
        id = message.from_user.id
        try:
            db.execute("INSERT INTO robot(userid, username) VALUES(?,?)", (message.from_user.id, message.from_user.username))
            db.commit()
            bot.send_message(message.chat.id, "*Welcome to Net-Tools Bot*\n`Bot writed by iWhH `\n*Click on help .*", disable_notification=True, reply_markup=markup, parse_mode="markdown")
            bot.send_message(admin, "New User ~> [{}](tg://user?id={})".format(message.from_user.first_name, message.from_user.id), parse_mode="markdown")
            print("{}{} Started the bot :d ".format(b, message.from_user.id))
        except sqlite3.IntegrityError:
            bot.send_message(message.chat.id, "*Welcome to Pentester Bot*\n`Bot writed by iWhH `\n*Click on help .*\n iran-cyber.net", disable_notification=True, reply_markup=markup, parse_mode="markdown")
    if message.from_user.id in admin and message.text == "/stats":
        s = db.execute("SELECT count(userid) FROM robot;")
        for _ in s:
            bot.reply_to(message, "Robot Users ~> `{}`".format(_[0]), parse_mode="markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "help":
        bot.send_message(call.message.chat.id, "1- *Whois Domain*\n `/whois domain.com`\n 2- *Dns Lookup*\n `/lookup domain.com\n` 3- *Zone Transfer*\n `/zone domain.com`\n 4- *Http Headers*\n `/httpheaders domain.com`\n 5- *Ip Information*\n `/ipinfo ip address`\n 6- *Traceroute*\n `/tr domain.com`\n iran-cyber.net",parse_mode="markdown")

bot.polling(True)
