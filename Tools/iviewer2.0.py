from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

class Aparat_bot():
    def __init__(self):
        #---Open Chrome Drive---
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')
        #---Address Chrome Driver---
        ChromePath = 'chromedriver_linux64/chromedriver'
        self.driver = webdriver.Chrome(ChromePath,chrome_options=option)

    def page_load(self,class_name):
        #---Time For View---
        TimeOut = 20

        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME,class_name))
            WebDriverWait(self.driver,TimeOut).until(element_present)
        except TimeoutException:
            print('<<Time Out>>')
#-------------------------------------------------------Editing----------------------------------------------------------------------
    def OpenVideo(self, url):
        self.driver.get(url)
        #---Open Video In URL User---
        video = self.driver.find_element_by_tag_name('video')
        #---Clicke For Video In URL---
        video.click()
        #---click In Buttum Play Video---
        self.page_load('ytp-button ytp-settings-button')
        video.click()
        #---Open Seting Video---
        setingOption = self.driver.find_elements_by_class_name('ytp-button ytp-settings-button')
        setingOption.click()
        #---Select the quality option---
        quality = self.driver.find_elements_by_class_name('romeo-button menu-button')
        quality.click()
        #---Decrease video quality---
        QualityValue = self.driver.find_element_by_xpath("//*[contains(text(), '148p')]")
        QualityValue.click()
        #---Open Seting Video---
        setingOption.click()
        #---Select the video playback speed option---
        speed = self.driver.find_element_by_by_xpath("//*[contains(text(), 'سرعت پخش')]")
        speed.click()
        #---Speed ​​up video---
        SpeedValue = self.driver.find_element_by_xpath("//*[contains(text(), '200%')]")
        SpeedValue.click()
#-------------------------------------------------------------------------------------------------------------------------------------
#---Welcome Page To Tools---        
print("      ________                                                         ")
print("     |        |                |                           |           ")
print("     |        |                |                      -----|-----      ")
print("     |        |    ________    |             ________      |           ")
print("     |________|   |--------|   |            |--------|     |           ")
print("     |      \     |--------|   |--------|   |--------|     |           ")
print("     |       \    |--------|   |        |   |--------|     |           ")
print("     |        \   |--------|   |        |   |--------|     |           ")
print("     |         \  |________|   |--------|   |________|     |______     ")
print("                     iviewer 2.0------YouTube ROBOT                              ")
print("                       Creator Aryia Behroziuan                        ")
print("_______________________________________________________________________")
print()
#---Runing Robot Aparat Create Object In Class---
video_url = input("Enter URL Video:>")
print()
for_url = int(input("Enter The Number Of Video Views:>"))
print("_______________________________________________________________________")
print()
#---Create Object In Class--
Robot = Aparat_bot()
for a in range(for_url):
    a = input()
    Robot.OpenVideo(video_url)