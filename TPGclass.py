# coding: utf-8
import pyppeteer as pp
import asyncio
from pyppeteer import launch
import datetime
import time
import re


class TPGclass:
    
    def __init__(self):
        self.depTextBoxSelector = '#REQ0JourneyStopsS0G'
        self.destTextBoxSelector = '#REQ0JourneyStopsZ0G'
        self.searchBtnSelector = 'body > form > div > input.directionsSearchButton'
        self.resultSelector = '#HFSResult > table:nth-child(5)'
        self.vieusseux = 'vieusseux'
        self.CERN = 'CERN'
        self.GC = 'Gare Cornavin'
    
    def updateTPG(self,from_,to_):
        self.writeTPGDataToFile(from_,to_)
        
    async def makeTPGsearch(self):
        try:
            browser = await launch()
            page = await browser.newPage()
            await page.goto('https://m.tpg.ch/directions.htm')
            await page.click(self.depTextBoxSelector)
            await page.keyboard.type(self.from_)
            await page.click(self.destTextBoxSelector)
            await page.keyboard.type(self.to_)
            await page.click(self.searchBtnSelector)
            time.sleep(1)
            element = await page.querySelector(self.resultSelector)
            self.searchResult = await page.evaluate('(element) => element.textContent', element)
            await browser.close()
            print(self.searchResult)
        except:
            self.searchResult='Could not download data'
            print(self.searchResult)

    
    def identifyDepartureTimes(self):
        depInd=[m.start() for m in re.finditer('p. ', self.searchResult)] #sort out departure times
        print(depInd)
        try:
            dep1=self.searchResult[depInd[0]+3:depInd[0]+8]
        except:
            dep1='No data available'
        try:
            dep2=self.searchResult[depInd[1]+3:depInd[1]+8]
        except:
            dep2='No data available'
        try:
            dep3=self.searchResult[depInd[2]+3:depInd[2]+8]
        except:
            dep3='No data available'
        departures=[dep1,dep2,dep3]
        return departures

    def getDepartures(self,from_,to_):
        self.from_ = from_
        self.to_ = to_
        asyncio.get_event_loop().run_until_complete(self.makeTPGsearch())
        departureText = self.identifyDepartureTimes()
        time=str(datetime.datetime.now().time())
        out=', '.join(departureText) + ', Data updated ' + time[0:8]
        return out
    
    def writeTPGDataToFile(self,from_,to_):
        data=str(self.getDepartures(from_, to_))
        fpath = r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data/'
        fname = to_ + ' Tram Data.txt'
        file = open(fpath+fname,'w')
        file.write(data)
 

def main():
    TPG = TPGclass()
    while True: 
        TPG.updateTPG('Vieusseux','CERN')
        TPG.updateTPG('Vieusseux','Gare Cornavin')
        time.sleep(11)
    
    

if __name__ == "__main__":
    main()
        
        
