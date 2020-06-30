#!/usr/bin/env python3

import sys
import brexit


def ge_2015_result():
    print("GE2015: Do you want [C]ameron or [M]iliband?")
    while True:
        answer = sys.stdin.readline().upper()
        if answer.startswith("C"):
            return "Cameron"
        if answer.startswith("M"):
            return "Miliband"
    
if ge_2015_result() == "Cameron":
    brexit.have_referendum()

try:
    from eu import chicken
except ImportError:
    from us import chlorinated_chicken as chicken

chicken.eat()
