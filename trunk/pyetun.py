#!/usr/bin/env python 
import os, sys


# Config file Object return



def console():
	try:
		print """
Python E17 tunner script (tm) * 
1 ) E17 modules
2 ) Desktop names
3 ) Border shade options
4 ) Languages
5 ) Winlist settings (alt+tab)
6 ) E17 cache (font and image)
7 ) Windows kill options
8 ) Keybindings 
0 ) Exit
"""
		rsp = raw_input ("Option: ")
		if rsp == "1":
			e17_modules()
		elif rsp == "2":
			e17_name_desktop()
		elif rsp == "3":
			e17_bshade()
		elif rsp =="4":
			e17_languages()
		elif rsp=="5":
			e17_winlist()
		elif rsp=="6":
			e17_cache()
		elif rsp=="7":
			e17_kill()
		elif rsp=="8":
			e17_keys()
		elif rsp =="0":
			print "Thanks for using E17 tunner. You're now a rice boy.. ;)\n"
			sys.exit()
	
	except KeyboardInterrupt:
		print "Thanks for using E17 tunner. You're now a rice boy.. ;)\n"
		sys.exit()

def bold(s): 
	return "\033[1m%s\033[0m" % s



#handle with e17 modules
def e17_modules():
	try:
		
		import pyetun_mod
		
		
		modules=pyetun_mod.build_modules_status()
		#let's list all modules  and status..
		for i in modules:
			if modules[i] == "1":	
				print i,
				print " [ status: enabled,loaded ]"
			elif modules[i] == "0":
				print i,
				print " [ status: disabled,loaded ]"
			elif modules[i] == "-1":
				print i,
				print "[ status: disabled,unloaded ]"
		
		print "> Options: "
		print bold("[e]nable <module_name>") 
		print bold("[d]isable <module_name>")
		print bold("[l]oad <module_name>")
		print bold("[u]nload <module_name>")
		print "> CTRL+C - Main Menu"
	
		value=raw_input("Option: ")
		if value == "s":
			status()
			return e17_modules()
	
		else:
			while 1:
				try:
					x=value.split(" ")
					let=x[0]
					mod=x[1]
				except IndexError:
					print "[error]: m00, wrong wrong wrong! ;-)"
					return e17_modules()
	
				if mod in modules:
					if let=="l":
						if modules[mod] == "1" or modules[mod] == "0":
							print bold("[ *] Module already loaded!")
							return e17_modules()
	
						if modules[mod] == "-1" :
							load_mod(mod)
							print bold("[M ] "+mod+" loaded!")
							return e17_modules()
					
					elif let=="u":
						if modules[mod] == "-1":
							print bold("[ *] Module already unabled!")
							return e17_modules()
	
						if modules[mod] == "1" or modules[mod] == "0" :
							unload_mod(mod)
							print bold("[M ] "+mod+" unloaded!")
							return e17_modules()
					
					elif let == "e":
						if modules[mod] == "1":
							print bold("[ *] Module already enabled!")
							return e17_modules()
	
						if modules[mod] == "-1":
							load_mod(mod)
							enable_mod(mod)
							print bold("[M ] "+mod+" loaded and enabled!")
							return e17_modules()
	
						if modules[mod] == "0" :
							enable_mod(mod)
							
							print bold("[M ] "+mod+" enabled!")
							return e17_modules()
		
					elif let == "d":
						if modules[mod] == "0":
							print bold("[ *] Module already disabled!")
							return e17_modules()
	
						if modules[mod] == "1":
							disable_mod(mod)
							print bold("[M ] "+mod+" disabled!")
							return e17_modules()
					
					else:
						print bold("[error] m000 wrong option!")
						return e17_modules()

				else:
					print bold("[error] m00dule not found! Check the list..")
					return e17_modules()

	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()


def e17_name_desktop():
	try:
		import pyetun_desk
		des_names=pyetun_desk.check_desktop_names()
		#let's print modules names..
		print "Desktop names list: "
		for i in des_names:
			print bold("* desk_name:"),i,
			print bold(">"), des_names[i]

		print "> Options: "
		print bold("[a]dd <desk_x> <desk_y> <desk_name> ") 
		print bold("[d]elete <desk_x> <desk_y> <desk_name>")
		print "> CTRL+C - Main Menu"
		
		value=raw_input("Option: ")
		while 1:
			try:
				opt, x, y, name = value.split(None,3)
				
			except IndexError:
				print "[error]: m00, wrong wrong wrong! ;-)"
				return e17_name_desktop()
			
			#options
			if opt=="a":
				pyetun_desk.add_des_name(x,y,name)
				print "Desktop ",x,"",y,"renamed to ",
				print bold(name)
				return e17_name_desktop()
			
			elif opt=="d" and name in des_names:
				pyetun_desk.rm_des_name(x,y,name)
				print "Desktop",x,"",y,">",
				print bold(name),
				print "deleted to original value.."
				return e17_name_desktop()
			
			else:
					print bold("[error] m000 wrong option!")
					e17_name_desktop()
	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()

