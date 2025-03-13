from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from pick.Locations import  *
from pick.helper import  *
options = UiAutomator2Options()
options.set_capability("appium:ignoreHiddenApiPolicyError", True)
URL = 'http://127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options)
# phone="80008000"
phone="80808080"
# phone="82311355"
def login_or_create_acc():
    click_by_id(driver,login_or_create_acc_path['login_icon_path'])
    send_keys_by_xpath(driver,login_or_create_acc_path['phone_number_path'],phone)
    click_by_xpath(driver,login_or_create_acc_path['next_btn_path'])

def otp():
    click_by_xpath(driver,otp_path["get_otp_path"])
    time.sleep(3)
    send_keys_by_xpath(driver,otp_path['otp_code_path'],'111111')
    time.sleep(10)
    click_by_xpath(driver,otp_path['checkbox_path'])
    time.sleep(2)
    click_by_xpath(driver,otp_path['got_it_path'])
    time.sleep(3)
    click_by_xpath(driver,otp_path['skip_path'])
    time.sleep(3)

def register():
    login_or_create_acc()
    click_by_xpath(driver,otp_path["get_otp_path"])
    time.sleep(3)
    send_keys_by_xpath(driver,otp_path['otp_code_path'],'111111')
    time.sleep(3)
    send_keys_by_xpath(driver,register_path['first_name_path'],"Shwe")
    send_keys_by_xpath(driver,register_path['last_name_path'],"Shwe")
    send_keys_by_xpath(driver,register_path['email_path'],f"shwezin{phone}@yopmail.com")
    send_keys_by_xpath(driver,register_path['postal_code_path'],'123456')
    click_by_xpath(driver,register_path['mail_checkbox_path'])
    scroll_element(driver,'Next')



