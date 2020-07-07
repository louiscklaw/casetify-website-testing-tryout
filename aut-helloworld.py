#!/usr/bin/env python3

import os
from time import sleep

import unittest

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class CasetifyHelloworld(unittest.TestCase):
    def waitForAppsSteady(self):
      time.sleep(15)

    def waitAfterTapAction(self):
      time.sleep(5)

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '/home/logic/_workspace/casetify-tryout/AUT/Casetify Custom Phone Case_v1.6.1_apkpure.com.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.waitForAppsSteady()

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_tapMenuHamburger(self):
        # apps implemented by a webview, no element selector work out
        # 68,144
        # el = self.driver.find_element_by_accessibility_id('Toggle navigation')
        # el.click()
        TouchAction(self.driver).tap(None, 68, 144, 1).perform()
        self.waitAfterTapAction()



    def test_tapCustomStudio(self):
      self.test_tapMenuHamburger()

      el = self.driver.find_element_by_xpath('//android.view.View[@text="CUSTOM STUDIO"]')
      el.click()
      self.waitAfterTapAction()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CasetifyHelloworld)
    unittest.TextTestRunner(verbosity=2).run(suite)
