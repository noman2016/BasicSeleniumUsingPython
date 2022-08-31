from selenium import webdriver

driver = webdriver.Firefox(executable_path="/AllBrowsersDriver\\geckodriver.exe")

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()