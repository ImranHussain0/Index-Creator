# 25/6/21
# Index Creator version 1.0
# Author: I.Hussain
# This program takes a list of stocks and checks which of them are considered undervalued according to the Graham number.
# The result is then written into a file called a seperate file.
# The intention is to create a universe where all the constituents are 'undervalued'
# Graham number: https://www.investopedia.com/terms/g/graham-number.asp
# Formula is:
#   ___________________
# \/ 22.5 x EPS x BVPS
#
# This formuala shows the maximum stock price you should pay. 
#
#  ---------------------------------------------------------------------
# Limitations:
# The lists are created using the *current* data.
# This means that the lists generated are probably not useful for backtesting.
# I am not sure if Yahoo finance has historic fundamental data avaliable or where to obtain alternate data sources (free/cheap). 
#
# ---------------------------------------------------------------------
# Areas that for program improvement:
#   1.) Program is slow so need to look into threading.
#   2.) Add feature to accept arguments instead of having to manually enter filenames in the code.
#   3.) The program currently does not make a list of the non-filtered entries.
#       Currently this needs done manually using the terminal e.g. $ comm -23 index_file.txt filtered.txt > newfile.txt
#   4.) Find a source of historic fundamental data so that backtesting can be improved.
#
# ----------------------------------------------------------------------

import yfinance as yf
import math

with open('russell3000.txt') as temp_file: # Change this to whatever file you want to read from.
  newlist = [line.rstrip('\n') for line in temp_file]

f = open("filtered.txt", "w") # This is the output file. Change if you want. 
for i in newlist:
    try:
        stock = yf.Ticker(i)
        eps = stock.info['trailingEps']
        bvps = stock.info['bookValue']
        if(eps >= 0 and bvps >=0):    
            graham = math.sqrt(22.5 * eps * bvps)
            if(stock.info['previousClose'] < graham):
                f.write(i + "\n")
    except:
        print("An error occured with: " + i)
f.close()