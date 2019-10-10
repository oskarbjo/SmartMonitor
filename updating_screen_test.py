from tkinter import *
import TPGclass
import datetime
import time
class UpdateScreen(Frame):
    def __init__(self, master=None,):
        self.TPG = TPGclass.TPGclass()
        master.geometry("100x50+5+5")
        Frame.__init__(self, master)
        master.attributes("-fullscreen", True)
        root.configure(background='white')
        self.pack()
        self.timestr = StringVar()
        lbl1 = Label(master, textvariable=self.timestr)
        lbl1.pack()
        self.updateTimeStr = StringVar()
        TPGtimeLbl = Label(root, textvariable=self.updateTimeStr,fg = 'black', bg = 'white',
                             font = "SanFrancisco 16 bold underline")
        TPGtimeLbl.place(relx=0.0, rely=0.05, anchor='sw')
        
        # register callback
        self.listenID1 = self.after(1000, self.newtime)
        self.listenID2 = self.after(5000,self.TPGupdate)
    def newtime(self):
        timenow = datetime.datetime.now()
        self.timestr.set("%d:%02d:%02d" %(timenow.hour, timenow.minute, timenow.second))
        self.listenID1 = self.after(1000, self.newtime)
        print('clock')
    def TPGupdate(self):
        [departuresCERN,timeOfUpdate] = self.TPG.getDepartures('Vieusseux','CERN')
        self.updateTimeStr.set(timeOfUpdate)
        self.listenID2 = self.after(5000,self.TPGupdate())
        print('updatetime')
    
root=Tk()
CT = UpdateScreen(root)
CT.mainloop()


