from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()