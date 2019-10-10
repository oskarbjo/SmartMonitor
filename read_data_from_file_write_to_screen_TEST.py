import tkinter as tk
import time
from PIL import Image
from PIL.ImageTk import PhotoImage

textColor1 = 'black'
bgColor1 = 'white'


def DrawLabels():
    global timeLabel
    global tramTitle1
    global tramTitle2
    global CERNdepLabel
    global GCdepLabel
    global weatherLabelTitle
    global weatherIconToday
    global todayWeatherTextLabel
    global tomorrowWeatherTextLabel
    global weatherIconTomorrow
    
    
    ######### ALL LABELS ARE DEFINED HERE: ###########
    
    timeLabel=tk.Label(root,text='TIME',fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 20 bold")
    timeLabel.pack()
    
    yOffset = 0.1    
    textData1='Trams towards CERN: '
    tramTitle1 = tk.Label(root, text=textData1,fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 16 bold")
    tramTitle1.pack()
    tramTitle1.place(relx=0.0, rely=yOffset, anchor='sw')
    
    
    textData2='Trams towards Gare Cornavin: '
    tramTitle2 = tk.Label(root, text=textData2,fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 16 bold")
    tramTitle2.pack()
    tramTitle2.place(relx=0.0, rely=yOffset+0.1, anchor='sw')
    
    
    CERNdepLabel = tk.Label(root, text='1. ' + 'CERN DATA',fg = textColor1, bg = bgColor1,
                    font = "SanFrancisco 16")
    CERNdepLabel.pack()
    CERNdepLabel.place(relx=0.0, rely=yOffset+0.05, anchor='sw')
    
    GCdepLabel = tk.Label(root, text='1. ' + 'GC DATA',fg = textColor1, bg = bgColor1,
                    font = "SanFrancisco 16")
    GCdepLabel.pack()
    GCdepLabel.place(relx=0.0, rely=yOffset+0.15, anchor='sw')

    #WEATHER LABELS:
    yOffset2 = yOffset+0.25
    weatherLabelTitleText ='Weather: '
    weatherLabelTitle = tk.Label(root, text=weatherLabelTitleText,fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 16 bold")
    weatherLabelTitle.pack()
    weatherLabelTitle.place(relx=0.0, rely=yOffset2, anchor='sw')
    
    
    todayWeatherTextLabel = tk.Label(root, text='',fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 16 bold")
    todayWeatherTextLabel.pack()
    todayWeatherTextLabel.place(relx=0.04, rely=yOffset2+0.06, anchor='sw')
    todayIcon = getWeatherIcon('today')
    weatherIconToday = tk.Label(root, image=todayIcon, bg = bgColor1)
    weatherIconToday.image=todayIcon
    weatherIconToday.pack()
    weatherIconToday.place(relx=0.0, rely=yOffset2+0.07, anchor='sw')
    
    tomorrowWeatherTextLabel = tk.Label(root, text='',fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 16 bold")
    tomorrowWeatherTextLabel.pack()
    tomorrowWeatherTextLabel.place(relx=0.04, rely=yOffset2+0.11, anchor='sw')
    tomorrowIcon = getWeatherIcon('today')
    weatherIconTomorrow = tk.Label(root, image=tomorrowIcon, bg = bgColor1)
    weatherIconTomorrow.image=todayIcon
    weatherIconTomorrow.pack()
    weatherIconTomorrow.place(relx=0.0, rely=yOffset2+0.12, anchor='sw')
    

def Refresher1Sec():
    timeLabel.configure(text=time.asctime())
    root.after(1000, Refresher1Sec) 
    
def Refresher10Sec():
    #Tram
    CERNdepLabel.configure(text=getCERNTramData())
    GCdepLabel.configure(text=getGCTramData())
    root.after(10000, Refresher10Sec)
    
def Refresher1000Sec():
    #Weather
    todayWeatherTextLabel.configure(text=getWeatherData()[0])
    icon1=getWeatherIcon('today')
    weatherIconToday.image = icon1  # <== this is were we anchor the img object
    weatherIconToday.configure(image=icon1)
    tomorrowWeatherTextLabel.configure(text=getWeatherData()[1])
    icon1=getWeatherIcon('tomorrow')
    weatherIconTomorrow.image = icon1  # <== this is were we anchor the img object
    weatherIconTomorrow.configure(image=icon1)
    root.after(1000000, Refresher1000Sec)
    
def getCERNTramData():
    file=open(r"C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\CERN Tram Data.txt", "r")
    data=file.readlines()
    return data[0]
def getGCTramData():
    file=open(r"C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\Gare Cornavin Tram Data.txt", "r")
    data=file.readlines()
    return data[0]
def getWeatherIcon(day):
    path=r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\weatherIcons/'+ day +'Icon.png'
    im = Image.open(path)
    ph = PhotoImage(im)
    return ph
def getWeatherData():
    file=open(r"C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\weatherDataToday.txt", "r")
    dataToday=str(file.readlines())
    dataToday=dataToday.replace('[','')
    dataToday=dataToday.replace(']','')
    dataToday=dataToday.replace('\'','')
    dataToday=dataToday.replace('\"','')
    dataToday="Aujourd'hui: " + dataToday
    file=open(r"C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\weatherDataTomorrow.txt", "r")
    dataTomorrow=str(file.readlines())
    dataTomorrow=dataTomorrow.replace('[','')
    dataTomorrow=dataTomorrow.replace(']','')
    dataTomorrow=dataTomorrow.replace('\'','')
    dataTomorrow=dataTomorrow.replace('\"','')
    dataTomorrow = 'Demain: '+ dataTomorrow
    return dataToday,dataTomorrow

root=tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background=bgColor1)
DrawLabels()
Refresher1Sec()
Refresher10Sec()
Refresher1000Sec()
root.mainloop()