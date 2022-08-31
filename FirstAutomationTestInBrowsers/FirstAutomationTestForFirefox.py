from selenium import webdriver

driver = webdriver.Firefox(executable_path="E:\\SeleniumAutomation\\Python\\PythonSeleniumProjects\\BasicSeleniumUsingPython\\allbrowsers\\geckodriver.exe")

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()