"""Cложение бесконечных цифр"""

class Additions():

    def addisions(*val1, **val2):
        sum = 0
        for m in val1:
            sum = sum + m
        for n in val2.values():
            sum = sum + n
        return sum

