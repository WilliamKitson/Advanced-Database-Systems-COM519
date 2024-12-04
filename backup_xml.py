#  Copyright (c) 2024. William E. Kitson

import sqlite3
import xml.etree.ElementTree as ET

class BackupXML:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()
        self.__backup = ET.Element(f"{database}_backup")

    def backup(self):
        self.__backup_staff()
        self.__write_backup()

    def __backup_staff(self):
        self.__cursor.execute(
            "SELECT * "
            "FROM Staff"
        )

        staff = self.__cursor.fetchall()
        table = ET.SubElement(self.__backup, 'Staff')

        for row in staff:
            self.__add_row_sub_elements(row, table)

    def __add_row_sub_elements(self, row, table):
        for column in row:
            ET.SubElement(table, "test").text = str(column)

    def __write_backup(self):
        backup_string = ET.tostring(self.__backup)

        with open("4kitsw10_COM519_database_backup.xml", "wb") as f:
            f.write(backup_string)

    def reload(self):
        print("reload from XML")