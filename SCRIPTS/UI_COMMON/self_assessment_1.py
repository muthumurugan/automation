import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class SelfAssessmentLogin:
    def __init__(self):
        self.delay = 120

    def initiate_browser(self, url, path):
        # chrome option is needed in VET cases - ( its handling permissions like mic access)
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return self.driver

    def ui_login_to_tenant(self, user_name, password):
        time.sleep(5)
        try:
            # To select vendors/tpo/placecom option before login page
            self.driver.find_element(By.XPATH, '//*[contains(text(), "Vendors/TPO/Placecom")]').click()
            time.sleep(2)
            self.driver.find_element(By.NAME, 'loginName').clear()
            self.driver.find_element(By.NAME, 'loginName').send_keys(user_name)
            self.driver.find_element(By.XPATH, "//input[@type='password']").clear()
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-default button_style login ng-binding"]').click()
            # self.driver.find_element_by_class_name('btn btn-default button_style login ng-binding').click()
            time.sleep(5)
            login_status = 'SUCCESS'

        except Exception as e:
            print(e)
            login_status = 'FAILED'
        return login_status

    def create_test_sa(self, testname):
        time.sleep(2)
        # value = "automation" % testname
        try:
            # select new test
            self.driver.find_element(By.XPATH,
                                     '//*[@class = "btn-group show_form no-padding pointer btn button_radius ng-binding ng-scope"]').click()
            time.sleep(15)
            # Enter test name
            self.driver.find_element(By.XPATH,
                                     '//*[@class = "form-control ng-pristine ng-untouched ng-valid ng-empty"]').send_keys(
                testname)
            time.sleep(5)
            # create test
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-primary_"]').click()
            time.sleep(15)
            test_status = 'success'

        except Exception as e:
            print(e)
            test_status = 'failed'
        return test_status

    def select_plus(self, index):
        try:
            plus = self.driver.find_elements(By.XPATH, '//*[@class = "fa fa-plus"]')
            plus[index].click()
            return 'success'

        except Exception as e:
            print(e)

        return 'failed'

    def create_mcq(self):
        try:
            print("create mcq")
            # add question - mcq
            time.sleep(5)
            self_assessment_obj.select_plus(2)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@class = "tab-option"]').click()
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-default dropdown-toggle pull-right"]').click()
            difficulty = self.driver.find_element(By.XPATH,
                                                  '//*[@class = "dropdown-menu ng-scope am-fade bottom-left"]')
            time.sleep(2)
            if difficulty.is_displayed():
                ele = self.driver.find_element(By.XPATH, '//a[@title="Low"]')
                ele.click()
                print("selected difficulty")
            else:
                print("not selected")

            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-default btn-sm"]').click()
            time.sleep(2)
            ele2 = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Question Description']")
            ele2.send_keys("mcq sa automation don't use /ans : B ")
            time.sleep(5)

            elements = self.driver.find_elements(By.XPATH,
                                                 "//textarea[@class='form-control ng-pristine ng-untouched ng-valid ng-empty']")
            c = 1
            for e in elements:
                e.send_keys(c)
                c += 1
            time.sleep(2)

            option = self.driver.find_elements(By.XPATH, "//*[@name='answer']")
            option[1].click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-default btn-success btn-sm ng-scope"]').click()

            time.sleep(10)

            return 'success'

        except Exception as e:
            print(e)

        return 'failed'

    def add_mcq(self):
        try:
            print("Add mcq question")
            # add question - mcq
            time.sleep(5)
            self_assessment_obj.select_plus(2)
            time.sleep(2)
            qid = self.driver.find_element(By.XPATH, '//*[@type="text"]')
            qid.send_keys("136095")
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-primary_ pull-right"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@name="grid_items"]').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-success_ pull-right"]').click()

            time.sleep(10)

            return 'success'

        except Exception as e:
            print(e)

        return 'failed'

    def add_mcq_hirepro(self):
        try:
            print("Add mcq question from hirepro tenant")
            # add question - mcq
            time.sleep(5)
            self_assessment_obj.select_plus(2)
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[contains(text(), "Hirepro Library")]').click()
            time.sleep(2)
            qid = self.driver.find_element(By.XPATH, '//*[@type="text"]')
            qid.send_keys("136097")
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-primary_ pull-right"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '//*[@name="grid_items"]').click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-success_ pull-right"]').click()

            time.sleep(10)

            return 'success'

        except Exception as e:
            print(e)

        return 'failed'

    def add_new_group(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, '//*[@class = "btn btn-link ng-scope"]').click()
            time.sleep(2)
            test_status = 'success'

        except Exception as e:
            print(e)
            test_status = 'failed'
        return test_status

    def add_new_section(self):
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, '//*[contains(text(), "Add Section")]"]').click()
            time.sleep(2)

        except Exception as e:
            print(e)
            test_status = 'failed'
        return test_status


self_assessment_obj = SelfAssessmentLogin()
