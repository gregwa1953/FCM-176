#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7x
#  in conjunction with Tcl version 8.6
#    Sep 20, 2021 07:22:08 AM CDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import login_support

class formLogin:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("468x253+797+414")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(0,  0)
        top.title("LOGIN FORM")
        top.configure(highlightcolor="black")

        self.top = top
        self.UserData = tk.StringVar()
        self.PassData = tk.StringVar()

        self.labelStaticUsername = tk.Label(self.top)
        self.labelStaticUsername.place(x=56, y=37, height=21, width=99)
        self.labelStaticUsername.configure(activebackground="#f9f9f9")
        self.labelStaticUsername.configure(anchor='e')
        self.labelStaticUsername.configure(text='''Username:''')

        self.labelStatucPassword = tk.Label(self.top)
        self.labelStatucPassword.place(x=56, y=95, height=21, width=99)
        self.labelStatucPassword.configure(activebackground="#f9f9f9")
        self.labelStatucPassword.configure(anchor='e')
        self.labelStatucPassword.configure(text='''Password:''')

        self.entryUsername = tk.Entry(self.top)
        self.entryUsername.place(x=160, y=30, height=33, width=206)
        self.entryUsername.configure(background="white")
        self.entryUsername.configure(font="TkFixedFont")
        self.entryUsername.configure(selectbackground="blue")
        self.entryUsername.configure(selectforeground="white")
        self.entryUsername.configure(textvariable=self.UserData)

        self.entryPassword = tk.Entry(self.top)
        self.entryPassword.place(x=160, y=90, height=33, width=206)
        self.entryPassword.configure(background="white")
        self.entryPassword.configure(font="TkFixedFont")
        self.entryPassword.configure(selectbackground="blue")
        self.entryPassword.configure(selectforeground="white")
        self.entryPassword.configure(textvariable=self.PassData)

        self.btnContinue = tk.Button(self.top)
        self.btnContinue.place(x=170, y=160, height=43, width=153)
        self.btnContinue.configure(activebackground="#f9f9f9")
        self.btnContinue.configure(borderwidth="2")
        self.btnContinue.configure(command=login_support.on_btnContinue)
        self.btnContinue.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.btnContinue.configure(text='''Continue''')

def start_up():
    login_support.main()

if __name__ == '__main__':
    login_support.main()




