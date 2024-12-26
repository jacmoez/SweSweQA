import time
from seleniumbase import BaseCase

class TestReno(BaseCase):
    def test_main(self):
        self.open("https://web-staging.renonation.sg/")
        self.maximize_window()
        time.sleep(2)
        # self.click("/html/body/div/div/div[2]/div/header/div/div[2]/div/button[2]")
        # self.type("name=mobile","8311")
        # mobile_btn = "/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/button"
        # self.click(mobile_btn)
        # err_mes = self.get_text("/html/body/div/div/div[3]/div/div/form[1]/div/div/div[1]/fieldset/p/span")
        # self.type("name=mobile","83115546")
        # time.sleep(1)
        # self.click(mobile_btn)
        # time.sleep(2)
        #
        # js_code = """ let opt_input = document.querySelector("input[name='otp']")
        # opt_input.style.opacity ="1" """
        # self.execute_script(js_code)
        # self.type("name=otp", "232323")
        # time.sleep(1)
        # self.click("/html/body/div/div/div[3]/div/div/form[2]/div/div/button")
        # time.sleep(2)
        # print("Login Success!")
        # self.click("/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[1]/div")
        # time.sleep(1)
        # self.click("/html/body/div/div/div[2]/div/header/div/div[2]/div/div[2]/div/div[2]/div")
        # time.sleep(1)
        # self.click("/html/body/div/div/div[4]/div[2]/form/div/div/button[2]")
        # time.sleep(3)

        #self.scroll_to(".custom-react-select__control css-1xjxcct-control")
        self.click("/html/body/div/div/main/section[1]/div[2]/div/form/div[1]/fieldset/div/div/div")
        time.sleep(3)
        self.click("//*[text()='DBSS']")
        time.sleep(2)
        style_path = "/html/body/div/div/main/section[1]/div[2]/div/form/div[2]/div[1]/fieldset/div/div/div/div"
        self.click(style_path)
        self.click("//*[text()='Asian']")



        time.sleep(10)



