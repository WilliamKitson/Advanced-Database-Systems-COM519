#  Copyright (c) 2024. William E. Kitson

class InputValidator:
    def __init__(self):
        self.__lowercase = "qwertyuiopasdfghjklzxcvbnm"
        self.__uppercase = "QWERTYUIOIOPASDFGHJKLZXCVBNM"
        self.__numbers = "0123456789"

    def valid_password(self, password):
        if self.__validate_password_lowercase(password):
            return True

        return False

    def __validate_password_lowercase(self, password):
        lowercases = 0

        for i in self.__lowercase:
            lowercases += password.find(i) != -1

        return lowercases > 0