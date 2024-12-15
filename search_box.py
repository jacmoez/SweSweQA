from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestSearchBox:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def test_open_browser(self,):
        self.driver.get("https://web-staging.renonation.sg/")
        self.driver.maximize_window()
        
    def test_search_box(self):
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".custom-react-select__control.css-1xjxcct-control").click()
        time.sleep(2)

        # property_type
        self.driver.find_element(By.XPATH, "//*[text()='HDB']").click()
        time.sleep(2)

        #Style
        style_path = "/html/body/div/div/main/section[1]/div[2]/div/form/div[2]/div[1]/fieldset/div/div/div/div"
        self.driver.find_element(By.XPATH, style_path).click()
        self.driver.find_element(By.XPATH, "//*[text()='Asian']").click()
        self.driver.find_element(By.XPATH, style_path).click()
        self.driver.find_element(By.XPATH, "//*[text()='Country']").click()
        time.sleep(2)

        #Budget
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/div/form/div[2]/div[2]/fieldset/div/div/div").click()
        self.driver.find_element(By.XPATH, "//*[text()='S$30,000 - S$40,000']").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/div/form/button").click()
        time.sleep(5)
        text = self.driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/section/div/h6").text
        print(text)
        print("Search Complete")

    def test_project_detail(self):
        self.driver.find_element(By.XPATH,"/html/body/div/div/main/section[2]/section/div/div[1]/div/div/div[3]").click()
        time.sleep(3)
        title = self.driver.find_element(By.CSS_SELECTOR, ".header-h3-regular.text-white").text
        print(title)
        detail = self.driver.find_element(By.CLASS_NAME, "header-h6-bold").text
        print(detail)


    def test_main(self):
        self.test_open_browser()
        self.test_search_box()
        self.test_project_detail()
        time.sleep(10)


TestSearchBox().test_main()