import tkinter as tk
import time
from PIL import Image
from PIL.ImageTk import PhotoImage

textColor1 = 'black'
bgColor1 = 'white'


def DrawLabels():
    global timeLabel
    global tramLabel
    global tramDepartureLabel
    global weatherLabelTitle
    global weatherIconToday
    global todayWeatherTextLabel
    global tomorrowWeatherTextLabel
    global weatherIconTomorrow
    
    
    ######### ALL LABELS ARE DEFINED HERE: ###########
    
    timeLabel=tk.Label(root,text='TIME',fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 20 bold")
    timeLabel.pack()
    
    
    # TRAMS
    yOffset = 0.45
    tramScreenShot=getTramScreenShot()
    tramDepartureLabel = tk.Label(root, image=tramScreenShot, bg = bgColor1)
    tramDepartureLabel.image=tramScreenShot
    tramDepartureLabel.pack()
    tramDepartureLabel.place(relx=0.01, rely=yOffset, anchor='sw')
    tramLabelText ='Trams: '
    tramLabel = tk.Label(root, text=tramLabelText,fg = textColor1, bg = bgColor1,
                         font = "SanFrancisco 16 bold")
    tramLabel.pack()
    tramLabel.place(relx=0.0, rely=yOffset-0.37, anchor='sw')


    #WEATHER LABELS:
    yOffset2 = yOffset+0.1
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
    tomorrowWeatherTextLabel.place(relx=0.04, rely=yOffset2+0.12, anchor='sw')
    tomorrowIcon = getWeatherIcon('today')
    weatherIconTomorrow = tk.Label(root, image=tomorrowIcon, bg = bgColor1)
    weatherIconTomorrow.image=todayIcon
    weatherIconTomorrow.pack()
    weatherIconTomorrow.place(relx=0.0, rely=yOffset2+0.13, anchor='sw')
    

def Refresher1Sec():
    timeLabel.configure(text=time.asctime())
    root.after(1000, Refresher1Sec) 


def Refresher3Sec():
    #Tram
    try:
        dep = getTramScreenShot()
        tramDepartureLabel.image = dep
        tramDepartureLabel.configure(image=dep)
    except:
        print('update 3sec failed')
    root.after(3000, Refresher3Sec)
    
def Refresher10Sec():
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
    root.after(25000, Refresher1000Sec)
    
def getTramScreenShot():
    path=r"C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\tramData\departures.png"
    im = Image.open(path)
    ph = PhotoImage(im)
    return ph
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
Refresher3Sec()
Refresher1000Sec()
root.mainloop()