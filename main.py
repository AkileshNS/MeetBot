from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import sys

#Add RVCE username and pwd. Don't worry, this file always runs locally.
NAME = ""
PASSWORD = ""

#driverpath = r"C:\Users\Akil\Desktop\Me\MeetsBot\ChromeDriver\chromedriver.exe"
#Add chrome driver path 
driverpath=""

#links = ['https://meet.google.com/okb-esoq-mqf','https://meet.google.com/fac-ktxt-iaz','https://meet.google.com/aag-mzfr-dxk','https://meet.google.com/pkz-djef-rcj']
#Add Class meet links to the list as followed above

links = []

def meetjoin(URL):

    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--disable-notifications")
    #Uncomment below argument if you want to mute all audio from the meet.
    #options.add_argument("--mute-audio")
    
    browser  = webdriver.Chrome(executable_path=driverpath,chrome_options=options)

    browser.get('https://accounts.google.com/signin')

    browser.find_element_by_name("identifier").send_keys(NAME)
    browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
    time.sleep(2)
    browser.find_element_by_name("password").send_keys(PASSWORD)
    browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
    time.sleep(2)
    browser.get(URL)
    #browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div').click()
    webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    time.sleep(3)
    #Mutes Mic
    browser.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    #Turns off Video
    browser.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    time.sleep(3)
    #Enters Meet
    browser.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
    #3000 indicates 50 minutes in seconds, Bot leaves meeting 50 minutes after joining.
    time.sleep(3000)
    
    browser.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button').click()
    time.sleep(2)
    sys.exit(0)


def getURL():
    day = datetime.today().weekday()
    hour = datetime.today().hour

    #Setup the following based on your time table.
    #Day=0 -> Monday
    #Day=4 -> Friday
    #Ensure your sysclock follows the 24 hour format
    if(day==0):
        if(hour==9):
            meetjoin(str(links[0]))
        elif(hour==10):
            print("Join Global class da")
            sys.exit(0)
        elif(hour==11):
            meetjoin(str(links[2]))
        elif(hour==12):
            meetjoin(str(links[3]))
        elif(hour==14):
            meetjoin(str(links[2]))
        else:
            sys.exit(0)

    elif(day==1):
        if(hour==9 or hour==10):
            meetjoin(str(links[2]))
        elif(hour==11):
            meetjoin(str(links[3]))
        elif(hour==12):
            meetjoin(str(links[1]))
        else:
            sys.exit(0)

    elif(day==2):
        if(hour==9):
            meetjoin(str(links[2]))
        elif(hour==10):
            print("Join Global class da")
            sys.exit(0)
        elif(hour==11):
            meetjoin(str(links[2]))
        elif(hour==12):
            meetjoin(str(links[0]))
        else:
            sys.exit(0)
        
    
    elif(day==3):
        if(hour==9):
            meetjoin(str(links[0]))
        elif(hour==10):
            print("Join Global class da")
            sys.exit(0)          
        elif(hour==11):
            meetjoin(str(links[1]))
        elif(hour==12):
            meetjoin(str(links[3]))
        else:
            sys.exit(0)

    elif(day==4):
        if(hour==9):
            meetjoin(str(links[2]))

        elif(hour==10):
            meetjoin(str(links[0]))

        elif(hour==11):
            meetjoin(str(links[2]))

        elif(hour==12):
            meetjoin(str(links[1]))
            
        else:
            sys.exit(0)

    else:
        sys.exit(0)


getURL()
