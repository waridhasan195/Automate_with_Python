from selenium  import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://www.thesun.co.uk/sport/football/'
# path = "D:/New_Start/Automate_with_Python/Automate_with_Python/ChromeDriver/chromedriver.exe"
# path = "D:/New_Start/Automate_with_Python/Automate_with_Python/edgedriver_win64/msedgedriver.exe"


class TheSun(webdriver.Chrome):
    def __init__(self, driver_path = r"D:/New_Start/Automate_with_Python/Automate_with_Python/ChromeDriver/chromedriver.exe"):
        self.driver_path = driver_path
        # self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(TheSun, self).__init__(options=options)
        self.implicitly_wait(40)
        self.maximize_window()
    

        

# from selenium import webdriver

# # profile = webdriver.FirefoxProfile()
# # profile.accept_untrusted_certs = True

# # driver = webdriver.Firefox(firefox_profile=profile)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get(URL)
# driver.maximize_window()
# driver.implicitly_wait(10)

