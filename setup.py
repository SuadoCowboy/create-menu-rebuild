from cx_Freeze import setup, Executable
import sys

build_exe_options = {"excludes": ["PyQt4.QtSql", "sqlite3", 
                                  "scipy.lib.lapack.flapack",
                                  "PyQt4.QtNetwork",
                                  "PyQt4.QtScript",
                                  "numpy.core._dotblas", 
                                  "PyQt5"],
                     "optimize": 2}

setup(name='Create Menu',
    version='2.0',
    description='',
    options = {"build_exe": build_exe_options},
    executables = [Executable('main.py', base=('Win32GUI' if sys.platform == 'win32' else None), icon='icon.ico')])