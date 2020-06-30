import random

referendum_result = {}

def have_referendum():
    referendum_result["leave"] = random.gauss(50, 3)
    print("You have a Brexit referendum")
    print("The leave vote is ", referendum_result["leave"])
