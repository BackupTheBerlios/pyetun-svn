import os, sys
e_remote_path="enlightenment_remote"

def get_font_cache():

	font=os.popen(e_remote_path+" -font-cache-get").readlines()
	del font[0]
	font=font[:-1]
	font[0]=font[0].split(" ")[1][:-1]
	return font

def get_image_cache():

	img=os.popen(e_remote_path+" -image-cache-get").readlines()
	del img[0]
	img=img[:-1]
	img[0]=img[0].split(" ")[1][:-1]
	return img

def set_font_cache(value):
	os.popen(e_remote_path+" -font-cache-set "+value)

def set_image_cache(value):
	os.popen(e_remote_path+" -image-cache-set "+value)
