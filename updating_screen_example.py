from tkinter import *
# import tkinter as tk
import datetime
import time
class ChangeTime(Frame):
    def __init__(self, master=None):
        master.geometry("100x50+5+5")
        Frame.__init__(self, master)
        self.pack()
        self.timestr = StringVar()
        lbl = Label(master, textvariable=self.timestr)
        lbl.pack()
        # register callback
        self.listenID = self.after(1000, self.newtime)
    def newtime(self):
        timenow = datetime.datetime.now()
        self.timestr.set("%d:%02d:%02d" %(timenow.hour, timenow.minute, timenow.second))
        self.listenID = self.after(1000, self.newtime)
root=Tk()
CT = ChangeTime(root)
CT.mainloop()