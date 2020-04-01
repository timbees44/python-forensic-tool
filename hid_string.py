#!/bin/env/python3

import os
import subprocess
import base64

#Function to iterate through all files in a root directory including files in hidden subdirectories.
def fileiterate(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			full_path = os.path.join(root, file)
			yield full_path

#Assigning the called "fileiterate" function to variable and giving it user input			
file_path_tup = tuple(fileiterate(input("please give path to main directory: ")))

#Function to check the type of file for each file found
def fileinfo(file):
	for i in file_path_tup:
		#function wide variables. 3 are terminal commands, 'f' is to take the name of the file from the path
		st = subprocess.check_output(["strings", i]).decode("utf-8")
		ftype = subprocess.check_output(["file", i]).decode("utf-8")
		f = i.rsplit('/',1)[-1]
		if "HTML" in ftype:
			if f.endswith(".html"):
				print("{} is a HTML file with matching extension".format(f))
			else:
				print("{} is a HTML file with the WRONG extension".format(f))
			hf = open(i, 'r')
			for line in hf:
				if "Comment" in line or "<!" in line or "<tr>" in line or "cdata".upper() in line:
						print("Path to file: " + i)
						print("Line with message: " + line)
						print("\n")
		elif "PNG" in ftype:
			if f.endswith(".png"):
				print("{} is a PNG file with matching extension".format(f))
			else:
				print("{} is a PNG file with the WRONG extension".format(f))
			if "tEXt" in st or "Exif" in st:
				print("Path to file: " + i)
				print("First 100 chars of png: " + st[:100] + "\n" + "last 100 chars of png: " + st[-100:])
			print("\n")
		elif "JPEG" in ftype:
			if f.endswith(".jpg") or f.endswith(".jpeg"):
				print("{} is a JPEG file with matching extension".format(f))
			else:
				print("{} is a JPEG file with the WRONG extension".format(f))
			if "tEXt" in st or "Exif" in st:
				print("Path to file: " + i)
				print("First 100 chars of jpeg: " + st[:100] + "\n" + "last 100 chars of jpeg: " + st[-100:])
			print("\n")
		elif "GIF" in ftype:
			if f.endswith(".gif"):
				print("{} is a GIF file with matching extension".format(f))
			else:
				print("{} is a GIF file with the WRONG extension".format(f))
			print("First 100 chars of gif: " + st[:100] + "\n" + "Last 100 chars of gif: " + st[-100:] + "\n")	
			print("\n")
		elif "Audio file" in ftype:
			if f.endswith(".mp3"):
				print("{} is a MP3 file with matching extension".format(f))
			else:
				print("{} is a MP3 file with the WRONG extension".format(f))
			print("First 100 chars of mp3: " + st[:100] + "\n" + "Last 100 chars of mp3: " + st[-100:] + "\n")
			print("\n")
		elif f.endswith(".java"):
			if "C source" in ftype:
				print("{} is probably a java file")
			else:
				print("{} this is some sort of code file maybe?")
			print("Here is the strings output for the .java file. It should be readable so you can check for secrets")
			print(st)
		elif "Microsoft" in ftype:
			ex = subprocess.check_output(["exiftool", i]).decode("utf-8")
			if f.endswith(".docx"):
				print("{} is a DOCX file with matching extension".format(f))
			else:
				print("{} is a Microsoft file check extension to see what type".format(f))
			print("Check out 'Core Properties Description' in exiftool output below. Looks like hidden stuff can be put here")
			print(ex)
			print("\n")	
		elif "PDF" in ftype:
			ex = subprocess.check_output(["exiftool", i]).decode("utf-8")
			if f.endswith(".pdf"):
				print("{} is a PDF file with matching extension".format(f))
			else:
				print("{} is a PDF file with the WRONG extension".format(f))
			if "Generated" in ex:
				print("Check out 'Generated' in exiftool output below")
				print(ex)
			print("\n")
		else:
			print("{} is a lil funky and you might need to check it out some more because I don't wanna hardcode all file types into this already long script".format(f))
			print("\n")

fileinfo(file_path_tup)
		