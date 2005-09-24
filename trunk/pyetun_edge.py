import os, sys, pyetun_cfg
e_remote_path=pyetun_cfg.return_remote()

def get_edge():
	edge=os.popen(e_remote_path+" -edge-flip-get").readlines()
	del edge[0]
	edge=edge[:-1]
	
	ed=edge[0].split(" ")[1][:-1] #python rocks
	return ed

def set_edge(value):
	value=str(value)
	os.popen(e_remote_path+" -edge-flip-set "+value)

def get_edge_timeout():
	edge2=os.popen(e_remote_path+" -edge-flip-timeout-get").readlines()
	del edge2[0]
	edge2=edge2[:-1]
	ed2=edge2[0].split(" ")[1][:-1] #python rocks
	return ed2

def set_edge_timeout(value):
	value=str(value)
	os.popen(e_remote_path+" -edge-flip-timeout-set "+value)

