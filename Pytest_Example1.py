from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver = webdriver.Chrome()


#driver = webdriver.Chrome(ChromeDriverManager("2.36").install())
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
sleep(3)
driver.close()

