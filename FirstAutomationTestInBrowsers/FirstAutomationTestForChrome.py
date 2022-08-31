from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\SeleniumAutomation\\Python\\PythonSeleniumProjects\\BasicSeleniumUsingPython\\allbrowsers\\chromedriver.exe")

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()