def e17_bshade():
	import pyetun_bshade
	try:
		print "Border Shade Options:"
		print bold("* "),
		# border shade animate
		if pyetun_bshade.get_bshade() == "1":
			print "Border shade animation - ENABLED (1)"
		elif pyetun_bshade.get_bshade() == "0":
			print "Border shade animation - DISABLED (0)"
		#border shade transition
		print bold("* "),
		print "Shading animation algorithm -",
		print pyetun_bshade.get_trans_alg()
		#shading speed (pixels/sec)
		print bold("* "),
		print "Shading Speed -",
		print pyetun_bshade.get_shade_speed(),
		print "pixels/sec"
		
		#Options
		print "> Options: "
		print bold("[b]order shade animation <0/1>") 
		print bold("[a]nimation algorithm <value between 0 and 3>")
		print bold("[s]hading speed <value>")
		print "> CTRL+C - Main Menu"
		
		valu=raw_input("Option: ")
		while 1:
			try:
				t=valu.split(" ")
				opt=t[0]
				value=t[1]
			except IndexError:
				print "[error]: m00, wrong wrong wrong! ;-)"
				e17_bshade()

			if opt=="b":
				pyetun_bshade.set_bshade(value)
				print bold("Done!")
				e17_bshade()
			elif opt=="a":
				pyetun_bshade.set_trans_alg(value)
				print bold("Done!")
				e17_bshade()
			elif opt=="s":
				pyetun_bshade.set_shade_speed(value)
				print bold("Done!")
				e17_bshade()
			else:
				print bold("[error] m000 wrong option!")
				e17_bshade()

	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()


def e17_languages():
	try:
		import pyetun_lang
		all=pyetun_lang.get_lang_list()
		current=pyetun_lang.current_lang()
		print "Available Languagues: "
		for i in all:
			print bold("* "),
			print i
		print "Current System Language: ",
		if current=='""':
			print "None (Default)"
		else:
			current=current.split('"')[1]
			print current
		
		print "> Options: "
		print bold("[s]et language <lang_name>")
		print "> CTRL+C - Main Menu"
	
		valu=raw_input("Option: ")
		while 1:
			try:
				t=valu.split(" ")
				opt=t[0]
				value=t[1]
			except IndexError:
				print "[error]: m00, wrong wrong wrong! ;-)"
				e17_languages()

			if opt=="s":
			
				if value in all:  
					pyetun_lang.set_lang(value) 
					e17_languages()
				else:
					print bold("[error]: This language is not present. Check the list..")
					e17_languages()
			else:
				print bold("[error] m000 wrong option!")
				e17_languages()

	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()



def e17_winlist():
	try:
		import pyetun_winlist
		other=pyetun_winlist.get_list_other_desktops()
		icon=pyetun_winlist.get_show_iconified_windows()
		jump=pyetun_winlist.get_jump_desk()
		

		print "Alt-tab Settings:"
		if other[0]=="POLICY=1":
			print "List other desktops windows: ENABLED (1)"
		elif other[0]=="POLICY=0":
		  	print "List other desktops windows: DISABLED (0)"
		 
		if icon[0]=="POLICY=1":
			print "Show iconified windows: TRUE (1)"
		elif icon[0]=="POLICY=0":
			print "Show iconified windows: FALSE (0)"
		

		if jump[0]=="POLICY=1":
			print "Jump to desktops while selecting: TRUE (1)"
			
		elif jump[0]=="POLICY=0":
			print "Jump to desktops while selecting: FALSE (0)"
			if other[0]=="POLICY=0":
				print bold(" |> NOTE:"),
				print "You need ENABLE [l]ist other desktop windows to use this option.."

		print "> Options: "
		print bold("[l]ist other desktop windows <0 or 1>")
		print bold("[s]how iconified windows <0 or 1>")
		print bold("[j]ump to desktops while selecting <0 or 1>")
		print "> CTRL+C - Main Menu"
	
		valu=raw_input("Option: ")
		while 1:
			try:
				t=valu.split(" ")
				opt=t[0]
				value=t[1]
			except IndexError:
				print "[error]: m00, wrong wrong wrong! ;-)"
				e17_winlist()
			
			value=int(value)
			
			if opt=="l":
				
				if value>=0 and value<=1:
					pyetun_winlist.set_list_other_desktops(value)
					print bold("Done!")
					e17_winlist()
				else:
					print bold("[error]: Value between 0 and 1")
					e17_winlist()
			
			elif opt=="s":
				if value>=0 and value<=1:
					pyetun_winlist.set_show_iconified_windows(value)
					print bold("Done!")
					e17_winlist()
			
			elif opt=="j":
				if value>=0 and value<=1:
					pyetun_winlist.set_jump_desk(value)
					print bold("Done!")
					e17_winlist()
				else:
					print bold("[error]: Value between 0 and 1")
					e17_winlist()
			else:
				print bold("[error] m000 wrong option!")
				e17_winlist()
			

	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()


