import re

# changing a string with numbers and symbols into a float value.

def str_to_float(value: str):
    a, b = value.split(".")
    a = re.sub('[^0-9]','', a)
    return float(a + "." + b)