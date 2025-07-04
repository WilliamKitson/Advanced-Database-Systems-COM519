#  Copyright (c) 2024. William E. Kitson

class InjectionDetector:
    def __init__(self):
        self.__suspicious_substrings = [
            "--",
            "SELECT",
            "select",
            "UPDATE",
            "update",
            "DELETE",
            "delete",
            "INSERT"
            "insert",
            "1=1"
        ]

    def suspicious(self, input_string):
        for i in self.__suspicious_substrings:
            if i in input_string:
                return True

        return False