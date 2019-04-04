#!/usr/bin/env python2.7
################################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 4-4-2019
# Github Repo: https://github.com/cyberstorm-team-5/P3-FTP-Covert-Channel-Team-Chinese
# Description: FTP folder list
#              The Python code will display the contents of a given folder


################################################################################
import ftplib
################################################################################

#global var for the string of the FTP server to connect to
SERVER = 'www.jeangourd.com'

#data retrieved from server is stored here
data = []

DIR = ''

################################################################################

#process input as a sequence of 7- or 8-bit ascii code to convert to a readable string
#(NOTE: function retrieved from our P1: Binary Decoder Program)

#####################################MAIN#######################################
	
#setup connection to server
server = ftplib.FTP()
server.connect(SERVER)
server.login('anonymous')
while True:
	files = []
	server.dir(DIR, files.append)
	print "\n".join(files)
	DIR = raw_input("Specify a folder path to list")



################################################################################