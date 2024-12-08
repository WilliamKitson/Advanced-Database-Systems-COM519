#  Copyright (c) 2024. William E. Kitson

from image_writer import ImageWriter
ImageWriter("4kitsw10_COM519_database").load("Ice Cream")

from input_validator import InputValidator
print(InputValidator().valid_password("qQ100000000000000000"))

from presentation import Presentation
Presentation("4kitsw10_COM519_database").render()