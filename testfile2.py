import pyppeteer as pp
import asyncio
from pyppeteer import launch
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
path = r'C:\Users\Oskar\eclipse-workspace\smart_display_project\pics/'

selector1 = '#REQ0JourneyStopsS0G'
selector2 = '#REQ0JourneyStopsZ0G'
selector3 = 'body > form > div > input.directionsSearchButton'
async def makeTPGsearch():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://m.tpg.ch/directions.htm')
    await page.click(selector1)
    await page.keyboard.type('vieusseux')
    await page.click(selector2)
    await page.keyboard.type('CERN')
    await page.click(selector3)
    await page.screenshot({'path': path + 'screendump1.png'})
    await browser.close()


def cropImage(path):
    im = Image.open(path)
    width, height = im.size 
    left = 400
    top = 280
    right = 500
    bottom = 380
    im1 = im.crop((left, top, right, bottom)) 
#     im = im.filter(ImageFilter.MedianFilter())
#     enhancer = ImageEnhance.Contrast(im)
#     im = enhancer.enhance(2)
#     im = im.convert('1')
    im1.save(r'C:\Users\Oskar\eclipse-workspace\smart_display_project\pics/'+'cropped.png')
    return im1

def identifyDepartureTimes(im):

#     im.save('temp2.jpg')
    text1 = pytesseract.image_to_string(im)
    text2=text1.split('\n',6)
    departures = [text2[0][-5:],text2[3][-5:],text2[5][-5:]]
    return departures

asyncio.get_event_loop().run_until_complete(makeTPGsearch())
croppedImage = cropImage(path + 'screendump.png')
departureText = identifyDepartureTimes(croppedImage)
print(departureText)

#print(' ')
