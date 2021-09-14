# CRC_Wiggle_Queries
Code to query "in stock" status of bikes from both CRC and Wiggle web pages. 

Background: I wanted to order a bike from Chain Reaction Cycles (CRC) (https://www.chainreactioncycles.com/us/en), which is owned by Wiggle (https://www.wiggle.com).  Because of current supply chain challenges, the stock of bikes is very sporatic.
CRC and Wiggle both allow for email alerts which will send an email if/when a bike comes back into stock, but there is a problem - latency.
From experience, I learned that the latency between the time the email arrives in my in-box, and I noticed it, and responded, the bike I wanted
was no longer in stock.  Very frustrating. 

This made me want to create alternative methods for becoming aware when bikes come back in stock and get a jump on a notification. 
I spent some time looking at the Wiggle and CRC web page code for the specific bike I wanted (Ragley Big Al 1.0) and was able to capture the differences
in the code between when they were out of stock (most of the time) and in stock (almost never). 
I took some time and wrote two sets of python and shell scripts which run every 45 seconds, parsing the web code, and looking for a change in stock.
I wanted to make these available to the wider community as a starting point. 

Note: This code was thrown together in a weekend, with some beer, so it's not bullet-proof. I welcome changes and updates. 

runCRC.sh - Driver shell script which calls 'CRC_URL_Final.py' and runs it forever, restarting if it dies.

CRC_URL_Final.py - Code to call CRC url for Ragley Big Al 1.0 and parse for in stock status, sending both an email and SMS text. 

runWiggle.sh - Driver shell script which calls 'Wiggle_URL_Final.py' and runs it forever, restarting if it dies.

Wiggle_URL_Final.py - Code to call Wiggle url for Ragley Big Al 1.0 and parse for in stock status, sending both an email and SMS text. 

Important items:
The python code will send an in stock email to your email address and it will send you a text, if your SMS provider enables this.
I have Verizon as my mobile provider, so this worked for me. 
1. server.login('MyEmail@gmail.com', 'MyEmailPassword' ) # Your email address & password
2.  server.sendmail( 'Name', 'MyNumber@vtext.com', 'Bike in Stock @ CRC!!!!!!' ) # telephone number
I have included some notes and references in the code to help debug this for you. 
Also, the html code between these two pages (CRC and Wiggle) is NOT the same, so there is a difference in how it's parsed. 

How to run: On my Mac, in a terminal, ./runWiggle.sh and ./runCRC.sh 
You may need to change the bit on the shell script as +x for it to run.
I have not tested this on Windows or Linux, so your mileage may vary. 

Lastly, I wrote this in python 3.8.8 using Anaconda and the Spyder IDE. 
Have fun!!
