#!/usr/bin/env python3

import os
from time import sleep

import unittest

from appium import webdriver

import base64

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '/home/logic/_workspace/casetify-tryout/AUT/ApiDemos-debug.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_find_elements(self):
        el = self.driver.find_element_by_accessibility_id('Graphics')
        el.click()
        el = self.driver.find_element_by_accessibility_id('Arcs')
        self.assertIsNotNone(el)

        self.driver.back()

        el = self.driver.find_element_by_accessibility_id("App")
        self.assertIsNotNone(el)

        els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
        self.assertGreaterEqual(12, len(els))

        self.driver.find_element_by_android_uiautomator('text("API Demos")')


    def test_simple_actions(self):
        el = self.driver.find_element_by_accessibility_id('Graphics')
        el.click()

        el = self.driver.find_element_by_accessibility_id('Arcs')
        el.click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Graphics/Arcs")')

    def test_takeScreenShot(self):
        screenshotBase64 = self.driver.get_screenshot_as_base64()
        imgdata = base64.b64decode(screenshotBase64)
        filename = './appium_screenshot_helloworld.jpg'
        with open(filename, 'wb') as f:
            f.write(imgdata)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
