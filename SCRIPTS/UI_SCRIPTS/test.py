import xlsxwriter
from SCRIPTS.COMMON.read_excel import *
from SCRIPTS.COMMON.io_path import *
import datetime
from SCRIPTS.CRPO_COMMON.crpo_common import *
from SCRIPTS.ASSESSMENT_COMMON.assessment_common import *
from SCRIPTS.COMMON.dbconnection import *

excel_read_obj.excel_read("C:\\Users\\Dell\\Downloads\\password.xls", 0)
print(excel_read_obj.details)