from sys import path
import time
import telebot
from telebot import types
import os
from colorama import Fore as cf
from random import randint as rn
from PIL import ImageGrab
#__CMD Note______________________________________________________________#
wel = f""""
    {cf.GREEN} ╦═╗┌─┐┌┬┐┌─┐┌┬┐┌─┐       ╔═╗╔═╗
    {cf.WHITE} ╠╦╝├┤ ││││ │ │ ├┤   ───  ║ ║╚═╗
    {cf.RED} ╩╚═└─┘┴ ┴└─┘ ┴ └─┘       ╚═╝╚═╝    
    {cf.YELLOW}
    {cf.YELLOW} ____________|info|_____________
    {cf.YELLOW}|                               |
    {cf.YELLOW}| Create: Alisa Alikhani (Quad) |
    {cf.YELLOW}| Telegram: @AL13A_7            |
    {cf.YELLOW}| github: github.com/Quad84     |
    {cf.YELLOW}| Made in Iran                  |{cf.LIGHTMAGENTA_EX}
    {cf.YELLOW}|_______________________________|
"""
os.system("cls")
print(wel)
time.sleep(0.01)
#__Connect______________________________________________________________#
TOKEN = "2017514530:AAGDCIro44NT_MI06r0HzQgzzkdU3d6AuxA"
bot = telebot.TeleBot(TOKEN)
#__Class______________________________________________________________#
class data:
    want_s = 0
    want_r = 0
#__GET-SET______________________________________________________________#
def getfile(file_name):
    file = open(file_name,"r+")
    return file.read()  
    file.close()
    
def setfile(file_name,Text):
    file = open(file_name,"a")
    file.write(Text)
    file.close()
#__Key_______________________________________________________________#
def My_Account_Info(user):
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    try:
        bot.send_chat_action(userchatid,"typing")
        print(f"-----\nSend Acc info for {userchatid}\n------")
        bot.send_message(userchatid,f"[1] Your Name: {userfirstname}\n[2] Your ID: {userchatid}\n[3] Your Username: {userusername}")
    except:
        startcmd(user)

def d_info(user):
    userchatid = user.chat.id
    try:
        bot.send_chat_action(userchatid,"typing")
        print(f"-----\nSend Developer info for {userchatid}\n------")
        bot.send_message(userchatid,"Name: Alisa\nFamily: Alikhani\nTelegtam: @AL13A_7")
    except:
        startcmd(user)


def Admins(user):
    admin = getfile("Admin.txt").splitlines()
    userchatid = user.chat.id
    try:
        print(f"-----\nSend Admins info for {userchatid}\n------")
        for adm in admin:
            bot.send_chat_action(userchatid,"typing")
            bot.send_message(userchatid,f"Admins:\n{adm}")
    except:
        startcmd(user)   


def help(user):
    userchatid = user.chat.id
    try:
        bot.send_chat_action(userchatid,"typing")
        print(f"-----\nSend Help for {userchatid}\n------")
        bot.send_message(userchatid,f"/start = Start Bot\n/save [text] = Save a text in database\n/savelist = Show database list")
    except:
        startcmd(user)


def power(user):
    userchatid = user.chat.id
    try:
        markups= types.ReplyKeyboardMarkup()
        key1 = types.KeyboardButton("Shut Down")
        key2 = types.KeyboardButton("Restart")
        key3 = types.KeyboardButton("Home")
        markups.add(key1,key2,key3)
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"Choose a options",reply_markup=markups)
    except:
        startcmd(user)

def screenshot(user):
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    try:
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"Taking Screen Shot ... ")
        print(f"[@] [{userchatid}],[{userfirstname}],[@{userusername}] Took a Screen Shot !")
        makephoto = ImageGrab.grab()
        makephoto.save("ScreenShot.png")
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"Sending ... ")
        photo = open("ScreenShot.png","rb")
        bot.send_chat_action(userchatid,"upload_photo")
        bot.send_photo(userchatid,photo,"ScreenShot")
        photo.close()
        os.remove("ScreenShot.png")
        startcmd(user)
    except:
        startcmd(user)

def shutdown(user):
    data.want_r = 0
    data.want_s = 1
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name

    try:
        print(f"------\n[{userchatid}],[{userfirstname}],[{userusername}] is want ShutDown Sys! ")
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"Are you sure ShutDown System ?\nChoose : /yes or /no")
    except:
        startcmd(user)

