#!/usr/bin/env python3

import os
from time import sleep

import unittest

from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

import time
import base64

LEFT_NAV_CUSTOM_STUDIO='CUSTOM STUDIO'
LEFT_NAV_SMARTPHONE='智能手機'
LEFT_NAV_APPLE_WATCH='APPLE WATCH'
LEFT_NAV_AIRPODS='AIRPODS'
LEFT_NAV_TECH_ACCESSORIES = '電子產品配件'
LEFT_NAV_SIGNATURE_PRINTS = '經典印花'
LEFT_NAV_FEATURE_ARTIST = '合作藝術家'
LEFT_NAV_CO_LAB = '品牌聯乘'

IDX_FILENAME = 0
left_nav_settings = {
  LEFT_NAV_CUSTOM_STUDIO:['./screenshots/zh_left_nav_menu_custom_studio.jpg'],
  LEFT_NAV_SMARTPHONE :['./screenshots/zh_left_nav_menu_智能手機.jpg'],
  LEFT_NAV_APPLE_WATCH :['./screenshots/zh_left_nav_menu_智能手機.jpg'],
  LEFT_NAV_FEATURE_ARTIST :['./screenshots/zh_left_nav_menu_合作藝術家.jpg'],
  LEFT_NAV_CO_LAB :['./screenshots/zh_left_nav_menu_品牌聯乘.jpg'],
  LEFT_NAV_SMARTPHONE :['./screenshots/zh_left_nav_menu_智能手機.jpg'],
  LEFT_NAV_SIGNATURE_PRINTS :['./screenshots/zh_left_nav_menu_經典印花.jpg'],
  LEFT_NAV_TECH_ACCESSORIES :['./screenshots/zh_left_nav_menu_電子產品配件.jpg']
}

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class CasetifyHelloworld(unittest.TestCase):
    def waitForAppsSteady(self):
      time.sleep(15)

    def waitAfterTapAction(self):
      time.sleep(5)

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
        TouchAction(self.driver).tap(None, 68, 144, 1).perform()
        self.waitAfterTapAction()

    # def test_tapCustomStudio(self):
    #   self.test_tapMenuHamburger()

    #   el = self.selectElByText("CUSTOM STUDIO")
    #   el.click()
    #   self.waitAfterTapAction()
    #   self.takeScreenShot('./screenshots/left_nav_menu_custom_studio.jpg')

    # # # # 智能手機
    def test_tapSmartPhone(self):
      test_settings = left_nav_settings[LEFT_NAV_SMARTPHONE]
      self.tapAndTakeScreenShot(LEFT_NAV_SMARTPHONE, test_settings[IDX_FILENAME])

    # def test_HappyTourLeftNavMenu(self):
    #   for nav_item_name in left_nav_settings.keys():
    #     item_name = nav_item_name
    #     nav_test_settings = left_nav_settings[nav_item_name]
    #     jpg_path = nav_test_settings[IDX_FILENAME]
    #     self.tapAndTakeScreenShot(nav_item_name, jpg_path)

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
