import unittest

from appium import webdriver
class SimpleAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def step_impl(self):
        SimpleAndroidTests.setUp(self)
        pass

    def test_add_two_numbers_impl(self):
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'1')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'5')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'9')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'9')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'5')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'+')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'6')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'=')]").click()
        assert self.driver.find_element_by_id("com.android.calculator2:id/result").text == "16,001"

