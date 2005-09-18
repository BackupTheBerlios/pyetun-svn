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

