# from selenium import webdriver
# import time
# browser = webdriver.Chrome('/Users/parvathi/Downloads/chromedriver')

# browser.get('http://127.0.0.1:5000/home')
# time.sleep(2)
# browser.find_element_by_name("username").send_keys('parvathi11')
# browser.find_element_by_name("password").send_keys('std101')
# browser.find_element_by_name("choice").send_keys('student')
# x='//*[@id="LOGIN"]'
# ele1=browser.find_element_by_xpath(x)
# ele1.click()
# time.sleep(2)


# browser.get('http://127.0.0.1:5000/home')
# time.sleep(2)
# browser.find_element_by_name("username").send_keys('deepakm11')
# browser.find_element_by_name("password").send_keys('fac101')
# browser.find_element_by_name("choice").send_keys('faculty')
# x='//*[@id="LOGIN"]'
# ele1=browser.find_element_by_xpath(x)
# ele1.click()

# from selenium import webdriver
# import time
# browser = webdriver.Chrome('/Users/parvathi/Downloads/chromedriver')

# browser.get('http://127.0.0.1:5000/home')
# time.sleep(2)
# browser.find_element_by_name("username").send_keys('parvathi11')
# browser.find_element_by_name("password").send_keys('std101')
# browser.find_element_by_name("choice").send_keys('student')
# x='//*[@id="LOGIN"]'
# ele1=browser.find_element_by_xpath(x)
# ele1.click()
# time.sleep(2)

# browser.get('http://127.0.0.1:5000/home')
# time.sleep(2)
# browser.find_element_by_name("username").send_keys('deepakm11')
# browser.find_element_by_name("password").send_keys('fac101')
# browser.find_element_by_name("choice").send_keys('faculty')
# x='//*[@id="LOGIN"]'
# ele1=browser.find_element_by_xpath(x)
# ele1.click()
# time.sleep(2)

# browser.get('http://127.0.0.1:5000/dashboard')
# time.sleep(2)
# browser.get('http://127.0.0.1:5000/issues-view-faculty')
# ele1=browser.find_element_by_xpath(x)
# ele1.click()
# time.sleep(2)

# browser.get('http://127.0.0.1:5000/dashboard')
# time.sleep(2)
# browser.get('http://127.0.0.1:5000/od-applications')
# ele1=browser.find_element_by_xpath(x)
# ele1.click()
# time.sleep(2)

# from selenium import webdriver
# import time
# browser = webdriver.Chrome('/Users/parvathi/Downloads/chromedriver')

# browser.get('http://127.0.0.1:5000/home')
# time.sleep(2)
# browser.find_element_by_name("username").send_keys('parvathi11')
# browser.find_element_by_name("password").send_keys('std101')
# browser.find_element_by_name("choice").send_keys('student')
# x='//*[@id="LOGIN"]'
# ele1=browser.find_element_by_xpath(x)
# ele1.click()
# time.sleep(2)

# browser.get('http://127.0.0.1:5000/home')
# time.sleep(2)
# browser.find_element_by_name("username").send_keys('deepakm11')
# browser.find_element_by_name("password").send_keys('fac101')
# browser.find_element_by_name("choice").send_keys('faculty')
# x='//*[@id="LOGIN"]'
# ele1=browser.find_element_by_xpath(x)
# ele1.click()
# time.sleep(2)

# browser.get('http://127.0.0.1:5000/dashboard')
# time.sleep(2)
# browser.get('http://127.0.0.1:5000/issues-view-faculty')
# time.sleep(2)

# browser.get('http://127.0.0.1:5000/dashboard')
# time.sleep(2)
# browser.get('http://127.0.0.1:5000/course_list_for_faculty')

# time.sleep(2)

# browser.get('http://127.0.0.1:5000/dashboard')
# time.sleep(2)
# browser.get('http://127.0.0.1:5000/od-update-date-and-hour')

# time.sleep(2)

# browser.get('http://127.0.0.1:5000/dashboard')
# time.sleep(2)
# browser.get('http://127.0.0.1:5000/change-attendance-status-date-hour-course-form')

# time.sleep(2)

from selenium import webdriver
import time
browser = webdriver.Chrome('/Users/parvathi/Downloads/chromedriver')

browser.get('http://127.0.0.1:5000/home')
time.sleep(2)
browser.find_element_by_name("username").send_keys('parvathi11')
browser.find_element_by_name("password").send_keys('std101')
browser.find_element_by_name("choice").send_keys('student')
x='//*[@id="LOGIN"]'
ele1=browser.find_element_by_xpath(x)
ele1.click()
time.sleep(2)
browser.get('http://127.0.0.1:5000/raise-issue-form')
browser.find_element_by_name("date").send_keys('02/03/2020')
browser.find_element_by_name("time").send_keys('2')
browser.find_element_by_name("fid").send_keys('fac101')
browser.find_element_by_name("cid").send_keys('cse125')
browser.find_element_by_name("remark").send_keys('I was on OD')
x='//*[@id="myDiv"]/form/input[6]'
ele1=browser.find_element_by_xpath(x)
ele1.click()
time.sleep(2)
browser.get('http://127.0.0.1:5000/attendance-report-form')
browser.find_element_by_name("course").send_keys('cse123')
x='/html/body/form/input[2]'
ele1=browser.find_element_by_xpath(x)
ele1.click()
time.sleep(2)
browser.get('http://127.0.0.1:5000/view-issues-students')
time.sleep(2)


browser.get('http://127.0.0.1:5000/home')
time.sleep(2)
browser.find_element_by_name("username").send_keys('deepakm11')
browser.find_element_by_name("password").send_keys('fac101')
browser.find_element_by_name("choice").send_keys('faculty')
x='//*[@id="LOGIN"]'
ele1=browser.find_element_by_xpath(x)
ele1.click()
time.sleep(2)



browser.get('http://127.0.0.1:5000/dashboard')
time.sleep(2)
browser.get('http://127.0.0.1:5000/issues-view-faculty')
time.sleep(2)

browser.get('http://127.0.0.1:5000/dashboard')
time.sleep(2)
browser.get('http://127.0.0.1:5000/course_list_for_faculty')


time.sleep(2)

browser.get('http://127.0.0.1:5000/dashboard')
time.sleep(2)
browser.get('http://127.0.0.1:5000/od-update-date-and-hour')
time.sleep(2)

browser.get('http://127.0.0.1:5000/dashboard')
time.sleep(2)
browser.get('http://127.0.0.1:5000/change-attendance-status-date-hour-course-form')
browser.get('http://127.0.0.1:5000/home')



time.sleep(2)