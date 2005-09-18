import os, sys, pyetun_cfg
e_remote_path=pyetun_cfg.return_remote()

def get_all_fonts():
	fonts2=[]
	fonts=os.popen(e_remote_path+" -font-available-list").readlines()
	del fonts[0]
	fonts=fonts[:-1]

	for i in fonts:
		fonts2.append(i.split(" ")[1].split('"')[1])
	
	return fonts2

def get_fallback_fonts():
	fonts2=[]
	fonts=os.popen(e_remote_path+" -font-fallback-list").readlines()
	del fonts[0]
	fonts=fonts[:-1]

	for i in fonts:
		fonts2.append(i.split(" ")[1].split('"')[1])
	
	return fonts2

def get_text_classes():
	clas2=[]
	clas=os.popen(e_remote_path+" -font-default-list").readlines()
	del clas[0]
	clas=clas[:-1]
	for i in clas:
		v=i.split(" ")
		clas2.append(v[2]+" "+v[3]+" "+v[4][:-1])

	return clas2


def set_font_default(t_class,f_name,f_size):
	f_size=str(f_size)
	os.popen(e_remote_path+" -font-default-set "+t_class+" "+f_name+" "+f_size)

def apply_font():
	os.popen(e_remote_path+" -font-apply")

