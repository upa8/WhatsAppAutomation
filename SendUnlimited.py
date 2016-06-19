""" 
	Author : Pratik Upacharya
	Date : 18 June 2016
"""

from time import sleep
from selenium import webdriver

print "Let's get started ....."

# Select whichever browser you want to open 
getBrowserContext = webdriver.Firefox()
# Enter the link of the whatsapp web 
getBrowserContext.get('http://web.whatsapp.com')

# Enter the message you want to send 
print "Enter the message to send"
message = raw_input()

# Enter the no of times you want to send it 

print " Enter the no of times you want to sent it ."
numberOfTimes = raw_input()

# Now enter the user name which is in your contacts "Friend Name"

getTheUserName = getBrowserContext.find_element_by_xpath('//span[contains(text(),"Friend Name")]')
getTheUserName.click()
selectInput = getBrowserContext.find_elements_by_class_name('input')

for x in xrange(1,numberOfTimes):
	selectInput[1].send_keys(message)
	getBrowserContext.find_element_by_class_name('send-container').click()
	print "Waiting"
	# You can change remove this sleep time or change it . 
	# Its sleeping for 300seconds now 
	sleep(300)     
	print "Send"

# You can send unlimited messages by using while loop for infinite times
