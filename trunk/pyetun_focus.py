import os, sys, pyetun_cfg
e_remote_path=pyetun_cfg.return_remote()

def get_focus():
	fc=os.popen(e_remote_path+" -focus-policy-get").readlines()
	del fc[0]
	fc=fc[:-1]
	fc=fc[0].split(" ")[1]
	
	return fc
	
def set_focus(value):
	os.popen(e_remote_path+" -focus-policy-set "+value)
	
#Get the focus setting policy

def get_setting():
	fc=os.popen(e_remote_path+" -focus-setting-get").readlines()
	del fc[0]
	fc=fc[:-1]
	fc=fc[0].split(" ")[1]
	
	return fc
	
def set_setting(value):
	os.popen(e_remote_path+" -focus-setting-set "+value)
	

#remember focused window while switching desktops

def get_last_focused():
	fc=os.popen(e_remote_path+" -focus-last-focused-per-desktop-get").readlines()
	del fc[0]
	fc=fc[:-1]
	fc=fc[0].split(" ")[1]
	
	return fc
	
def set_last_focused(value):
	value=str(value)
	os.popen(e_remote_path+" -focus-last-focused-per-desktop-set "+value)
	
def get_revert():
	fc=os.popen(e_remote_path+" -focus-revert-on-hide-or-close-get").readlines()
	del fc[0]
	fc=fc[:-1]
	fc=fc[0].split(" ")[1]
	
	return fc

def set_revert(value):
	value=str(value)
	os.popen(e_remote_path+" -focus-revert-on-hide-or-close-set "+value)


def get_maximize():
	maxi=os.popen(e_remote_path+" -maximize-policy-get").readlines()
	del maxi[0]
	maxi=maxi[:-1]
	maxi=maxi[0].split(" ")[1][:-1] #python rocks
	return maxi

def set_maximize(value):
	os.popen(e_remote_path+" -maximize-policy-set "+value)
	
