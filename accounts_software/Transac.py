# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:38:26 2018

@author: ortizca
"""


import datetime as dt


class Transac:
    def __init__(self, name, date, value=0, ligne=None):
        if ligne is None:
            self.name = name
            dmy = date.split("/")
            self.date = dt.date(int(dmy[2], base=10), int(dmy[1], base=10), int(dmy[0], base=10))
            self.value = value
        else:
            data = ligne.split("%")
            self.name = data[1]
            dmy = data[2].split("/")
            self.date = dt.date(int(dmy[2], base=10), int(dmy[1], base=10), int(dmy[0], base=10))
            self.value = data[3]


    def __lt__(self, other):
        return self.date < other.date
    def __gt__(self, other):
        return self.date > other.date

    def __str__(self):
        return "%{name}%{date}%{value}%".format(name=self.name, date=str(self.date.strftime("%d/%m/%Y")), value=str(self.value))


if __name__ == "__main__":
    t1 = Transac("McDo", "17/05/2023")
    t2 = Transac("KFC", "18/06/2023", 40)
    print(t1<t2)
    print(t1>t2)
    print(t1)
    print(str(t2))
    t3 = Transac(0, 0, ligne="%Udemy%09/06/2023%-14.99%")
    print(t3)