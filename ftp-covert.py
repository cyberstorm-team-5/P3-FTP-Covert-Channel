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


if METHOD == 0:
	inputString = server.dir('7', data.append)
	i = 0
	while i < len(data):
		data[i] = data[i][0:12]
		i=i+1





















else:
	server.dir('10', data.append)
	i = 0
	while i < len(data):
		data[i] = data[i][0:12]
		i=i+1













for line in data:
	print(line)
