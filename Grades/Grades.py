import random
def grades(num):
        if num in range(0,60):
            print num , "your grade is F"
        elif num in range(60,70):
            print num, "your grade is D"
        elif num in range(70,80):
            print num, "your grade is C"
        elif num in range(80,90):
            print num, "your grade is B"
        elif num in range(90,100):
            print num, "your grade is A"
grades(random.randint(1,100))