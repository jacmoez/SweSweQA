from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

class TestRenovation:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def test_open_browser(self,):
        self.driver.get("https://web-staging.renonation.sg/")
        self.driver.maximize_window()

    def test_login(self):

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input").send_keys("311")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button").click()
        invalid = self.driver.find_element(By.CSS_SELECTOR, ".flex-1.text-sm.text-error").text
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input").send_keys("83115546")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "otp").send_keys("232323")
        otp_btn = "/html/body/div/div/div[3]/div/div/form[2]/div/div/button"

        self.driver.find_element(By.XPATH,otp_btn ).click()

        print(invalid)
        print("Test 2: Login Success!")


    def test_login_verify(self):

        my_profile = "/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[1]/div/span"
        self.driver.find_element(By.XPATH, my_profile).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[2]/a[1]/div/div/div").click()

        #URL Verify
        my_profile_url = "https://web-staging.renonation.sg/my-profile"
        time.sleep(2)
        url = self.driver.current_url
        if my_profile_url == url : print("Login Success!")
        else : print("Login Fail!")

        self.driver.find_element(By.XPATH, my_profile).click()

        #Login Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[2]/div").click()

        #Login btn
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[2]/form/div/div/button[2]").click()

        print("Test 3 : Login Verify")

    def test_sing_up(self):

        mobile_number_path = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input"

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]").click()
        self.driver.find_element(By.XPATH, mobile_number_path).send_keys("8311")


        #Random Number

        phone_number = [random.randint(0,9) for _ in range(4)]
        num = "".join(str(x) for x in phone_number)
        time.sleep(2)
        self.driver.find_element(By.XPATH, mobile_number_path).send_keys(num)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "otp").send_keys("232323")
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/form[2]/div/div/button" ).click()

    def test_step_one(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "firstName").send_keys("Swe")
        time.sleep(2)
        self.driver.find_element(By.ID, "lastName").send_keys("Swe")

        email = "sweswe"
        email_num = [random.randint(0,9) for _ in range(2)]
        num = "".join(str(x) for x in email_num)

        self.driver.find_element(By.ID, "email").send_keys(email,num,"@yopmail.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div[2]/button").click()
        print("Test 4 : Step One Complete")

    def test_step_two(self):
        #Property type
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form[2]/div/div[2]/div/div[1]/div/fieldset[1]/div/button[3]").click()
        time.sleep(2)

       #2 No. of Bedrooms
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form[2]/div/div[2]/div/div[1]/div/div/fieldset/div/button[5]").click()
        time.sleep(2)

        #3 Property Status
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form[2]/div/div[2]/div/div[1]/div/fieldset[2]/div/button[1]").click()

        #Yes Key
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/div/form[2]/div/div[2]/div/div[1]/div/fieldset[3]/div/button[1]").click()


    def test_main(self):
        self.test_open_browser()
        #self.test_login()
        #self.test_login_verify()
        self.test_sing_up()
        self.test_step_one()
        self.test_step_two()


TestRenovation().test_main()

# import random
#
# phone_number = [random.randint(0,9) for _ in range(4)]
# print(phone_number)
# num = "".join(str(x) for x in phone_number)
# print(num)


