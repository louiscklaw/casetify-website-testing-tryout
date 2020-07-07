#!/usr/bin/env python3

import os
from time import sleep
from pprint import pprint

import unittest

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

import time
import base64

import config
from test_settings import *

from diffimg import diff
from pyunitreport import HTMLTestRunner

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class CasetifyHelloworld(unittest.TestCase):
    def waitForAppsSteady(self):
      time.sleep(config.TIME_APP_STEADY)

    def waitAfterTapAction(self):
      time.sleep(config.TIME_TAP_STEADY)

    def waitUntilTextAppear(self, selector, timeout=15):
      keep_continue = True
      try:
        while keep_continue:
          el = self.driver.find_element_by_xpath(selector)
          time.sleep(1)
          timeout-=1
          keep_continue= False
          return el

      except Exception as e:
        if timeout > 0:
          pass
        else:
          raise e


    def takeScreenShot(self, file_jpg_path):
        screenshotBase64 = self.driver.get_screenshot_as_base64()
        imgdata = base64.b64decode(screenshotBase64)
        with open(file_jpg_path, 'wb') as f:
            f.write(imgdata)

    def selectElByText(self, xpath_selector):
      return self.driver.find_element_by_xpath(xpath_selector)

    def tapAndTakeScreenShot(self, xpath_selector, jpg_path):
      self.tapMenuHamburger()
      self.waitUntilTextAppear(xpath_selector)

      el = self.selectElByText(xpath_selector)
      el.click()
      self.waitAfterTapAction()
      self.takeScreenShot(jpg_path)

    def getLeftNavTestSettings(self, left_nav_text):
      return left_nav_settings[left_nav_text]

    def diffScreenshots(self, screenshot_expect, screenshot_to_test):
      return diff(screenshot_expect, screenshot_to_test)

    def assertScreenshots(self, screenshot_expect, screenshot_to_test, fail_threshold=0.1):
      return self.assertGreater(
        fail_threshold,
        self.diffScreenshots(screenshot_expect, screenshot_to_test)
      )

    def getExpectedScreenshot(self, test_screenshot_filepath):
      return test_screenshot_filepath.replace(TEST_RESULT, TEST_EXPECTED_RESULT)

    # def test_assertScreenshots(self):
    #   png_filename = 'helloworld.png'
    #   result = os.path.join(TEST_RESULT,png_filename)
    #   corr_expected_result = os.path.join(TEST_EXPECTED_RESULT, png_filename)
    #   self.assertScreenshots(
    #     result, corr_expected_result
    #   )

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

    def tapMenuHamburger(self):
        (HAM_X, HAM_Y) = HAMBURGER_BUTTON_XY
        TouchAction(self.driver).tap(None, HAM_X, HAM_Y, 1).perform()
        self.waitAfterTapAction()

    # util self test
    # def test_tapMenuHamburger(self):
    #     # apps implemented by a webview, no element selector work out
    #     # 68,144
    #     # el = self.driver.find_element_by_accessibility_id('Toggle navigation')
    #     # el.click()
    #     self.tapMenuHamburger()

    # test app
    def tapNavItemAndTest(self, test_settings):
      screenshot_filename = test_settings[IDX_FILENAME]
      xpath_selector = test_settings[IDX_SELECTOR]

      self.tapAndTakeScreenShot(xpath_selector, screenshot_filename)

      self.assertScreenshots(
        self.getExpectedScreenshot(screenshot_filename),
        screenshot_filename
      )

    # CUSTOM STUDIO
    def test_tapCustomStudio(self):
      test_settings = left_nav_settings[LEFT_NAV_CUSTOM_STUDIO]
      self.tapNavItemAndTest(test_settings)

    # 合作藝術家
    def test_tapFeatureArtist(self):
      test_settings = left_nav_settings[LEFT_NAV_FEATURE_ARTIST]
      self.tapNavItemAndTest(test_settings)

    # 品牌聯乘
    def test_tapCoLab(self):
      test_settings = left_nav_settings[LEFT_NAV_CO_LAB]
      self.tapNavItemAndTest(test_settings)

    # 智能手機
    def test_tapSmartPhone(self):
      test_settings = left_nav_settings[LEFT_NAV_SMARTPHONE]
      self.tapNavItemAndTest(test_settings)

    # 經典印花
    def test_tapSignaturePrints(self):
      test_settings = left_nav_settings[LEFT_NAV_SIGNATURE_PRINTS]
      self.tapNavItemAndTest(test_settings)

    # 電子產品配件
    def test_tapTechAccessories(self):
      test_settings = left_nav_settings[LEFT_NAV_TECH_ACCESSORIES]
      self.tapNavItemAndTest(test_settings)

if __name__ == '__main__':
  # normal test runner
  # suite = unittest.TestLoader().loadTestsFromTestCase(CasetifyHelloworld)
  # unittest.TextTestRunner(verbosity=2).run(suite)

  # html test runner
  unittest.main(testRunner=HTMLTestRunner(output='../docs'))