def e17_cache():

	try:
		import pyetun_cache
		font=pyetun_cache.get_font_cache()
		img=pyetun_cache.get_image_cache()
		print "Cache values:"
		print "Font: ",font[0],"Kb  [default: 512Kb]"
		print "Image:",img[0], "Kb  [default: 4096Kb]"
		
		print "> Options: "
		print bold("[f]ont size cache <Kb>")
		print bold("[i]mage size cache <Kb>")
		
		print "> CTRL+C - Main Menu"
	
		valu=raw_input("Option: ")
		while 1:
			try:
				t=valu.split(" ")
				opt=t[0]
				value=t[1]
			except IndexError:
				print "[error]: m00, wrong wrong wrong! ;-)"
				e17_cache()
			
			if opt=="f":
				pyetun_cache.set_font_cache(value)
				print bold("Done!")
				e17_cache()
			elif opt=="i":
				pyetun_cache.set_image_cache(value)
				print bold("Done!")
				e17_cache()
		 	 
			else:
				print bold("[error] m000 wrong option!")
				e17_cache()

		 
	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()



def e17_kill():
	try:
		import pyetun_kill
		possible=pyetun_kill.get_kill_close_not_possible()
		kill=pyetun_kill.get_kill_process()
		timer=pyetun_kill.get_kill_timer_wait()

		print "E17 Windows kill Options:"
		
		if possible=="KILL=1":
			print "Kill when close window is not possible: ENABLED (1)"
		else:
			print "Kill when close window is not possible: DISABLED (0)"
		
		if kill=="KILL=1":
			print "Kill process via E: ENABLED (1)"
		else:
			print "Kill process via E : DISABLED (0) (via X Window System)"
		
		print "Interval to wait before killing client: ",timer, "sec"

		print "> Options: "
		print bold("[k]ill when close not possible <0/1>") 
		print bold("[e]nlightenment kill process <0/1>")
		print bold("[s]et interval before killing <value in seconds>")
		print "> CTRL+C - Main Menu"
		valu=raw_input("Option: ")
		while 1:
			try:
				t=valu.split(" ")
				opt=t[0]
				value=t[1]
			except IndexError:
				print "[error]: m00, wrong wrong wrong! ;-)"
				e17_winlist()
			
			value=float(value)
			
			if opt=="k":
				
				if value>=0 and value<=1:
					pyetun_kill.set_kill_close_not_possible(value)
					print bold("Done!")
					e17_kill()
				else:
					print bold("[error]: Value between 0 and 1")
					e17_kill()
			
			elif opt=="e":
				if value>=0 and value<=1:
					pyetun_kill.set_kill_process(value)
					print bold("Done!")
					e17_kill()
			
				else:
					print bold("[error]: Value between 0 and 1")
					e17_winlist()


			elif opt=="s":
				pyetun_kill.set_kill_timer_wait(value)
				print bold("Done!")
				e17_kill()

			else:
				print bold("[error] m000 wrong option!")
				e17_kill()
			

	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()

def e17_keys():
	try:
		import pyetun_keys
		keys=pyetun_keys.get_KEYS()
		mod=pyetun_keys.get_MODIFIERS()
		action=pyetun_keys.get_ACTION()
		par=pyetun_keys.get_PARAMS()
		
		
		for index,i in enumerate(keys):
			print bold("[MODIFIER+KEY] "),
			print mod[index],"+",i,
			print bold(" [ACTION] "),
			print action[index],
			print bold(" [ACTION PARAMS] "),
			print par[index][:-1]

		print "> Options: "
		print bold("[a]dd keybinding  <modifier+key> <action> <action_params>") 
		print bold("[d]elete keybinding <modifier+key> <action> <action_params>")
		print "EXAMPLE: a ALT+g exec gedit * This example creates a shortcut key (ALT+g) to open gedit *"

		print "> CTRL+C - Main Menu"
		valu=raw_input("Option: ")
		while 1:
			try:
				opt, key, action, param=valu.split(None,3)
				
				#opt=t[0]
				#key=t[1]
				key_final=key.split("+")[1]
				mod=key.split("+")[0]
				#action=t[2]
				#param=t[3]
				
			except IndexError:
				print "[error]: m00, wrong wrong wrong! ;-)"
				e17_keys()
			
			
			
			if opt=="a":
				pyetun_keys.add_key(key_final,mod,action,param)
				print bold("KEY:"),
				print mod,"+",key, "ADDED!"

				e17_keys()

			elif opt=="d":
				pyetun_keys.del_key(key_final,mod,action,param)
				print bold("KEY:"),
				print mod,"+",key, "DELETED!"
				e17_keys()
			
			else:
				print bold("[error] m000 wrong option!")
				e17_keys()

	except KeyboardInterrupt:
		print "\nOops! exiting ;)"
		console()


console()
	
