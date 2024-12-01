from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRenovation:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def test_open_browser(self):
        self.driver.get("https://web-staging.renonation.sg/")

    def test_login(self):
        mobile_text_box = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/div/div/input"
        mobile_btn = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button"
        opt_path = "/html/body/div/div/div[3]/div/div/form[2]/div/div/fieldset/div/div[2]/ul/li["
        otp_digits = ["2","3", "2", "3", "2", "3"]
        otp_input_path = "/html/body/div/div/div[3]/div/div/form[2]/div/div/fieldset/div/div[2]/input"


        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("8311 ")
        self.driver.find_element(By.XPATH, mobile_btn).click()
        invalid = self.driver.find_element(By.CSS_SELECTOR, ".flex-1.text-sm.text-error").text
        self.driver.find_element(By.XPATH, mobile_text_box).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, mobile_text_box).send_keys("83113345")
        self.driver.find_element(By.XPATH, mobile_btn).click()
        time.sleep(2)
        opt_input = self.driver.find_element(By.XPATH, otp_input_path)
        opt_input.send_keys("".join(otp_digits))


        for i,opt_digit in enumerate(otp_digits, start=1):

            li_path = f"{opt_path}{i}]"
            print('Li path ',li_path)
            opt_element = self.driver.find_element(By.XPATH, li_path)
            self.driver.execute_script("arguments[0].textcontent = arguments[1];", opt_element, opt_digit)

        print("Hello ")
        opt_continue = self.driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div/form[2]/div/div/button")
        opt_continue.click()

        print(invalid)
        print("Test 2 : ", " Login Success!")

    def test_main(self):
        self.test_open_browser()
        self.test_login()


TestRenovation().test_main()