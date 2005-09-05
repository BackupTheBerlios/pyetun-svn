import os, sys
e_remote_path="enlightenment_remote"

#define if alt-tab show others desktops
def get_list_other_desktops():
	other=os.popen(e_remote_path+" -winlist-list-show-other-desk-windows-get").readlines()
	del other[0]
	other=other[:-1]
	other[0]=other[0].split(" ")[1][:-1]
	return other

def set_list_other_desktops(value):
	value=str(value)
	os.popen(e_remote_path+" -winlist-list-show-other-desk-windows-set "+value)
#def set_winlist_align():


def get_show_iconified_windows():
	ic=os.popen(e_remote_path+" -winlist-list-show-iconified-get").readlines()
	del ic[0]
	ic=ic[:-1]
	ic[0]=ic[0].split(" ")[1][:-1]
	return ic

def set_show_iconified_windows(value):
	value=str(value)
	os.popen(e_remote_path+" -winlist-list-show-iconified-set "+value)
