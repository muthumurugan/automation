import datetime

from SCRIPTS.COMMON.dbconnection import *


class EncryptionDelete:

    def __init__(self):
        print(datetime.datetime.now())

    @staticmethod
    def encryption_delete():
        db_connection = ams_db_connection()
        cursor = db_connection.cursor()
        query = "delete from candidates where  hp_dec(email1) COLLATE  utf8mb4_unicode_ci = 'testencryptionautomationtenant@gmail.com' and tenant_id=1787;"
        print(query)
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()


del_data = EncryptionDelete()
del_data.encryption_delete()
print(datetime.datetime.now())
