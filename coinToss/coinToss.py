import random
def coin_Toss(num):
    i = 0
    j = 0
    while i < num:
        chance = random.randint(1,2)
        if chance == 1:
            print "Attempt number" , i , "It's a head!... Got ", i , "head(s) so far and " , j , "tail(s) so far"
            i = i+ 1
        elif chance == 2:
            print "Attempt number" , j , "It's a tails!... Got ", j , "tails(s) so far and ", i, "head(s) so far"
            j= j+1
coin_Toss(5000)
