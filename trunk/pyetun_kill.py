import os, sys
e_remote_path="enlightenment_remote"

def get_kill_close_not_possible():
	kill=os.popen(e_remote_path+" -kill-if-close-not-possible-get").readlines()
	kill=kill[:-1]
	del kill[0]
	value=kill[0].split(" ")[1]
	return value[:-1]


# kill by E or by X
def get_kill_process():
	kill=os.popen(e_remote_path+" -kill-process-get").readlines()
	kill=kill[:-1]
	del kill[0]
	value=kill[0].split(" ")[1]
	return value[:-1]

def get_kill_timer_wait():
	kill=os.popen(e_remote_path+" -kill-timer-wait-get").readlines()
	kill=kill[:-1]
	del kill[0]
	value=kill[0].split(" ")[1]
	return value[:-1]

def set_kill_close_not_possible(value):
	value=str(value)
	os.popen(e_remote_path+" -kill-if-close-not-possible-set "+value)

def set_kill_process(value):
	value=str(value)
	os.popen(e_remote_path+" -kill-process-set "+value)

def set_kill_timer_wait(value):
	value=str(value)
	os.popen(e_remote_path+" -kill-timer-wait-set "+value)
