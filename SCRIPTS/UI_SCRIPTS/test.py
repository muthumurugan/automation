from SCRIPTS.UI_COMMON.assessment_ui_common_v2 import *


class FileUpload:
    def __init__(self):
        self.url = "https://amsin.hirepro.in/crpo/#/AT/candidates/create"
        self.path = r"F:\qa_automation\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=chrome_options)
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # return self.driver
        # self.driver = assess_ui_common_obj.initiate_browser(self.url, self.path)
        # time.sleep(8)
        # self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, 'loginName').clear()
        self.driver.find_element(By.NAME, 'loginName').send_keys("admin")
        self.driver.find_element(By.XPATH, "//input[@type='password']").clear()
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys('At@2023$$')

        # self.driver.find_element(By.XPATH, "//*[@type = password]").send_keys("At@2023$$")
        self.driver.find_element(By.XPATH, '//*[@id="mainBodyElement"]/div[3]/section/div[1]/div[2]/form/div[3]/a').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.LINK_TEXT, "Choose File").click()



obj = FileUpload()
