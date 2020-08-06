import requests
import os
from datetime import datetime, timedelta
from random import randrange
import smtplib, ssl

# Settings
gmailAddress   = "your_gmail@gmail.com"
gmailPassword  = "your_gmail_password"
emailToText    = "your_mobile_number@text.att.net"

# Product You're Interested In
URL = "https://www.bestbuy.com/site/oculus-quest-all-in-one-vr-gaming-headset-128gb-black/6342915.p?skuId=6342915"


def sendInStockEmail(gmailAddress, gmailPassword, emailToText):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(gmailAddress, gmailPassword)
        message = """\
        Subject: IN STOCK IN STOCK IN STOCK IN STOCK
        
        IN STOCK IN STOCK IN STOCK
        """
        server.sendmail(gmailAddress, emailToText, message)

# Misc Setup
header      = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
               'Cache-Control': 'no-cache'}
timeToCheck = datetime.now() - timedelta(seconds = 1)

# Checking To See if In Stock
while True:
    if datetime.now() > timeToCheck:
        page = requests.get(URL, headers=header, timeout=5)

        # Check if "Sold Out" is Inside The Website
        if "Sold Out" in page.text:
            print("Sold Out =(")
            #os.system('say "OUT OF STOCK"')
        else:
            print("In Stock, Let's GOOOOOOOOOOOOOOOOOO")
            os.system('say "IN STOCK"')
            sendInStockEmail(gmailAddress, gmailPassword, emailToText)

        waitInterval = randrange(6, 15, 1)
        timeToCheck = timeToCheck + timedelta(seconds = waitInterval)
        print("Waiting for %d seconds before trying again..." % waitInterval)
