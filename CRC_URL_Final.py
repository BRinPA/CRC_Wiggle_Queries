#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Version 4 created on Sun Jul 18 08:45:37 2021
@author: Bill R. 
"""
Original version created on Thu Apr  8 18:46:49 2021
1. Search for 'in stock' status for specific frame size;
2. Parse the 'Out of Stock' text from HTML;
3. Figure out SMS texting of status.
Grabs web page content every 45 seconds and searches for stock status of large bike.
If found, rings computer 'bell' 5 times and sends a text message to phone, 5 times.
Will run until you stop it or an exception is thrown.

Note: You will most likely need to make security changes to your gmail account
if you use that email platform.  
See https://support.google.com/mail/thread/5621336/bad-credentials-using-gmail-smtp?hl=en
Test enabling “Access for less secure apps” (which just means the client/app doesn’t use 
OAuth 2.0 - https://oauth.net/2/) for the account you are trying to access.  
It's found in the account settings on the Security tab, Account permissions 
(not available to accounts with 2-step verification enabled):
https://support.google.com/accounts/answer/6010255?hl=en

"""

# Importing libraries
import time, datetime
import sys
import urllib
from urllib.request import urlopen, Request
import smtplib
countMe=0

# function to search web data for string and send SMS text
def parseURL():
    # Set some variables 
    ct = datetime.datetime.now()
    keyword = ('"FramesSize":"L"')
    inventoryStatus=[]
    URLTxt=[]
    newText=()
    CRC_BigAl=("https://www.chainreactioncycles.com/us/en/ragley-big-al-1-0-hardtail-bike-2021/rp-prod197459?_requestid=1517478") 
    url = Request(CRC_BigAl, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(url).read()
    URLTxt = response.decode('UTF-8')
    # Get some data
    before_keyword, keyword, after_keyword = URLTxt.partition(keyword)
    newText = after_keyword.split("inventoryStatus",1)[1] 
    inventoryStatus = newText[3:15]
    print("current time:-", ct)
    if inventoryStatus=="Out of Stock" :
        print ('"' + inventoryStatus + '"' + " @ CRC")  #Boo!!
    else:
        x=1
        print ('"' + inventoryStatus + '"' + " @ CRC!!!!!") # Yay!!!
        sys.stdout.write('\a\a\a\a\a')
        sys.stdout.flush()
        for x in range(1, 5):
            server = smtplib.SMTP("smtp.gmail.com", 587 )
            server.starttls()
            server.login('MyEmailAddress@gmail.com', 'MyEmailPassword' ) # Your email address & password
            # Send text message through SMS gateway of destination number
            server.sendmail( 'MyName', 'MyNumber@vtext.com', 'Bike in Stock @ CRC!!!!!!' ) # telephone number
            x += 1 # This should send a text 5 times
    return None

while True:
    try:
        parseURL() # Do some work...
        countMe += 1 # How many times have we pinged this page?
        print (countMe)
        time.sleep(45)  # wait 45 seconds. 
    except: # Print some errors here
        print("Unexpected error:", sys.exc_info()[0])
        if (urllib.error.URLError, urllib.error.HTTPError):
            print("Server is offline.")
        raise
