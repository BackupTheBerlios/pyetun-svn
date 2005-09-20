import os, sys, pyetun_cfg
e_remote_path=pyetun_cfg.return_remote()

def get_bshade():
	
	bshade=os.popen(e_remote_path+" -border-shade-animate-get").readlines()
	del bshade[0]
	bshade=bshade[:-1]
	
	#get value...
	valo=bshade[0].split(" ")[1][:-1]
	return valo


def get_trans_alg():
	btrans=os.popen(e_remote_path+" -border-shade-transition-get").readlines()
	del btrans[0]
	btrans=btrans[:-1]
	
	#get value...
	val=btrans[0].split(" ")[1][:-1]
	return val

def get_shade_speed():
	bspeed=os.popen(e_remote_path+" -border-shade-speed-get").readlines()
	del bspeed[0]
	bspeed=bspeed[:-1]
	
	#get value...
	val=bspeed[0].split(" ")[1][:-1]
	return val

def set_bshade(value):
	value=str(value)
	os.popen(e_remote_path+" -border-shade-animate-set "+value)

def set_trans_alg(value):
		
	value=str(value)			
	os.popen(e_remote_path+" -border-shade-transition-set "+value)


def set_shade_speed(value):
	value=str(value)
	os.popen(e_remote_path+" -border-shade-speed-set "+value)
