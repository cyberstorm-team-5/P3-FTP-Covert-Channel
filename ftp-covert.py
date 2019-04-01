################################################################
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
#              code), will either use the last 7 or all 10 bits of the file
#              permissions to generate and output the covert message.
################################################################
import ftplib
###############################################################

METHOD = 1
#all of our data is stored in this list
data = []

###############################################################
server = ftplib.FTP()
server.connect('www.jeangourd.com')
server.login('anonymous')

#process input as a sequence of 7- or 8-bit ascii code to convert to a readable string
def convertASCII(binaryInput, binaryLength):
	
	finalString = ""
	
	#loop through indexes such that i = the 0th bit in every sequence of numBits
	#(7 or 8) bits in the binaryInput
	for i in range(0, binaryLength-(6), 7):

		#get the ASCII number for the bits
		num = int(binaryInput[i:i+7], 2)

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



if METHOD == 0:
	server.dir('7', data.append)
	i = 0
	while i < len(data):
		data[i] = data[i][0:10]
		i=i+1

	string = ''
	
		
###########################################################################################################################


	for line in data:
		if line [:3] == ('---'):
			for letter in line[3:]:
				if letter ==  ('-'):
					string += "0"

				else:
					string += "1"

	convertASCII(string, len(string))
				

	


###########################################################################################################################              

 













# implementation fro 10 | CDB


else:
	server.dir('10', data.append)
	i = 0
	while i < len(data):
		data[i] = data[i][0:10]
		i=i+1

	string = ''

	for line in data:
		for letter in line:
			if letter ==  ('-'):
				string += "0"

			else:
				string += "1"

	convertASCII(string, len(string))


############################################################################################################################


#for line in data:
	#print(line)
