import os, sys, pyetun_cfg
e_remote_path=pyetun_cfg.return_remote()

def get_lang_list():
	list2=[]
	lista=os.popen(e_remote_path+" -lang-list").readlines()
	del lista[0]
	#del lista[1]
	lista=lista[:-1]
	del lista[0]
	
	for i in lista:
		val=i.split(" ")[1]
		val2=val.split('"')[1]
		list2.append(val2)
	
	return list2

def current_lang():
	lista=os.popen(e_remote_path+" -lang-get").readlines()
	del lista[0]
	#del lista[1]
	lista=lista[:-1]

	current=lista[0].split(" ")[1][:-1]	
	return current

def set_lang(lang_name):
	os.popen(e_remote_path+" -lang-set "+lang_name)
