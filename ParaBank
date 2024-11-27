from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


class ParaBan:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def setup(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        print("Test 1 : Open Browser ")


    def login(self):
        self.driver.find_element(By.NAME, "username" ).send_keys("QA")
        self.driver.find_element(By.NAME, "password").send_keys("123456", Keys.ENTER)
        print("Test 2 : Login Success!")

    def account_overview(self):
        time.sleep(2)
        from_acc_number = self.driver.find_element(By.LINK_TEXT, "16563").text
        from_acc_balance =  self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]").text
        from_acc_amount = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]").text
        time.sleep(2)

        to_acc_number = self.driver.find_element(By.LINK_TEXT, "17118").text
        to_acc_balance =  self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]").text
        to_acc_amount = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[2]/td[3]").text

        print("--------From Before Account----------")
        print("Form Account Number : ", from_acc_number)
        print("Form Account Balance : ", from_acc_balance)
        print("From Account Amount: ", from_acc_amount)

        print("--------To Before Account----------")
        print("To Account Number : ", to_acc_number)
        print("To Account Balance : ", to_acc_balance)
        print("To Account Amount: ", to_acc_amount)
        print("Test 3 : Account Over view Success!")


    def open_new_account(self):

        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Open New Account").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/form/select[1]/option[2]").click()
        self.driver.find_element(By.CLASS_NAME, "button").click()
        print("Test 4 : Open New Account Success")


    def transfer(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
        time.sleep(2)
        self.driver.find_element(By.NAME, "input").send_keys("10")
        time.sleep(2)
        select = Select(self.driver.find_element(By.ID, "fromAccountId"))
        select.select_by_visible_text("16563")
        time.sleep(2)
        select = Select(self.driver.find_element(By.ID, "toAccountId"))
        select.select_by_value("17118")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[2]/input").click()
        print("Test 5 : Transfer Success ")

    def verifier(self):
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Accounts Overview").click()
        time.sleep(5)

        from_account = self.driver.find_element(By.LINK_TEXT, "16563").text
        print(1)
        time.sleep(5)

        from_account_balance = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]").text
        print(2)
        time.sleep(5)
        to_account = self.driver.find_element(By.LINK_TEXT, "17118").text
        to_account_balance = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]").text
        print("--------From Account----------")
        print("From Account Account :", from_account)
        print("From Account Balance :", from_account_balance)

        print("--------To Account----------")
        print("To Account Account :", to_account)
        print("To Account Balance :", to_account_balance)


    def main(self):
        self.setup()
        self.login()
        self.account_overview()
        #self.open_new_account()
        self.transfer()
        self.verifier()


ParaBan().main()
