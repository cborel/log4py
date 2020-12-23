import sys;
import os;
sys.path.insert(0, os.path.dirname(__file__)+ "/..");
import log4py
a = log4py.log4py();
a.DEBUG('ciao');
a.INFO('ciao');
a.ERROR('ciao');
a.CRITICAL('ciao');
a.WARNING('ciao');