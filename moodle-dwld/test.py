try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
except ImportError:
	print ("Dependencies not satsfied")
driver = webdriver.Chrome()
driver.get("http://moodlecc.vit.ac.in")

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys('15BCE1283')
password.send_keys('geek@911')
btn = driver.find_element_by_id('loginbtn')

btn.click()

driver.implicitly_wait(10)

dashboard = driver.find_elements_by_css_selector('span.item-content-wrap')[0];

dashboard.click()

driver.implicitly_wait(5)

cse3002 = driver.find_element_by_css_selector('a[title="Internet and Web Programming(CSE3002)"]')

cse3002.click()


