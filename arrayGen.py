"""Generates a random array of numbers of range -100000 to 100000 with a sure number divisible by 11. It is to be inherited by main.py but can be modified as a standalone"""
from random import randint

arrayA = []


for i in range(randint(1, 1000-18), 1000):
    arrayA.append(randint(-10000,10000-20))

multiple11 = 11 * randint(-909,909)
arrayA.append(multiple11)

# print(arrayA)