from SCRIPTS.UI_COMMON.self_assessment_1 import *
from SCRIPTS.UI_SCRIPTS.assessment_data_verification import *
from SCRIPTS.COMMON.io_path import *


class SaTest:
    def __init__(self):
        self.browser = None

    def self_assessment(self, tuname, tpass):
        print("inside tenant_login")
        amsin_crpodemo_tenant_url = 'https://amsin.hirepro.in/crpo/#/login/crpodemo'
        self.browser = self_assessment_obj.initiate_browser(amsin_crpodemo_tenant_url, chrome_driver_path)
        print("Initiate browser success")

        login_details = self_assessment_obj.ui_login_to_tenant(tuname, tpass)
        if login_details == 'SUCCESS':
            print("Login to tenant : ", login_details)
            time.sleep(5)
            sprint_id = ''
            while sprint_id == '':
                sprint_id = input('Please enter a valid test name')

            create_test = self_assessment_obj.create_test_sa(sprint_id)

            if create_test == 'success':
                print("Test created")
                # add_question = self_assessment_obj.add_mcq_question()
                # add_grp = self_assessment_obj.add_new_group()
                # add_sec = self_assessment_obj.add_new_section()

                create_mcq_q = self_assessment_obj.create_mcq()
                if create_mcq_q == 'success':
                    create_mcq_q_status = 'success'
                    print("MCQ question created")
                else:
                    create_mcq_q_status = 'success'

                add_mcq_q = self_assessment_obj.add_mcq()
                if add_mcq_q == 'success':
                    print("MCQ question added from local tenant")

                add_mcq_hp_q = self_assessment_obj.add_mcq_hirepro()
                if add_mcq_hp_q == 'success':
                    print("MCQ question added from hirepro tenant")

            self.browser.quit()
            # time.sleep(5)
        else:
            print("Login failed")
            self.browser.quit()


print(datetime.datetime.now())
assessment_obj = SaTest()
# input_file_path = r"F:\qa_automation\PythonWorkingScripts_InputData\UI\Assessment\ui_relogin.xls"
tuser_name = 'suparya'
tpassword = 'New@1234'
assessment_obj.self_assessment(tuser_name, tpassword)
print("main2")

print(datetime.datetime.now())
