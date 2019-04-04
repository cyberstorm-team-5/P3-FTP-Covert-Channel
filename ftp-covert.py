#!/usr/bin/env python2.7
################################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 4-5-2019
# Github Repo: https://github.com/cyberstorm-team-5/P3-FTP-Covert-Channel-Team-Chinese
# Description: Program 3: FTP (storage) Covert Channel
#              The Python code will extract a covert message from the
#              file permissions of a FTP server. It first fetches the file
#              listing and (based on the METHOD variable at the top of the
#              code), will either use the last 7 or all 10 bits (METHOD = 0
#              or 1, respectively) of the file permissions to generate
#              and output the covert message. The server and directory within the
#              server can be specified using the global variables SERVER and DIR, as
#              well as whether to convert binary with 7- or 8-bit ASCII (NUMBITS).

################################################################################
import ftplib
################################################################################

#global var to select number of bits to use for converting ASCII (int 7 or 8)
NUMBITS = 7

#global var to select mode (0 (7-bit) or 1 (10-bit))
METHOD = 0

#global var for the string of the FTP server to connect to
SERVER = 'www.jeangourd.com'

#global var for directory within server to retrieve file permissions info from
DIR = ''

#adjusts the DIR based on the METHOD
if (METHOD == 0):
	DIR = '7'
else:
	DIR = '10'

#data retrieved from server is stored here
data = []

################################################################################

#process input as a sequence of 7- or 8-bit ascii code to convert to a readable string
#(NOTE: function retrieved from our P1: Binary Decoder Program)
def convertASCII(binaryInput, binaryLength):
	
	finalString = ""
	
	#loop through indexes such that i = the 0th bit in every sequence of numBits
	#(7 or 8) bits in the binaryInput
	for i in range(0, binaryLength-(NUMBITS-1), NUMBITS):

		#get the ASCII number for the bits
		num = int(binaryInput[i:i+NUMBITS], 2)

		#check if the num will produce a backspace (ASCII 8)
		if(num == 8):
			#remove the trailing character from the string
			finalString = finalString[:-1]
		   
		else:
			#convert the 7 or 8 bits into an integer form base 2, then use chr
			#to convert the integer into the equivalent ASCII character
			finalString += chr(num)
		
	print(finalString)
	return


#append all permissions data in the DIR directory in the server to the data array
def retrieveData():
	
	server.dir(DIR, data.append)

	#loop through each line of data retrieved (1 line/index of the data array)
	for i in range(len(data)):

		#remove all but the first 10 characters of each line (only want
		#the permissions info)
		data[i] = data[i][0:10]
		i=i+1


#generate a binary string based on the permissions in the data array
def genString():
	
	string = ''

	#based on METHOD specified, process data accordingly
	if (METHOD == 0):

		#7-bit method
		for line in data:

			#only process lines of data that have all '-' for
			#the first 3 characters
			if line [:3] == ('---'):

				#for the remaining 7-bits, append a 0 to the
				#string for any '-', else 1
				for letter in line[3:]:
					if (letter ==  ('-')):
						string += "0"
					else:
						string += "1"

	else:

		#10-bit method
		for line in data:

			#append 0 to string for any '-', else 1
			for letter in line:
				if (letter ==  ('-')):
					string += "0"
				else:
					string += "1"

	#output the 7-bit ASCII version of the binary string
	convertASCII(string, len(string))
	
#####################################MAIN#######################################
	
#setup connection to server
server = ftplib.FTP()
server.connect(SERVER)
server.login('anonymous')

#retrieve the permissions data from server
retrieveData()

#generate the binary string and print the 7-bit ASCII version
genString()

################################################################################
