import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time




driver = webdriver.Chrome('/home/juan.martin.lequerica/Documents/drivers/chromedriver')
driver.get('https://login.replicon.com/DefaultV2.aspx')

companyName = driver.find_element_by_id('CompanyNameTextBox')
companyName.send_keys('tradehelm')
driver.find_element_by_id('NextButton').click()


#login
username = driver.find_element_by_id('LoginNameTextBox')
longstring='jose'
time.sleep(3)
driver.execute_script("document.getElementById('LoginNameTextBox').setAttribute('value', 'mailn')");
driver.execute_script("document.getElementById('PasswordTextBox').setAttribute('value', 'password!')");
driver.find_element_by_id('LoginButton').click()

#inside 
time.sleep(7)
#add column
newLine=driver.find_element_by_id('add-new-timeline')
newLine.click()

#class duration
#select by row 3
items = driver.find_elements_by_xpath("//td[contains(@class, 'day') and not(@class='dayOff')]//input")
time.sleep(2)
for item in items:
    try: 
        #print(item.__dict__)
        item.send_keys("8")
        print('item.text: {0}'.format(item_text))
    except:
        pass


itemsOff = driver.find_elements_by_xpath("//td[contains(@class, 'dayOff')]//input")
for off in itemsOff:
    off.clear()
    off.send_keys("0")

#time.sleep(5)
#driver.close()



