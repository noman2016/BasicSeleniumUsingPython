from selenium import webdriver

driver = webdriver.Firefox(executable_path="E:\\SeleniumAutomation\\PythonProjects\\browserdrivers\\geckodriver.exe")

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()