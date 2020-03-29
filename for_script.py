#!/bin/env/python3

import os
import subprocess
import glob

def fsearch(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			full_path = os.path.join(root, file)
			ftype = str(subprocess.check_output(["file", full_path]))
			
			#html querying
			if "HTML" in ftype:
				hf = open(full_path, 'r')
				for line in hf:
					if "Comment" in line:
						print("\nPath to file: " + full_path)
						print("File name: " + file)
						print("Line of file output: " + line)
					if "<!--" in line:
						print("\nPath to file: " + full_path)
						print("File name: " + file)
						print("Line of file output: " + line)
				if full_path.endswith(".html"):
					print(file + " File extension matches file type. This is an HTML file\n")
				else:
					print(file + " File extension and file type DO NOT MATCH, check file type!!!\n")

			#media file querying
			mf = str(subprocess.check_output(["strings", full_path]))
			if "PNG image data" in ftype:
				print("\n" + file + ": This is a PNG file, does it match extension (.png)?")
				if "tEXt" in mf:
					print("\nPath to file: " + full_path)
					print("File name: " + file)
					print("First 100 chars of png: " + mf[:100] + "\n" + "last 50 chars of png: " + mf[-50:])

			if "JPEG image data" in ftype and "Exif" in mf:
				print("\nPath to file: " + full_path)
				print("File Name: " + file)
				print(file + ": is a JPEG file, does it match extension (.jpg)?")
				print("First 100 chars of jpeg: " + mf[:100] + "\n" + "Last 50 chars of jpeg: " + mf[-50:] + "\n")

			if "GIF image data" in ftype and "GIF" in mf:
				print("\nPath to file: " + full_path)
				print("File Name: " + file)
				print(file + ": is a GIF file, does it match extension (.gif)?")
				print("First 100 chars of gif: " + mf[:100] + "\n" + "Last 50 chars of gif: " + mf[-50:] + "\n")
				
			if "Audio file" in ftype and "TOPE" in mf:	
				print("\nPath to file: " + full_path)
				print("File Name: " + file)
				print(file + ": is a MP3 file, does it match extension (.mp3)?")
				print("First 100 chars of mp3: " + mf[:100] + "\n" + "Last 50 chars of mp3: " + mf[-50:] + "\n")	

			else:
				print("This file ({}) is different. You'll have to manually check it. Soz :(".format(file))
				print("Here is the file path: " + full_path)

fsearch(input("please give path to main directory: "))