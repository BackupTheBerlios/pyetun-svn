#!/usr/bin/env python

from distutils.core import setup

setup(name='pyetun',
      version='0.2',
      description='E17 tunner',
      author='Luis Marques',
      author_email='drune@gmx.net',
      url='http://pyetun.berlios.de',
      py_modules=['pyetun_bshade', 'pyetun_cache', 'pyetun_cfg', 'pyetun_desk', 'pyetun_focus', 'pyetun_font', 'pyetun_keys', 'pyetun_kill', 'pyetun_lang', 'pyetun_mod', 'pyetun_winlist', 'pyetun_edge'],
		data_files=[('/etc', ['pyetun.conf']),
					('/usr/bin', ['pyetun'])]
     )
