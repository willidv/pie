words = "It's thanksgiving day. It's my birthday, too!"
#print words.replace("day", "month")----------> This line is for reference
words = words.replace("day", "month") #-------->This line is to Change the original value of the string "words"
print words
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def min_Max(list):
    for count in list:
        print max(list)
        print min(list)
        break
min_Max([2,54,-2,7,12,98])
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def first_Last(list):
    for count in list:
        print list[:1]
        print list[len(list)-1]
        new_list = list[:1] + list[7:8]
        print new_list
        break
first_Last(["hello",2,54,-2,7,12,98,"world"])
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def list_Order(list):
    list.sort()
    new_list = list[0:len(list)/2]
    new_list_2 = list[len(list)/2:len(list)-1]
    final_list = [new_list] + new_list_2
    print final_list
list_Order([19,2,54,-2,7,12,98,32,10,-3,6])  
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''      