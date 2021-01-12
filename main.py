"""Script finds the smallest number divisible by 11 in an array of random integerf between -10000 and 10000"""
from arrayGen import arrayA



def func():
    arrayDivs = []
    for i in arrayA:
        if i%11 == 0:
            arrayDivs.append(i/11)
        else:
            pass
    
    #function sorts array in ascending order
    arrayDivs.sort()


    print(f"\n In {arrayA} the smallest number divisible by 11 is: {int(arrayDivs[0]*11)}")
    return arrayDivs[0]


func()