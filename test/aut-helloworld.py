#!/usr/bin/env python3

import os
from time import sleep

import unittest

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

import time
import base64

import config
from test_settings import *


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class CasetifyHelloworld(unittest.TestCase):
    def waitForAppsSteady(self):
      time.sleep(config.TIME_APP_STEADY)

    def waitAfterTapAction(self):
      time.sleep(config.TIME_TAP_STEADY)

    def takeScreenShot(self, file_jpg_path):
        screenshotBase64 = self.driver.get_screenshot_as_base64()
        imgdata = base64.b64decode(screenshotBase64)
        with open(file_jpg_path, 'wb') as f:
            f.write(imgdata)

    def selectElByText(self, text_wanted):
      return self.driver.find_element_by_xpath('//android.view.View[@text="'+text_wanted+'"]')

    def tapAndTakeScreenShot(self, left_nav_menu_text, jpg_path):
      self.test_tapMenuHamburger()

      el = self.selectElByText(left_nav_menu_text)
      el.click()
      self.waitAfterTapAction()
      self.takeScreenShot(jpg_path)

    def getLeftNavTestSettings(self, left_nav_text):
      return left_nav_settings[left_nav_text]

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
        (HAM_X, HAM_Y) = HAMBURGER_BUTTON_XY
        TouchAction(self.driver).tap(None, HAM_X, HAM_Y, 1).perform()
        self.waitAfterTapAction()

    def test_tapCustomStudio(self):
      self.test_tapMenuHamburger()

      el = self.selectElByText("CUSTOM STUDIO")
      el.click()
      self.waitAfterTapAction()
      self.takeScreenShot('./screenshots/left_nav_menu_custom_studio.jpg')

    # # # # # 智能手機
    # def test_tapSmartPhone(self):
    #   test_settings = left_nav_settings[LEFT_NAV_SMARTPHONE]
    #   self.tapAndTakeScreenShot(LEFT_NAV_SMARTPHONE, test_settings[IDX_FILENAME])

    # 合作藝術家
    def test_tapFeatureArtist(self):
      test_settings = left_nav_settings[LEFT_NAV_FEATURE_ARTIST]
      self.tapAndTakeScreenShot(LEFT_NAV_FEATURE_ARTIST, test_settings[IDX_FILENAME])

    # 品牌聯乘
    def test_tapCoLab(self):
      test_settings = left_nav_settings[LEFT_NAV_CO_LAB]
      self.tapAndTakeScreenShot(LEFT_NAV_CO_LAB, test_settings[IDX_FILENAME])

    # 智能手機
    def test_tapSmartPhone(self):
      test_settings = left_nav_settings[LEFT_NAV_SMARTPHONE]
      self.tapAndTakeScreenShot(LEFT_NAV_SMARTPHONE, test_settings[IDX_FILENAME])

    # 經典印花
    def test_tapSignaturePrints(self):
      test_settings = left_nav_settings[LEFT_NAV_SIGNATURE_PRINTS]
      self.tapAndTakeScreenShot(LEFT_NAV_SIGNATURE_PRINTS, test_settings[IDX_FILENAME])

    # 電子產品配件
    def test_tapTechAccessories(self):
      test_settings = left_nav_settings[LEFT_NAV_TECH_ACCESSORIES]
      self.tapAndTakeScreenShot(LEFT_NAV_TECH_ACCESSORIES, test_settings[IDX_FILENAME])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CasetifyHelloworld)
    unittest.TextTestRunner(verbosity=2).run(suite)
