import os, sys
e_remote_path="enlightenment_remote"

def get_all_keys():
	keys=os.popen(e_remote_path+" -binding-key-list").readlines()
	del keys[0]
	keys=keys[:-1]

	return keys



def get_KEYS():
	
	keys=get_all_keys()
	keys2=[]
	
	for j in keys:
		x=j.split("KEY=")
		y=x[1].split(" ")[0]
		keys2.append(y)
	
	return keys2

def get_MODIFIERS():
	keys=get_all_keys()
	keys3=[]
	
	for j in keys:
		x=j.split("MODIFIERS=")
		y=x[1].split(" ")[0]
		keys3.append(y)
	
	return keys3

def get_ACTION():
	keys=get_all_keys()
	keys4=[]
	
	for j in keys:
		x=j.split("ACTION=")
		y=x[1].split(" ")[0]
		keys4.append(y)
	
	return keys4


def get_PARAMS():
	keys=get_all_keys()
	keys5=[]
	
	for j in keys:
		x=j.split("PARAMS=")
		
		keys5.append(x[1])
	
	return keys5

# NOTE:
# Context is ALLWAYS: ANY
# ANY_MOD: 0

def add_key(key,mod,action,param):
	os.popen(e_remote_path+" -binding-key-add ANY "+key+" "+mod+" 0 "+action+" "+param)

def del_key(key,mod,action,param):
	os.popen(e_remote_path+" -binding-key-del ANY "+key+" "+mod+" 0 "+action+" "+param)
