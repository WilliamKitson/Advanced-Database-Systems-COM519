#  Copyright (c) 2024. William E. Kitson

import sqlite3
from tkinter import filedialog
from PIL import Image
import io

class ImageWriter:
    def __init__(self, database):
        self.__database = sqlite3.connect(database)
        self.__cursor = self.__database.cursor()

    def write(self, menu_id):
        with open(filedialog.askopenfilename(), 'rb') as file:
            file_blob = file.read()

        query = (
            "UPDATE Menu "
            "SET Image = ? "
            "WHERE Name = ?"
        )

        parameters = (
            file_blob,
            menu_id
        )

        self.__cursor.execute(query, parameters)
        self.__database.commit()

    def load(self, menu_id):
        query = (
            "SELECT Image "
            "FROM Menu "
            "WHERE Name = ?"
        )

        parameters = (menu_id,)
        self.__cursor.execute(query, parameters)

        image = self.__cursor.fetchall()

        for row in image:
            return Image.open(io.BytesIO(image[0][0]))

        return Image.new("RGB", (100, 100))