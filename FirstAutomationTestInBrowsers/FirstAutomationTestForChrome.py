from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\\SeleniumAutomation\\PythonProjects\\browserdrivers\\chromedriver.exe")

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()