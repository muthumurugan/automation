from SCRIPTS.CRPO_COMMON.crpo_common import *
from SCRIPTS.CRPO_COMMON.credentials import *
from SCRIPTS.COMMON.read_excel import *
from SCRIPTS.COMMON.write_excel_new import *
from SCRIPTS.COMMON.io_path import *
from SCRIPTS.CRPO_COMMON.behavioural_proc_eval_config import *
import datetime


class ProctorEvaluation:
    def __init__(self):
        print(datetime.datetime.now())
        write_excel_object.save_result(output_path_behaviour_proctor_evaluation_new)
        # 0th Row Header
        header = ['Proctoring Evaluation automation']
        # 1 Row Header
        write_excel_object.write_headers_for_scripts(0, 0, header, write_excel_object.black_color_bold)
        header = ['Testcases', 'Status', 'Test ID', 'Candidate ID', 'Testuser ID', 'Behaviour type ',
                  'Expected behaviour proctoring status',
                  'Actual behaviour proctoring status',
                  'Expected overall proctoring status',
                  'Actual overall proctoring status', 'Expected overall rating', 'Actual overall rating']

        write_excel_object.write_headers_for_scripts(1, 0, header, write_excel_object.black_color_bold)

    def suspicious_or_not_supicious(self, data, overall_proctoring_status_value):
        if data is True:
            # only overall proctoring status has number value.
            if overall_proctoring_status_value is False:
                self.status = 'Suspicious'
            else:
                if overall_proctoring_status_value >= 0.66:
                    self.status = 'Highly Suspicious'

                elif overall_proctoring_status_value >= 0.35:
                    self.status = 'Medium'

                elif overall_proctoring_status_value > 0:
                    self.status = 'Low'
                else:
                    self.status = 'Not Suspicious'
        else:
            self.status = 'Not Suspicious'

    def proctor_detail(self, row_count, current_excel_data, token):
        write_excel_object.current_status_color = write_excel_object.green_color
        write_excel_object.current_status = "Pass"
        tu_id = int(current_excel_data.get('testUserId'))
        print(tu_id)
        tu_proctor_details = crpo_common_obj.proctor_evaluation_detail(token, tu_id)
        proctorDetail = tu_proctor_details['data']['proctorDetail']

        if current_excel_data.get('is_video_behaviour') == 'No':
            write_excel_object.compare_results_and_write_vertically('behavior suspicious', None,
                                                                    row_count,
                                                                    5)
            behaviour_suspicious = proctorDetail.get('behaviouralSuspicious')
            self.suspicious_or_not_supicious(behaviour_suspicious, False)
            write_excel_object.compare_results_and_write_vertically(
                current_excel_data.get('expectedBehaviourProctoringStatus'),
                self.status, row_count, 6)
        else:
            write_excel_object.compare_results_and_write_vertically('video suspicious', None, row_count,
                                                                    5)

            behaviour_video_suspicious = proctorDetail.get('faceSuspicious')
            self.suspicious_or_not_supicious(behaviour_video_suspicious, False)
            write_excel_object.compare_results_and_write_vertically(
                current_excel_data.get('expectedBehaviourProctoringStatus'),
                self.status, row_count, 6)

        # behaviour_suspicious = proctorDetail.get('behaviouralSuspicious')
        #
        # self.suspicious_or_not_supicious(behaviour_suspicious, False)
        # write_excel_object.compare_results_and_write_vertically(
        #     current_excel_data.get('expectedBehaviourProctoringStatus'),
        #     self.status, row_count, 5)

        overall_proctoring_status = proctorDetail.get('finalDecision')
        overall_suspicious_value = proctorDetail.get('systemOverallDecision')
        self.suspicious_or_not_supicious(overall_proctoring_status, overall_suspicious_value)
        write_excel_object.compare_results_and_write_vertically(current_excel_data.get('overallProctoringStatus'),
                                                                self.status, row_count, 8)
        excel_overall_suspicious_value = round(current_excel_data.get('overallSuspiciousValue'), 4)
        write_excel_object.compare_results_and_write_vertically(excel_overall_suspicious_value,
                                                                overall_suspicious_value, row_count, 10)
        write_excel_object.compare_results_and_write_vertically(current_excel_data.get('testCase'), None, row_count, 0)
        write_excel_object.compare_results_and_write_vertically(write_excel_object.current_status, None, row_count, 1)
        write_excel_object.compare_results_and_write_vertically(current_excel_data.get('testId'), None, row_count, 2)
        write_excel_object.compare_results_and_write_vertically(current_excel_data.get('candidateId'), None, row_count,
                                                                3)
        write_excel_object.compare_results_and_write_vertically(current_excel_data.get('testUserId'), None, row_count,
                                                                4)



login_token = crpo_common_obj.login_to_crpo(cred_crpo_admin.get('user'), cred_crpo_admin.get('password'),
                                            cred_crpo_admin.get('tenant'))
content = json.dumps(automation_proctor_eval_app_pref2)
app_pref_proc_eval_id = automation_tenant_proc_eval_id2
app_pref_proc_eval_type = automation_tenant_proc_eval_type2
update_app_preference = CrpoCommon.save_apppreferences(login_token, content, app_pref_proc_eval_id,
                                                       app_pref_proc_eval_type)

excel_read_obj.excel_read(input_path_proctor_evaluation, 3)
excel_data = excel_read_obj.details
proctor_obj = ProctorEvaluation()
tuids = []
over_all_status = 'Pass'
for fetch_tuids in excel_data:
    tuids.append(int(fetch_tuids.get('testUserId')))
context_id = CrpoCommon.force_evaluate_proctoring(login_token, tuids)
print(tuids)
context_id = context_id['data']['ContextId']
print(context_id)
current_job_status = 'Pending'

while current_job_status == 'Pending':
    current_job_status = CrpoCommon.job_status(login_token, context_id)
    current_job_status = current_job_status['data']['JobState']
    print("_________________ Proctor Evaluation is in Progress _______________________")
    print(current_job_status)
    time.sleep(20)

row_count = 2
for data in excel_data:
    proctor_obj.proctor_detail(row_count, data, login_token)
    row_count = row_count + 1
write_excel_object.write_overall_status(testcases_count=25)
print(datetime.datetime.now())
