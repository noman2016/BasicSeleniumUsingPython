from selenium import webdriver

from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()