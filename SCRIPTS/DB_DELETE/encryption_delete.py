import datetime

from SCRIPTS.COMMON.dbconnection import *


class EncryptionDelete:

    def __init__(self):
        print(datetime.datetime.now())

    @staticmethod
    def encryption_delete():
        db_connection = ams_db_connection()
        cursor = db_connection.cursor()

        query = 'delete from candidates where ' \
                'email1 = "enc_str:::aiSSXIZOrLo6zWtF/Dzi+RFKdp2BAV6o8abacVu7GYCB4Nbjqw2085XMQXBYCWk9" ' \
                'and tenant_id=1787;'
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()


del_data = EncryptionDelete()
del_data.encryption_delete()
print(datetime.datetime.now())
