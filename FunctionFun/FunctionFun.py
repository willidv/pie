def odds_And_Evens(number):
    i = 0
    while i <= number:
        if i%2==0:
            print "the number is", i, "This is an even number"  
        if i%2!=0:
            print "the number is", i, "This is an odd number"  
        i = i + 1
odds_And_Evens(2000)
#This function brings back all integers between 1 and 2000 and prints the number plus if it is an even or odd number

def multiply(num, list):
    new_list = []
    for i in list:
        i = i * num
        new_list.append(i)
    print new_list
multiply(5, [2,4,10,16])
#This function takes any given list and creates a new list with the numbers of the original list multiplied by any given number
