try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
except ImportError:
	print ("Dependencies not satsfied")

driver = webdriver.Chrome()
driver.get("http://academicscc.vit.ac.in/student")

username = driver.find_element_by_name('regno')
password = driver.find_element_by_name('passwd')
username.send_keys('15BCE1283')
password.send_keys('chmod777')
btn = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[6]/td/input[1]')

driver.implicit_wait(20)





