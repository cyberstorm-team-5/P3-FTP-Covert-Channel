# Program 3: FTP Covert Channel
* Authors: Team Chinese (Lane Arnold, Christopher Boquet, Christopher Bouton, Darrell Durousseaux, Clay Fonseca, Rebecca Grantham, Andrew Maurice)
* Class: Cyber Security 2019 (CSC 442)
## About
This repository contains the code and other resources used for the third programming assignment, FTP Covert Channel. The Python code will extract a covert message from the file permissions of a FTP server. It first fetches the file listing and (based on the METHOD variable at the top of the code), will either use the last 7 or all 10 bits of the file permissions to generate and output the covert message.
