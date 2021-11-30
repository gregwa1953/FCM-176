#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7x
#  in conjunction with Tcl version 8.6
#    Sep 20, 2021 07:21:38 AM CDT  platform: Linux
#    Sep 20, 2021 07:22:18 AM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import tkinter.messagebox as messagebox
import login


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = login.formLogin(_top1)
    # My startup code here
    start_up()
    root.mainloop()


def start_up():
    _w1.entryUsername.focus_set()


def on_btnContinue(*args):
    print('login_support.on_btnContinue')
    for arg in args:
        print('another arg:', arg)
    sys.stdout.flush()

    users = ['Greg', 'Steve', 'Sam']
    password = 'password'
    if _w1.UserData.get() in users:
        if password == _w1.PassData.get():
            titl = 'Login Accepted'
            msg = 'Username and password accepted'
            resp = messagebox.showinfo(titl, msg)
            root.destroy()
    else:
        titl = 'Login Information Incorrect'
        msg = 'Information not accepted'
        resp = messagebox.showerror(titl, msg)
        _w1.UserData.set('')
        _w1.PassData.set('')
        _w1.entryUsername.focus_set()


if __name__ == '__main__':
    login.start_up()