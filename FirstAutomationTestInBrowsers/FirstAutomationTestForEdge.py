from selenium import webdriver

driver = webdriver.Edge(executable_path="/AllBrowsersDriver\\msedgedriver.exe")

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()