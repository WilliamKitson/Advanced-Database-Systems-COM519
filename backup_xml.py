#  Copyright (c) 2024. William E. Kitson

import sqlite3
import xml.etree.ElementTree as ET

class BackupXML:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()

    def backup(self):
        data = ET.Element('4kitsw10_COM519_database_backup')

        self.__cursor.execute("SELECT * FROM Staff")
        get_login_details = self.__cursor.fetchall()

        element1 = ET.SubElement(data, 'Staff')

        for row in get_login_details:
            ET.SubElement(element1, 'Staff_Id').text = str(row[0])
            ET.SubElement(element1, 'Username').text = row[1]
            ET.SubElement(element1, 'Password').text = row[2]
            ET.SubElement(element1, 'Forename').text = row[3]
            ET.SubElement(element1, 'Surname').text = row[4]
            ET.SubElement(element1, 'DOB').text = row[5]

        b_xml = ET.tostring(data)

        with open("4kitsw10_COM519_database_backup.xml", "wb") as f:
            f.write(b_xml)

    def reload(self):
        print("reload from XML")