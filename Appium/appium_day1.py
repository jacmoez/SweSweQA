import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.set_capability("appium:ignoreHiddenApiPolicyError", True)
URL = 'http://127.0.0.1:4723'
driver = webdriver.Remote(URL, options=options)

package_name = "com.picknetwork.android.dev"

#VariableSetUp
login_cta_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]"

mobile_textbox_xpath = "//android.widget.EditText"

invalid_mobile_msg_xpath = '//android.widget.TextView[@text="Please enter a valid mobile number/email address."]'

next_btn_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button"

get_otp_btn_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button"

opt_box_xpath = "//android.widget.EditText"

biometrics_no_btn_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button"

acknowledge_checkbox_xpath = "//android.widget.CheckBox"

got_it_btn_xpath = "//android.widget.Button"

more_menu_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[2]"

logout_cta_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[9]"

logout_yes_btn_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button"

what_up_cta_xpath = '//android.widget.TextView[@text="What\'s Up"]'

what_up_latest_menu_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[3]"

latest_details_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View"

what_up_promotions_menu_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]"

promotion_details_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]"

what_up_coming_soon_menu_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]"

back_cta_xpath = '//android.view.View[@content-desc="arrow back"]'

notification_icon_xpath = "//android.widget.Button"

notification_one_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]"

notification_delete_xpath = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.Button"

notification_cancel_delete_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button"

notification_yes_delete_xpath = "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button"

skip = '//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button'

def install_app():



#install app
    print("--------------------------install--------------------")
    driver.install_app("C:/Users/DELL/Downloads/app-staging-debug.apk")
    time.sleep(5)
    print("App is installed? : ", driver.is_app_installed(package_name))

def uninstall_app():
    print("---------------------uninstall-----------------------")
    if driver.is_app_installed(package_name):
        driver.remove_app(package_name)
        print("Uninstall")

options.set_capability("appPackage",package_name)
options.set_capability("appWaitActivity","com.picknetwork.android.dev.*")

def open_and_activate():
     driver.launch_app()
     time.sleep(2)
     print("App is launched ")
     driver.activate_app(package_name)
     print("App is activate")
     # time.sleep(20)
     # driver.terminate_app(package_name)

def get_read_to_pick():
    time.sleep(5)

    #next 1
    next_btn_path = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button'


    driver.find_element(AppiumBy.XPATH, next_btn_path).click()


    #next 2
    driver.find_element(AppiumBy.XPATH, next_btn_path).click()

    #Pick You
    driver.find_element(AppiumBy.CSS_SELECTOR, ".android.widget.Button").click()
    print("--------------Get Ready-------------------")

def login():
    driver.find_element(AppiumBy.XPATH,login_cta_xpath).click()
    time.sleep(10)#Click Login or Sign Up CTA
    driver.find_element(AppiumBy.XPATH,mobile_textbox_xpath).send_keys("8000")
    time.sleep(10)#Enter invalid mobile number
    invalid = driver.find_element(AppiumBy.XPATH,invalid_mobile_msg_xpath).text #Print out invalid mobile number text msg
    print("Test Case 1:", invalid)
    time.sleep(10)
    driver.find_element(AppiumBy.XPATH,mobile_textbox_xpath).clear() #Clear mobile number textbox
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,mobile_textbox_xpath).send_keys("80008000") #Enter valid mobile number
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,next_btn_xpath).click() #Click Next button
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,get_otp_btn_xpath).click() #Click OTP confirmation popup box
    time.sleep(3)
    print("Test Case 2: Navigate to OTP screen")
    driver.find_element(AppiumBy.XPATH,opt_box_xpath).send_keys("111111") #Enter OTP value
    time.sleep(10)
    #driver.find_element(AppiumBy.XPATH,biometrics_no_btn_xpath).click()
    #time.sleep(10)#Click biometric not accept btn
    #print("Test Case 3: Login Successful")
    driver.find_element(AppiumBy.XPATH,acknowledge_checkbox_xpath).click()
    time.sleep(3)#Check acknowledge checkbox
    driver.find_element(AppiumBy.XPATH,got_it_btn_xpath).click()
    time.sleep(3)#Click Got it btn
    driver.find_element(AppiumBy.XPATH, skip).click()

def logout():
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH,more_menu_xpath).click()
    time.sleep(3)#Click More menu
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Log out"))'
    )
    #Scroll down
    driver.find_element(AppiumBy.XPATH,logout_cta_xpath).click()
    time.sleep(3)#Click logout CTA
    driver.find_element(AppiumBy.XPATH,logout_yes_btn_xpath).click()
    time.sleep(3)#Click logout confirmation popup box
    print("Test Case 4: Logout Successful")




#install_app()
#open_and_activate()
login()
logout()
#get_read_to_pick()
#uninstall_app()


