# -*- encoding=utf-8

from selenium import webdriver


# Create a Firefox Browser instance
browser = webdriver.Firefox()

# Delete all cookies and go to Google website
browser.delete_all_cookies()
browser.get('http://www.google.de')

# find element by
text = browser.find_element_by_link_text("search")
text.is_displayed()

# Type the text 'test' into the search input field
browser.find_element_by_id('gbqfq').send_keys('test')

# click the search button
browser.find_element_by_id("gbqfb").click()

# wait for results and take screen shot
browser.implicitly_wait(3)
browser.save_screenshot('test.png')





