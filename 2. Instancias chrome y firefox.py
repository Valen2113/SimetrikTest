from selenium import webdriver

# Configuracion Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_driver = webdriver.Chrome(options=chrome_options)

# Configuracion Firefox WebDriver
firefox_options = webdriver.FirefoxOptions()
firefox_driver = webdriver.Firefox(options=firefox_options)

chrome_driver.get("https://www.google.com")


firefox_driver.get("https://www.google.com")


chrome_driver.quit()
firefox_driver.quit()
