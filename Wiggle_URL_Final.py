#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Grabs web page content every 45 seconds and searches for "In STOCK".
If found, rings computer 'bell'.
Sends email and SMS message. 

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

# function to search web data for string
def readVar():
    ct = datetime.datetime.now()
    print("current time:-", ct)
    Wiggle_BigAl=("https://www.wiggle.com/ragley-big-al-10-hardtail-bike-2021")
    url = Request(Wiggle_BigAl, headers={'User-Agent': 'Mozilla/5.0'})
    URLTxt=[]
    response = urlopen(url).read()
    URLTxt = response.decode('UTF-8')
    if "Only (" in URLTxt:    # tested with "In STOCK" product - Blue Pig
        print ("In STOCK @ Wiggle!!...") # Yay!!!
        sys.stdout.write('\a\a\a\a\a')
        sys.stdout.flush()
        for x in range(1, 5):
            server = smtplib.SMTP("smtp.gmail.com", 587 )
            server.starttls()
            server.login('MyEmail@gmail.com', 'MyEmailPassword') # Your email address & password
            # Send text message through SMS gateway of destination number
            server.sendmail( 'MyName', 'MyNumber@vtext.com', 'Bike in Stock @ Wiggle!!!!!!' ) # telephone number
            x += 1 # This should send a text 5 times
    else:
        print ("Out of Stock @ Wiggle...") # Boo!!!
    return URLTxt

while True:
    try:
        readVar()
        countMe += 1 # How many times have we pinged this page?
        print (countMe)
        time.sleep(45)  # wait for 45 seconds

    except:
        print("Unexpected error:", sys.exc_info()[0])
        if (urllib.error.URLError, urllib.error.HTTPError):
            print("Server is offline.")
        raise
