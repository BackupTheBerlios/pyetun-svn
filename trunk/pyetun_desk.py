import os, sys
e_remote_path="enlightenment_remote"

def check_desktop_names():
	dic={}
	des=os.popen(e_remote_path+" -desktop-name-list").readlines()
	des=des[:-1]
	del des[0]
	
	des2=[]
	if des==[]:
		print "Ok, No specified names in virtual desktops.."
	
	else:
		for index, i in enumerate(des):
			x=i.split("=")
			r=i.split(" ")
			dic[x[-1][:-1]]=r[4]+" "+r[5]
		
	return dic



def add_des_name(x,y,name):
	#FIXME : container=0 and zone=0...
	os.popen(e_remote_path+" -desktop-name-add 0 0 "+x+" "+y+" "+name)

def rm_des_name(x,y,name):
	#FIXME : container=0 and zone=0...
	os.popen(e_remote_path+" -desktop-name-del 0 0 "+x+" "+y+" "+name)
