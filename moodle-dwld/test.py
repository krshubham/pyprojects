try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
except ImportError:
	print "Dependencies not satsfied"
driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/1mytyPTLJ00m2BLjeSHBB64a2VTgyBUkdCVNkdVlAwoU/viewform?edit_requested=true")
boxes = driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
print boxes
arr = ['Kumar Shubham','test','youu','youu','youu','youu','youu']
for i in range(0,len(boxes)):
	boxes[i].send_keys(arr[i]);
