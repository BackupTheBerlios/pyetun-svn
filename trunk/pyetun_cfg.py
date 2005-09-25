import os,sys

def return_cfg():
	try:
		import ConfigParser
		config = ConfigParser.ConfigParser()
		
		if os.path.exists("/etc/pyetun.conf"):
			config.read("/etc/pyetun.conf")
			
			return config
		
		else:
			print "[error]: Configuration file not found!"
			print "Exiting.."
			sys.exit()

		
		return value
	except KeyboardInterrupt:
		print "Thanks for using E17 tunner. You're now a rice boy.. ;)\n"
		sys.exit()

def return_remote():
	config=return_cfg()
	value=config.get("paths","enlightement_remote")
	return value
		


def return_modpath(mod_type):
	config=return_cfg()
	value=config.get("modules",mod_type)
	return value

#set enlightenment_remote path...to use with autogenerate
def set_er_path():
	config=return_cfg()

	val=os.popen("whereis enlightenment_remote").readlines()
	val2=val[0].split(" ")
	# delete first element (name of app..)
	del val2[0]
	try:
		f = open("/etc/pyetun.conf", 'w')

	except IOError:
		print "\n> Error: Permission Denied when editing /etc/pyetun.conf or File not Found!"
		sys.exit()

	for i in val2: 
		if os.path.exists(i):
			
			config.set("paths","enlightement_remote", i)
			config.write(f)
			f.close()
			break

def set_modules_path():
	
	pos_paths=["/usr/lib/enlightenment/modules/","/usr/local/lib/enlightenment/modules/","/opt/lib/enlightenment/modules/"]
	
	config=return_cfg()
	try:

		f2 = open("/etc/pyetun.conf", 'w')
	except IOError:
		print "\n> Error: Permission Denied when editing /etc/pyetun.conf or File not Found!"
		sys.exit()
	for j in pos_paths:
		if os.path.exists(j):
			config.set("modules","normal", j)
			
			config.set("modules","extra",j[:-1]+"_extra/")
			config.write(f2)
			f2.close()
			break


			

			

	
