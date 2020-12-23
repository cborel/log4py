clear all

py_path = py.sys.path;
py_path.insert(int64(1), '..\\');
log = py.importlib.import_module('log4py');
py.importlib.reload(log);

a = log.log4py();
a.DEBUG('ciao');
a.INFO('ciao');
a.ERROR('ciao');
a.CRITICAL('ciao');
a.WARNING('ciao');
