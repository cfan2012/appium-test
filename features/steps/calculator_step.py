import unittest

from behave import *
from appium import webdriver

class CucumberAndroidTests(unittest.TestCase):

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

    @given(u'user open calculator app')
    def open_cacluator_app(self):
        CucumberAndroidTests.setUp(self)
        pass

    @when(u'user input two numbers')
    def add_two_numbers_impl(self):
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'1')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'5')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'9')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'9')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'5')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'+')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'6')]").click()
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'=')]").click()

    @then(u'result is right')
    def step_impl(self):
        assert self.driver.find_element_by_id("com.android.calculator2:id/result").text == "16,002"

    @when(u'user input number {number}')
    def input_number(self,number):
        for i in number:
         self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'" + i + "')]").click()

    @when(u'user use {operation}')
    def step_impl(self,operation):
        xpaths = {
            "add": "//android.widget.Button[contains(@text,'+')]",
            "minus": "//android.widget.Button[contains(@text,'−')]",
            "multiply": "//android.widget.Button[contains(@text,'×')]",
            "divide": "//android.widget.Button[contains(@text,'÷')]"
        }
        xpath = xpaths.get(operation)
        self.driver.find_element_by_xpath(xpath).click()

    @when(u'user calculate result')
    def click_result_button(self):
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'=')]").click()

    @then(u'result should be {result}')
    def step_impl(self,result):
        assert self.driver.find_element_by_id("com.android.calculator2:id/result").text == result