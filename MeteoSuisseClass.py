# coding: utf-8
import pyppeteer as pp
import asyncio
from pyppeteer import launch
import datetime
import time
import re
from PIL import Image

class MeteoSuisse():
    
    def __init__(self):
        self.geneveSelector='#forecast-map > div.leaflet-map-pane > div.leaflet-objects-pane > div.leaflet-marker-pane > div:nth-child(26)'
        self.todayWeatherDataSelector='#overview__leaflet-map-popover > section > article.popup-today'
        self.tomorrowWeatherDataSelector='#overview__leaflet-map-popover > section > article:nth-child(6)'
        self.searchResultToday=''
        self.searchResultTomorrow=''
        self.weatherIconToday='#overview__leaflet-map-popover > section > article.popup-today > img'
        self.weatherIconTomorrow='#overview__leaflet-map-popover > section > article:nth-child(6) > img'
        self.imgURL1=''
        self.imgURL2=''
        self.SCpathToday = r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\weatherIcons/screenshotToday.png'
        self.SCpathTomorrow = r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\weatherIcons/screenshotTomorrow.png'
    async def makeMeteoSuisseSearch(self):
        try:
            browser = await launch()
            page = await browser.newPage()
            await page.goto('https://www.meteosuisse.admin.ch/home.html?tab=overview')
            print('On web page')
            await page.click(self.geneveSelector)
            print('Clicked geneve')
            element = await page.querySelector(self.todayWeatherDataSelector)
            self.searchResultToday = await page.evaluate('(element) => element.textContent', element)
            element = await page.querySelector(self.tomorrowWeatherDataSelector)
            self.searchResultTomorrow = await page.evaluate('(element) => element.textContent', element)
              
            print('Data fetched')
             
            element = await page.querySelector(self.weatherIconToday)
            self.imgURL1 = await page.evaluate('(element) => element.src', element)
            element = await page.querySelector(self.weatherIconTomorrow)
            self.imgURL2 = await page.evaluate('(element) => element.src', element)
            
            await page.goto(self.imgURL1)
            await page.screenshot({'path': self.SCpathToday})

            await page.goto(self.imgURL2)
            await page.screenshot({'path': self.SCpathTomorrow})

            await browser.close()
            
        except:
            self.searchResultToday='Could not download data'
            self.searchResultTomorrow='Could not download data'
    
    def getWeatherData(self,input):
        data=input.replace('\t','')
        data=data.replace('\xa0','')
        data=data.splitlines()
        weatherData = list(filter(None, data)) #remove any empty strings
#         print(weatherData)
        return weatherData
        
        
    def cropWeatherIcon(self):
        path=r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\weatherIcons/todayIcon.png'
        im = Image.open(self.SCpathToday)
        im1 = im.crop((0,0,40,46)) 
        im1.save(path)
        path=r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\weatherIcons/tomorrowIcon.png'
        im = Image.open(self.SCpathTomorrow)
        im1 = im.crop((0,0,40,46)) 
        im1.save(path)
    
    def writeWeatherDataToFile(self):
        data=self.searchResultToday.replace('\t','')
        data=str(data.splitlines()[3:5])  
        data=data.replace('{[','')
        data=data.replace(']}','')      
        fpath = r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data/'
        fname = 'weatherDataToday.txt'
        file = open(fpath+fname,'w')
        file.write(data)
        
        data=self.searchResultTomorrow.replace('\t','')
        data=str(data.splitlines()[3:5])  
        data=data.replace('{[','')
        data=data.replace(']}','')      
        fpath = r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data/'
        fname = 'weatherDataTomorrow.txt'
        file = open(fpath+fname,'w')
        file.write(data)
        
    def updateMeteo(self):
        asyncio.get_event_loop().run_until_complete(self.makeMeteoSuisseSearch())
        weatherDataToday=self.getWeatherData(self.searchResultToday)
        weatherDataTomorrow=self.getWeatherData(self.searchResultTomorrow)
        self.cropWeatherIcon()
        self.writeWeatherDataToFile()
        
def main():
    while True:
        try:
            Meteo = MeteoSuisse()
            Meteo.updateMeteo()
            print(Meteo.searchResultToday)
            time.sleep(30)
        except:
            print('Could not retrieve data')
    

if __name__ == "__main__":
    main()
        