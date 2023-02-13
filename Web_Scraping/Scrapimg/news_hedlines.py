from selenium  import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


# # profile = webdriver.FirefoxProfile()
# # profile.accept_untrusted_certs = True
# # driver = webdriver.Firefox(firefox_profile=profile)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# "Program run without Opening Browser"
    # path = "D:/New_Start/Automate_with_Python/Automate_with_Python/ChromeDriver/chromedriver.exe"
    # from selenium.webdriver.chrome.options import Options
    # options = Options()
    # options.headless = True
    # service = Service(executable_path=path)
    # driver = webdriver.Chrome(service=service, options=options)


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
        self.implicitly_wait(10)
        self.maximize_window()

    # def __exit__(self, exc_type, exc, traceback):
    #     if self.teardown:
    #         self.quit()

    def landPage(self):
        self.get(URL)
    
    def Card_news(self):
        titles = []
        sub_titles = []
        news_links = []
        containers = self.find_elements(By.XPATH, '//div[@class="teaser-item teaser__small  theme-football"]')

        for cotainer in containers:
            title = cotainer.find_element(By.XPATH, './div/a/h3').text
            sub_title = cotainer.find_element(By.XPATH, './div/a/p').text
            news_link = cotainer.find_element(By.XPATH, './div/a').get_attribute('href')

            titles.append(title)
            sub_titles.append(sub_title)
            news_links.append(news_link)
    
        my_dict = {'Title':titles, 'Sub_Title': sub_titles, 'News_Link': news_links}
        df_headlines = pd.DataFrame(my_dict)
        df_headlines.to_csv('Headlines.csv')

        self.quit()
        print("All Complete")

    

        



    