def restart(user):
    data.want_r = 1
    data.want_s = 0
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name

    try:
        print(f"------\n[{userchatid}],[{userfirstname}],[{userusername}] is want restart Sys! ")
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"Are you sure Restart System ?\nChoose : /yes or /no")
    except:
        startcmd(user)

def yes_r_s(user):
    userchatid = user.chat.id
    try:
        if data.want_s == 1 and data.want_r == 0:
            bot.send_chat_action(userchatid,"typing")
            bot.send_message(userchatid,"Shutting Down ...")
            data.want_r = 0
            data.want_s = 0
            os.system("Shutdown /S /t 1 /f")
        elif data.want_s == 0 and data.want_r == 1:
            bot.send_chat_action(userchatid,"typing")
            bot.send_message(userchatid,"Restarting ...")
            data.want_r = 0
            data.want_s = 0
            os.system("Shutdown /r /t 120 /f")
        else:
            bot.send_chat_action(userchatid,"typing")
            bot.send_message(userchatid,"Error Process !")
    except:
        startcmd(user)

def no_r_s(user):
    userchatid = user.chat.id
    try:
        data.want_r = 0
        data.want_s = 0
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"Done !")
    except:
        startcmd(user)
        

#__Data______________________________________________________________#


def startcmd(user):
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name

    markups= types.ReplyKeyboardMarkup()
    
    key1 = types.KeyboardButton("Power Options")
    key2 = types.KeyboardButton("Take Screen Shot")
    key3 = types.KeyboardButton("Help CMD")
    key4 = types.KeyboardButton("Admins")
    key5 = types.KeyboardButton("Developer Info")
    key6 = types.KeyboardButton("My Account Info")

    markups.add(key1,key2,key3,key4,key5,key6)
    bot.send_chat_action(userchatid,"typing")
    bot.send_message(userchatid,"""Hello,
Welcome To My Robot
Admin : @Al13A_7
    """,reply_markup=markups)

    print(f"[!] Time : {time.ctime()}")
    print(f"[+] {userfirstname} (@{userusername}) Started Bot !")
    print("-----------------------------------------------")

def savecmd(user):
    usertext = user.text
    userchatid = user.chat.id
    try:
        tex = usertext.replace("/save ","")
        
        rad = rn(11111,99999)
        setfile(f"db/data_{str(rad)}.txt",str(tex))
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"Your message has been received !")
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,f"Your message was saved with ID {str(rad)}")
    except:
        startcmd(user)

        
def savelist(user):
    userchatid = user.chat.id
    try:
        listfile = ""
        for r , d , f in os.walk("db"):
            for filelist in f :
                listfile = listfile + "\n" + str(filelist)
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,f"your file list in Data-base:\n{listfile}")
    except:
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,f"Your folder is full .. Please empty")
        startcmd(user)
        

        



#__Main Panel______________________________________________________________#

@bot.message_handler(content_types=["text"])
def botmain(user):
    admin = getfile("Admin.txt").splitlines()
    memberr = getfile("member.txt").splitlines()
    usertext = user.text
    userchatid = user.chat.id
    userusername = user.chat.username
    userfirstname = user.chat.first_name
    userlastname = user.chat.last_name
    if not str(userchatid) in memberr:
        uci = str(userchatid)+"\n"
        member = setfile("member.txt",uci)
    
    #__Code______________________________________________________________#
    if userusername in admin or str(userchatid) in admin:
        if usertext == "/start" or usertext == "Home":
            startcmd(user)
        elif usertext == "/save":
            bot.send_chat_action(userchatid,"typing")
            bot.send_message(userchatid,"Usage:\n/save [Your Text]")
        elif usertext.startswith("/save "):
            savecmd(user)
        elif usertext == "/savelist":
            savelist(user)
        elif usertext == "My Account Info":
            My_Account_Info(user)
        elif usertext == "Developer Info":
            d_info(user)
        elif usertext == "Admins":
            Admins(user)
        elif usertext == "Help CMD":
            help(user)
        elif usertext == "Power Options":
            power(user)
        elif usertext == "Take Screen Shot":
            screenshot(user)
        elif usertext == "Shut Down":
            shutdown(user)
        elif usertext == "Restart":
            restart(user)
        elif usertext == "/yes":
            yes_r_s(user)
        elif usertext == "/no":
            no_r_s(user)
    else:
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,"You do not have the necessary permissions!")
        bot.send_chat_action(userchatid,"typing")
        bot.send_message(userchatid,f"Your ID : {user.chat.id}")     

#__End______________________________________________________________#
bot.polling(True)



