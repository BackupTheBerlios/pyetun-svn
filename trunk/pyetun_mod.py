import os, sys


extra_modules_path="/usr/lib/enlightenment/modules_extra"
extra_modules_path_local="/usr/local/lib/enlightenment/modules_extra"
modules_path="/usr/lib/enlightenment/modules"
modules_path_local="/usr/local/lib/enlightenment/modules"
e_remote_path="enlightenment_remote"

# check modules (enabled and disabled one) status
def all_loaded_modules():
	list_modules=[] #list with parser modules
	dic={}
	all_mods=os.popen(e_remote_path+" -module-list").readlines()
	all_mods=all_mods[:-1] #remove first and last element of list (useless)
	del all_mods[0]
	
	for i in all_mods:
		mod=i.split(" ")
		dic[mod[1].split('"')[1]]=mod[3][:-1]

	
	return dic

		

def locate_extra_modules():
	if os.path.exists(extra_modules_path):
		extra=os.listdir(extra_modules_path)
		
	elif os.path.exists(extra_modules_path_local):
		extra=os.listdir(extra_modules_path_local)
	
		
	else:
		print "[E] Can't find extra modules path for E17. To continue.."
		extra=[]
		
	
	return extra

def locate_normal_modules():
	if os.path.exists(modules_path):
		normal=os.listdir(modules_path)
		
	elif os.path.exists(modules_path_local):
		normal=os.listdir(modules_path_local)
	
		
	else:
		print "[E] Can't find modules path for E17. To continue.."
		normal=[]
		
	
	return normal


def build_modules_status():
	total=locate_extra_modules()
	total=total+locate_normal_modules()
	
	
	
	mod_all_status=all_loaded_modules()
	temp2=[]


	for l in total:
		if l not in mod_all_status:
			mod_all_status[l]="-1"

	return mod_all_status
	
