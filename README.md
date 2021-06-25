# 25/6/21
# index creator version 1.0
# author: i.hussain
# this program takes a list of stocks and checks which of them are considered undervalued according to the graham number.
# the result is then written into a file called a seperate file.
# the intention is to create a universe where all the constituents are 'undervalued'
# graham number: https://www.investopedia.com/terms/g/graham-number.asp
# formula is:
#   ___________________
# \/ 22.5 x eps x bvps
#
# this formuala shows the maximum stock price you should pay. 
#
#  ---------------------------------------------------------------------
# limitations:
# the lists are created using the *current* data.
# this means that the lists generated are probably not useful for backtesting.
# i am not sure if yahoo finance has historic fundamental data avaliable or where to obtain alternate data sources (free/cheap). 
#
# ---------------------------------------------------------------------
# areas that for program improvement:
#   1.) program is slow so need to look into threading.
#   2.) add feature to accept arguments instead of having to manually enter filenames in the code.
#   3.) the program currently does not make a list of the non-filtered entries.
#       currently this needs done manually using the terminal e.g. $ comm -23 index_file.txt filtered.txt > newfile.txt
#   4.) find a source of historic fundamental data so that backtesting can be improved.
#
# ----------------------------------------------------------------------# Index-Creator
