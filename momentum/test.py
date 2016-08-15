try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
except ImportError:
	print ("Dependencies not satsfied")

driver = webdriver.Chrome()
driver.get("chrome://newtab")





