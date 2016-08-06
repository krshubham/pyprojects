try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
except ImportError:
	print "Dependencies not satsfied"
driver = webdriver.Firefox()
driver.get("localhost:3000/admin")
username = driver.find_element_by_name("name")
password = driver.find_element_by_name("password")
username.clear()
password.clear()
username.send_keys("krshubham")
password.send_keys("shubhi")
username.send_keys(Keys.RETURN)
title = driver.find_element_by_name("title")
title.clear()
title.send_keys("Testing thr web app")
content = driver.find_element_by_name("content")
content.clear()
content.send_keys("Test is successful")
content.submit()