# coding: utf-8
import pyppeteer as pp
import asyncio
from pyppeteer import launch
import datetime
import time
import re


class TPGclass2:
    
    def __init__(self):
        self.depTextBoxSelector = '#TR_arret_field'
        self.searchBtnSelector = '#aui_3_2_0_1334 > ul:nth-child(26) > li'
        self.tickBox1 = '#\31 4_GARE\ CORNAVIN'
        self.tickBox2 = '#\31 4_MEYRIN-GRAVIERE'
        self.tickBox3 = '#\31 4_PXPLUSXR\ BERNEX'
        self.tickBox4 = '#\31 8_BACHET'
        self.tickBox5 = '#\31 8_CERN'
        self.tickBox6 = '#\31 8_PALETTES'
        self.searchBtnSelector2 = '#lineDestinations_noscript > div.button-right > input'
        self.screenShotPath = r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\tramData/screenshot.png'
        self.screenShotPath2 = r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\tramData/screenshot2.png'
    
        
    async def makeTPGsearch(self):
        try:
            browser = await launch()
            page = await browser.newPage()
            await page.goto('http://www.tpg.ch/')
            await page.click(self.depTextBoxSelector)
            print('here1')
            time.sleep(1)
            await page.keyboard.type(self.from_)
            await page.keyboard.press('Enter')
            print('here2')
            time.sleep(5)
            await page.screenshot({'path': self.screenShotPath2})
#             time.sleep(1)
            print('scroll')
            await page.evaluate('{window.scrollBy(420, 910);}')
            time.sleep(2)
            print('click search all')
            await page.click(self.searchBtnSelector2)
            print('scroll')
            await page.evaluate('{window.scrollBy(0, 40);}')
            time.sleep(3)
            print('capturing screenshot')
            await page.screenshot({'path': self.screenShotPath})
            await browser.close()
        except:
            searchResult='Could not download data'
            print(searchResult)

    
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

    def getDepartures(self,from_):
        self.from_ = from_
        asyncio.get_event_loop().run_until_complete(self.makeTPGsearch())
#         self.cropImage(self.scre)
    
#     def cropImage(self):
        
 

def main():
    TPG = TPGclass2()
    while True: 
        TPG.getDepartures('Vieusseux')
        time.sleep(10)
    
    

if __name__ == "__main__":
    main()
        
        
