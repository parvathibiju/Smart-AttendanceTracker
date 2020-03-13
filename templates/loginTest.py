from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import time


class testcase(unittest.TestCase):
    def setupclass(self):
        #dir=os.path.dirname(os.path.abspath(__file__))
        self.driver=webdriver.Safari()
        self.driver.implicitly_wait(5)
        #print("helooo")
        self.driver.maximize_window()
        #self.driver.get("http://www.google.com/")

    def test_login(self,username,password):
        #print('@@@####')
        self.driver=webdriver.Safari()
        self.driver.get("http://localhost:5000/home")
        u_name_field=self.driver.find_element_by_id("username")
        u_name_field.send_keys(username)
        self.driver.implicitly_wait(2)
        p_name_field = self.driver.find_element_by_id("password")
        p_name_field.send_keys(password)
        submit=self.driver.find_element_by_id("LOGIN")
        submit.click()

    def test_studentlogin(self):
        print("***")
        self.driver=webdriver.Safari()
        self.test_login("parvathis11","std101")
        self.driver.implicitly_wait(5)
        text=self.driver.find_element_by_id("greeting").text
        self.assertEqual(text,"Welcome")
        self.driver.implicitly_wait(5)
        #self.logout()
        
    def test_facultylogin(self):
        self.driver=webdriver.Safari()
        self.driver.get("http://localhost:5000/home")
        self.test_login("deepakm11", "fac101")
        self.driver.implicitly_wait(2)
        text = self.driver.find_element_by_id("greeting").text
        self.assertEqual(text, "Welcome")
        self.driver.implicitly_wait(2)
        #self.logout()
   

    def test_invalid_login(self):
        self.driver=webdriver.Safari()
        self.driver.get("http://localhost:5000/home")
        self.test_login("sanj", "sam")
        self.driver.implicitly_wait(5)
        text = self.driver.find_element_by_id("wrong").text
        self.assertEqual(text, "Invalid!")

    def tearDown(self):
        self.driver=webdriver.Safari()
        self.driver.quit()

if __name__=='__main__' :
    unittest.main(verbosity=2)






