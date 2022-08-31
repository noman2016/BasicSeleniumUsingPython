from selenium import webdriver

driver = webdriver.Edge(executable_path="E:\\SeleniumAutomation\\Python\\PythonSeleniumProjects\\BasicSeleniumUsingPython\\allbrowsers\\msedgedriver.exe")

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()