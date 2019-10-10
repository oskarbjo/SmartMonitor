
# Link that explains how to make a search on a page with pyppeteer:
# https://medium.com/@e_mad_ehsan/getting-started-with-puppeteer-and-chrome-headless-for-web-scrapping-6bf5979dee3e

# from tkinter import mainloop
import tkinter as tk
from TPGclass import TPGclass
import datetime
import time
from tkinter import StringVar
import threading

textColor1 = 'black'
bgColor1 = 'white'
def main():
    root = createMainWindow()
    updateAll(root)
    root.mainloop()

def updateAll(root):
    TPG = TPGclass()
    [departuresCERN,timeOfUpdate] = TPG.getDepartures('Vieusseux','CERN')
    [departuresGC,timeOfUpdate] = TPG.getDepartures('Vieusseux','Gare Cornavin')
    staticText = StaticText(root)
    tramDepartures = TramDepartures(root)
    tramDepartures.displayDepartureDataCERN(root, departuresCERN)
    tramDepartures.displayDepartureDataGC(root, departuresGC)
    tramDepartures.updateTime(root,timeOfUpdate)
    tramDepartures.updateTime(root,datetime.datetime.now().time())




def createMainWindow():
    root=tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background=bgColor1)
    return root



class TramDepartures:
    def __init__(self,root):    
        self.yOffset = 0.1    
        textData1='Towards CERN: '
        self.tramLabel = tk.Label(root, text=textData1,fg = textColor1, bg = bgColor1,
                             font = "SanFrancisco 16 bold")
        self.tramLabel.place(relx=0.0, rely=self.yOffset, anchor='sw')

        textData2='Towards Gare Cornavin: '
        self.tramLabel2 = tk.Label(root, text=textData2,fg = textColor1, bg = bgColor1,
                             font = "SanFrancisco 16 bold")
        self.tramLabel2.place(relx=0.0, rely=self.yOffset+0.22, anchor='sw')
        
        self.stringVar1 = StringVar()
        self.timeLabel = tk.Label(root, textvariable=self.stringVar1,fg = textColor1, bg = bgColor1,
                             font = "SanFrancisco 16 bold underline")
        self.timeLabel.place(relx=0.0, rely=0.05, anchor='sw')
        
        


    def displayDepartureDataCERN(self,root,departures):
        dep1 = tk.Label(root, text='1. ' + departures[0],fg = textColor1, bg = bgColor1,
                        font = "SanFrancisco 16")
        dep1.place(relx=0.0, rely=self.yOffset+0.05, anchor='sw')
        dep2 = tk.Label(root, text='2. ' + departures[1],fg = textColor1, bg = bgColor1,
                        font = "SanFrancisco 16")
        dep2.place(relx=0.0, rely=self.yOffset+0.1, anchor='sw')
        dep3 = tk.Label(root, text='3. ' + departures[2],fg = textColor1, bg = bgColor1,
                        font = "SanFrancisco 16")
        dep3.place(relx=0.0, rely=self.yOffset+0.15, anchor='sw')

    def displayDepartureDataGC(self,root,departures):

        dep1 = tk.Label(root, text='1. ' + departures[0],fg = textColor1, bg = bgColor1,
                        font = "SanFrancisco 16")
        dep1.place(relx=0.0, rely=self.yOffset+0.27, anchor='sw')
        dep2 = tk.Label(root, text='2. ' + departures[1],fg = textColor1, bg = bgColor1,
                        font = "SanFrancisco 16")
        dep2.place(relx=0.0, rely=self.yOffset+0.32, anchor='sw')
        dep3 = tk.Label(root, text='3. ' + departures[2],fg = textColor1, bg = bgColor1,
                        font = "SanFrancisco 16")
        dep3.place(relx=0.0, rely=self.yOffset+0.37, anchor='sw')
        
    def updateTime(self,root,dateTime):
        textData1='TRAM DEPARTURES (updated ' + str(dateTime)[0:10] + '): '
        self.stringVar1.set(textData1)
        print(self.stringVar1)
        
#         tramLabel = tk.Label(root, text=textData1,fg = textColor1, bg = bgColor1,
#                              font = "SanFrancisco 16 bold underline")
#         tramLabel.place(relx=0.0, rely=0.05, anchor='sw')


        
class StaticText:
    
     def __init__(self,root):
         textData1=str(datetime.datetime.now())
         self.displayTitle(root,textData1)
     
     def displayTitle(self,root,textData):
         tk.Label(root, 
         text=textData,
         fg = textColor1,
         bg = bgColor1,
         font = "SanFrancisco 26 bold").pack()


if __name__ == "__main__":
    main()
    
    
    