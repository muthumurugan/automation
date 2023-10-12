import mysql
import mysql.connector
from SCRIPTS.CRPO_COMMON.credentials import *


def ams_db_connection():
    conn = mysql.connector.connect(host=amsin_slave.get('host'),
                                   database=amsin_slave.get('database'),
                                   user=amsin_slave.get('user'),
                                   password=amsin_slave.get('password'))
    return conn

