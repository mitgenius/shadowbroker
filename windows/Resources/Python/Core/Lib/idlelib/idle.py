# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: idle.py
import os.path
import sys
idlelib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, idlelib_dir)
import idlelib.PyShell
idlelib.PyShell.main()