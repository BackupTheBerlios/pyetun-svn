import os, sys, pyetun_cfg




e_remote_path=pyetun_cfg.return_remote()

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
	extra=pyetun_cfg.return_modpath("extra")
	
	if os.path.exists(extra):
		extra=os.listdir(extra)
		
		
	else:
		print "[E] Can't find extra modules path for E17. To continue.."
		extra=[]
		
	
	return extra

def locate_normal_modules():
	modules_path=pyetun_cfg.return_modpath("normal")
	if os.path.exists(modules_path):
		normal=os.listdir(modules_path)
	
		
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
	

def load_mod(mod):
	os.popen(e_remote_path+" -module-load "+mod)

def unload_mod(mod):
	os.popen(e_remote_path+" -module-unload "+mod)

def enable_mod(mod):
	os.popen(e_remote_path+" -module-enable "+mod)

def disable_mod(mod):
	os.popen(e_remote_path+" -module-disable "+mod)




