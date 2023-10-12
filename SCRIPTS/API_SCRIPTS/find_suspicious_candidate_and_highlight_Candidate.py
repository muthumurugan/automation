import np
from SCRIPTS.COMMON.io_path import *
from SCRIPTS.COMMON.read_excel import *
from SCRIPTS.COMMON.write_excel_new import *
from SCRIPTS.CRPO_COMMON.crpo_common import *


class SuspiciousProcess:

    def __init__(self):
        self.suspicious_process = ["Skype",
                                   "SkypeHost",
                                   "CamRecorder",
                                   "g2mcomm.exe",
                                   "GotoMeetingWinStore",
                                   "vncserver",
                                   "vncviewer",
                                   "vncserverui",
                                   "vncagent",
                                   "chromoting",
                                   "Mikogo-host",
                                   "Mikogo-video",
                                   "Mikogo-screen-service",
                                   "AeroAdmin",
                                   "beamyourscreen-host",
                                   "RemotePCDesktop",
                                   "RPCService",
                                   "RPCSuite",
                                   "join.me",
                                   "Teams",
                                   "Slack",
                                   "Discord",
                                   "seamonkey",
                                   "Riot",
                                   "Screenleap",
                                   "smpcsetup",
                                   "smpcview",
                                   "Anymeeting",
                                   "jitsi",
                                   "proficonf",
                                   "uber",
                                   "whereby",
                                   "remote_assistance_host",
                                   "remote_assistance_host_uiaccess",
                                   "remoting_host",
                                   "remoting_native_messaging_host",
                                   "remoting_desktop",
                                   "remoting_start_host",
                                   "romviewer",
                                   "romserver",
                                   "mingleview",
                                   "UltraViewer_Desktop",
                                   "UltraViewer_Service",
                                   "splash",
                                   "zoom",
                                   "skypebridge",
                                   "skypeapp",
                                   "skypebackgroundhost",
                                   "bdcam",
                                   "rutview",
                                   "rutserv",
                                   "teamviewer",
                                   "xboxApp",
                                   "xblAuthManager",
                                   "xboxGipSvc",
                                   "xblGameSave",
                                   "xboxNetApiSvc",
                                   "GameBar",
                                   "GameBarFTServer",
                                   "ManyCam",
                                   "ManyCamService",
                                   "YouCam10",
                                   "YouCamService10",
                                   "XSplit.Core",
                                   "XGS32",
                                   "XGS64",
                                   "DemoCreator",
                                   "DCCefWing",
                                   "DCSHelper",
                                   "Steam",
                                   "Steamservce",
                                   "steamwebhelper",
                                   "SAMBC",
                                   "Wirecast",
                                   "wirecastd",
                                   "chromedriver",
                                   "AvastBrowserCrashHandler",
                                   "AvastBrowserCrashHandler64",
                                   "browser",
                                   "yandex",
                                   "opera_crashreporter",
                                   "blisk",
                                   "Colibri",
                                   "Update",
                                   "epic",
                                   "EpicUpdate",
                                   "iridium",
                                   "whale",
                                   "Classic",
                                   "decentr",
                                   "decentr_wg_communicator",
                                   "kinza",
                                   "Flock",
                                   "Aviator",
                                   "chedot",
                                   "chedot_notifications",
                                   "Fifo",
                                   "Sphere",
                                   "tor",
                                   "Proxificator",
                                   "onelaunch",
                                   "onelaunchtray",
                                   "AlterCam",
                                   "TSVBEngineProc",
                                   "DroidCamApp",
                                   "IriunWebcam",
                                   "CamoStudio",
                                   "vMix64",
                                   "vMixService",
                                   "PowerToys",
                                   "DouWan",
                                   "Streamlabs OBS",
                                   "WebcamMax",
                                   "EpocCamTest",
                                   "EpocCamService",
                                   "EWCService",
                                   "Vysor",
                                   "PRISMLauncher",
                                   "recorder",
                                   "Snap Camera",
                                   "Camtasia",
                                   "CamtasiaStudio",
                                   "Camtasia_Studio",
                                   "CamPlay",
                                   "CamtasiaUtl",
                                   "Element",
                                   "Telegram",
                                   "g2mlauncher",
                                   "g2mstart",
                                   "webexmta",
                                   "ptoneclk",
                                   "AA_v3",
                                   "CiscoCollabHost",
                                   "CiscoWebExStart",
                                   "obs64",
                                   "obs32",
                                   "obs",
                                   "IperiusRemote",
                                   "SMPCSetup",
                                   "FreeConferenceCall",
                                   "ApowerMirror",
                                   "ISLLight",
                                   "anydesk",
                                   "getscreen",
                                   "msteams",
                                   "vmms",
                                   "vmware-authd",
                                   "WhatsApp",
                                   "CastSrv",
                                   "BraveUpdate",
                                   "AnyDesk",
                                   "msedge",
                                   "dwagent",
                                   "cmw_srv",
                                   "nahimicNotifSys",
                                   "SamsungDeX",
                                   "vmware-hostd",
                                   "WSHelper",
                                   "WsToastNotification",
                                   "YourPhone"]
        requests.packages.urllib3.disable_warnings()
        self.row_size = 2
        write_excel_object.save_result(output_path_suspicious_candidates)
        header = ["Sept/07/2023"]
        write_excel_object.write_headers_for_scripts(0, 0, header, write_excel_object.black_color_bold)
        header1 = ["CandidateID", "TestuserID", "SuspiciousStatus", "SuspiciousList", "CandidateProcessList"]
        write_excel_object.write_headers_for_scripts(1, 0, header1, write_excel_object.black_color_bold)

    def validate_process(self, excel_input):
        candidate_id = int(excel_input.get('candidateId'))
        testuserid = int(excel_input.get('testUserId'))
        process = excel_input.get('processes').split(',')
        # suspicious_list = ['NortonSecurity', 'chrome', 'muthu']
        suspicious_value = []
        final_suspicious_status = "Not Suspicious"
        indices = np.where(np.in1d(process, self.suspicious_process))[0]
        if len(indices) > 0:
            for i in indices:
                suspicious_value.append(process[i])
            if len(suspicious_value) > 0:
                final_suspicious_status = "Suspicious"
            else:
                final_suspicious_status = "Not Suspicious"
        suspicious_value = str(suspicious_value)
        suspicious_value = suspicious_value.replace('[', '')
        suspicious_value = suspicious_value.replace(']', '')
        write_excel_object.compare_results_and_write_vertically(candidate_id, None, self.row_size,
                                                                0)
        write_excel_object.compare_results_and_write_vertically(testuserid, None, self.row_size,
                                                                1)
        write_excel_object.compare_results_and_write_vertically(final_suspicious_status, None, self.row_size,
                                                                2)
        write_excel_object.compare_results_and_write_vertically(suspicious_value, None, self.row_size,
                                                                3)
        write_excel_object.compare_results_and_write_vertically(excel_input.get('processes'), None, self.row_size,
                                                                4)

        self.row_size += 1


allowed_ext_obj = SuspiciousProcess()
excel_read_obj.excel_read(input_path_suspicious_list, 0)
excel_data = excel_read_obj.details
for data in excel_data:
    allowed_ext_obj.validate_process(data)
ended = datetime.datetime.now()
write_excel_object.write_excel.close()
