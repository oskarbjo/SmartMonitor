# coding: utf-8
import pyppeteer as pp
import asyncio
from pyppeteer import launch
import datetime
import time
import re
from PIL import Image

class CERNcalendar:
    
    def __init__(self):
        self.url = 'https://mmmservices.web.cern.ch/mmmservices/'
        self.mailSelector = '#ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_Menu2 > tbody > tr:nth-child(2) > td:nth-child(3) > a > b'
        self.userNameSelector = '#ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_txtFormsLogin'
        self.passwordSelector = '#ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_txtFormsPassword'
        self.loginBtnSelector = '#ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlForm > div.oneAuth > table > tbody > tr:nth-child(2) > td.box_signinbutton'
        self.calendarSelector = '#lnkCal'
        self.weekViewSelector = '#divToolbarButtonweek'
        self.weekScheduleSelector = '#divMainViewbody'
        self.searchResult = ''
        self.screenShotPath=r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\cernCal/screenshot.png'
        
    async def goToCERNmail(self):
        browser = await launch()
        print('browser launched')
        page = await browser.newPage()
        await page.goto(self.url)
        await page.click(self.mailSelector)
        time.sleep(1)
        await page.click(self.userNameSelector)
        await page.keyboard.type('objorkqv')
        await page.click(self.passwordSelector)
        await page.keyboard.type('=OKQWE9ijzxc')
        await page.click(self.loginBtnSelector)
        time.sleep(2)
        print('Logged on to mail')
        await page.screenshot({'path': self.screenShotPath})
        print('screenshot1')
        await page.click(self.calendarSelector)#click twice in case notifications pop up
        await page.click(self.calendarSelector)
        time.sleep(2)
        print('Clicked calendar')
#         await page.screenshot({'path': self.screenShotPath})
#         print('screenshot2')
#         await page.click(self.weekViewSelector)
#         print('Clicked week view')
        await page.screenshot({'path': self.screenShotPath})
        print('screenshot3')
        element = 'await page.querySelector(self.weekScheduleSelector)'
        self.searchResult = await page.evaluate('(element) => element.outerHTML', element)
        await browser.close()
        

    
    def cropCalendarImage(self):
        path=r'C:\Users\Oskar\Dropbox\Local files_oskars dator\Dropbox dokument\Python Scripts\SmartMonitor_data\cernCal/calendar.png'
        im = Image.open(self.screenShotPath)
        im1 = im.crop((100,100,760,560))
        im1.save(path)
        print('cropped image')
        
    def updateCal(self):
        asyncio.get_event_loop().run_until_complete(self.goToCERNmail())
        self.cropCalendarImage()

def main():
    while True:
        CERNcal = CERNcalendar()
        CERNcal.updateCal()
        print('')
        time.sleep(10)

    

if __name__ == "__main__":
    main()
        
        
