#  Copyright (c) 2024. William E. Kitson

import sqlite3
import xml.etree.ElementTree as ET

class BackupXML:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()
        self.__backup = ET.Element(f"{database}_backup")

    def backup(self):
        self.__backup_table("Staff")
        self.__backup_table("Roles")
        self.__backup_table("Staff_Roles")
        self.__backup_table("Menu")
        self.__backup_table("Categories")
        self.__backup_table("Ingredients")
        self.__backup_table("Menu_Ingredients")
        self.__write_backup()

    def __backup_table(self, name):
        self.__cursor.execute(
            f"SELECT * "
            f"FROM {name}"
        )

        table = self.__cursor.fetchall()
        sub_element = ET.SubElement(self.__backup, name)

        for row in table:
            self.__add_row_sub_elements(row, sub_element)

    def __add_row_sub_elements(self, row, sub_element):
        for i, column in enumerate(row):
            ET.SubElement(sub_element, self.__get_column_name_at(i)).text = str(column)

    def __get_column_name_at(self, index):
        return str(self.__cursor.description[index][0])

    def __write_backup(self):
        backup_string = ET.tostring(self.__backup)

        with open("4kitsw10_COM519_database_backup.xml", "wb") as f:
            f.write(backup_string)

    def reload(self):
        print("reload from XML")