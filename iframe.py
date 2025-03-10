from pyotp import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select


class TestYoGa:

    driver = webdriver.Edge()

    def test_open_browser(self):
        self.driver.get("https://webfront-uat.yogamovement.com/")
        self.driver.maximize_window()
        #Alearg Close
        self.driver.find_element(By.XPATH, "/html/body/div/div/aside/div/div[2]/button").click()
        print("Test 1 : Open browser success!")


    #Buy A Class Pack
    def test_buy_class(self):
        #Login in
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "email").send_keys("waiwai60@yopmail.com")
        time.sleep(1)
        self.driver.find_element(By.NAME, "password").send_keys("Phy123", Keys.ENTER)
        time.sleep(3)

        #Buy a class pack
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[2]/ul/li[3]/a").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='Buy A Class Pack']").click()
        time.sleep(5)

        #All Access Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/ul/li[2]/a").click()
        time.sleep(3)

        #All Access Pass + Free Gift Git
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div/div[3]/section[2]/div[2]/div[1]/div[4]/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/form/button").click()
        time.sleep(5)


    def test_payment_method(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/button").click()
        time.sleep(2)

        js_code = """let element = document.querySelector("input[name='hidden']");
        element.disabled = false;
       return element;"""


        iframe1 = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure card number input frame']")
        self.driver.switch_to.frame(iframe1)
        time.sleep(2)
        self.driver.execute_script(js_code)
        self.driver.find_element(By.NAME, "cardnumber").send_keys("4111111111111111")
        time.sleep(3)



        self.driver.switch_to.default_content()
        iframe2 = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure expiration date input frame']")
        self.driver.switch_to.frame(iframe2)
        time.sleep(2)
        self.driver.execute_script(js_code)
        self.driver.find_element(By.NAME, "exp-date").send_keys("11/26`")
        time.sleep(2)


        self.driver.switch_to.default_content()
        iframe3 = self.driver.find_element(By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame'][title='Secure CVC input frame']")
        self.driver.switch_to.frame(iframe3)
        time.sleep(2)
        self.driver.execute_script(js_code)
        self.driver.find_element(By.NAME, "cvc").send_keys("123")


    def test_register_test(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/header/div[2]/div/div/nav[1]/ul/li[1]/a").click()

        #Ramdom Email

        user_email = [random.randint(0,9) for i in range(3)]
        num = "".join(str(x) for x in user_email)


        self.driver.find_element(By.NAME, "email").send_keys("waiwai", num, "@yopmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Phy123", Keys.RETURN)
        time.sleep(3)

        #First Name
        self.driver.find_element(By.NAME, "firstname").send_keys("QA")
        time.sleep(3)

        #Last Name
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[1]/label/input").send_keys("Wai Wai")
        time.sleep(2)

        #Email Check
        email = self.driver.find_element(By.NAME,"email")
        val = email.get_attribute("value")
        if val == user_email : print("Email Match")
        else : print("Not Email Match")

        #I Identify as
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[4]/div/div/div[2]/div/div[2]/label/div/div").click()
        time.sleep(2)

        #Country
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[1]/div[2]").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[1]/input").send_keys("Myanmar")
        time.sleep(2)

        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[1]/div[3]/label/div[1]/div[2]/div[4]").click()

        #Mobile Number
        phone_number = [random.randint(0,9) for i in range(9)]
        num = "".join(str(x) for x in phone_number)
        self.driver.find_element(By.NAME, "mobile").send_keys("9",num)
        time.sleep(2)

        #DOB
        self.driver.find_element(By.ID, "dob").click()
        time.sleep(2)

        #Year
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]/option[74]").click()
        time.sleep(2)

        Select(self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[2]")).select_by_value("1998")


        time.sleep(2)
        Select(self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/select[1]")).select_by_value("10")

        time.sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[2]/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div[4]").click()
        time.sleep(2)


        #Home Country
        self.driver.find_element(By.CLASS_NAME, "css-egispl").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//img[@src='https://s3.ap-southeast-1.amazonaws.com/yogamovement-app.com.staging/Country/flag-hk.png']" ).click()

        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[6]/div/button").click()
        time.sleep(2)
        text= self.driver.find_element(By.CSS_SELECTOR, ".terms__title.text-uppercase").text
        time.sleep(2)

        self.driver.find_element(By.NAME, "name").send_keys(Keys.RETURN)
        time.sleep(2)

        err_name = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[1]/label[1]/div[2]").text
        print(err_name)

        time.sleep(2)
        err_mobile = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[1]/label[2]/div[2]").text
        print(err_mobile)
        time.sleep(2)
        self.driver.find_element(By.NAME, "name").send_keys("QA Wai Wai")
        time.sleep(2)
        self.driver.find_element(By.NAME, "mobile").send_keys("959796686061")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/div[2]/div/label/div/div").click()
        print(text)
        #btn Click
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div/div/main/form/div/div[3]/div/button").click()

        print("Go to next page successfully")





    def test_main(self):
        self.test_open_browser()
        self.test_buy_class()
        self.test_payment_method()

        #self.test_register_test()
        time.sleep(10)

TestYoGa().test_main()

