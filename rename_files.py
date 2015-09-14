#!/usr/bin/env python

import os
def rename_files():

	# get file names
	file_list=os.listdir("/home/vishal/Downloads/prank/prank")
	print(file_list)

	saved_path=os.getcwd()
	print("the current working directory is:" +saved_path)

	os.chdir("/home/vishal/Downloads/prank/prank")
	
	saved_path=os.getcwd()
	print("the current working directory is:" +saved_path)

	# for each file, rename filenames

	for file_name in file_list:
		os.rename(file_name,file_name.translate(None,"0123456789"))

rename_files()
