# import np
#
# a = {'candidateId': 7905767.0, 'testUserId': 11435221.0,
#      'processes': 'firefox1, Chrome'}
#
# candidate_id = int(a.get('candidateId'))
# testuserid = int(a.get('testUserId'))
# process = a.get('processes').split(',')
# print(process)
# suspicious_list = ['firefox']
# suspicious_value = []
# final_suspicious_status = "Not Suspicious"
# indices = np.where(np.in1d(process, suspicious_list))[0]
# if len(indices) > 0:
#     for i in indices:
#         suspicious_value.append(process[i])
#     if len(suspicious_value) > 0:
#         final_suspicious_status = "Suspicious"
#     else:
#         final_suspicious_status = "Not Suspicious"
# print(final_suspicious_status)


a = str([])
b = a.replace('[', '')
c = b.replace(']', '')
print(c)
