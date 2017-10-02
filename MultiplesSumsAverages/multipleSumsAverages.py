for count in range(1,1000):
    if count%2!=0:
        print count
#This for loop will count all intergers between 1 and 1000 and only print the interger if it is an odd number


for count in range(5,1000000):
    if count%5==0:
        print count
#This for loop will count all intergers between 5 and 1,000,000 and only print the interger if it is a multiple of 5

def sum_list(list):
    sum_num = 0
    for i in list:
        sum_num += i
    print sum_num

sum_list([1, 2, 5, 10, 255, 3])
#This function will find the sum of any given array passed through by the user

def avg_List(list):
    num = 0
    for i in list:
        num +=i
    avg_num = num / len(list)
    print avg_num
avg_List([1, 2, 5, 10, 255, 3])
#This function will find the average of any given array passed through by the user