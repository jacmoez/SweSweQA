from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

def click_by_id(driver,idd):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,idd).click()

def click_by_xpath(driver,xpath):
    driver.find_element(AppiumBy.XPATH,xpath).click()

def send_keys_by_xpath(driver,xpath,value):
    driver.find_element(AppiumBy.XPATH,xpath).send_keys(value)


def scroll_element(driver,text):
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
    )