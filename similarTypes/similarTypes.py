def similar_Types(list):
    num = 0.0
    new_Str = ""
    seenNum = False
    seenStr = False
    for i in list:
        if type(i) == int or type(i) == float:
            num += i  
            seenNum = True                   
        elif type(i) == str:
            new_Str += i + " "
            seenStr = True
    if seenNum == True and seenStr == False:
         print "The list you entered is of integer type"
    elif seenStr == True and seenNum == False:
        print "The list you entered is of string type"
    else:
        print "The list you entered is of mixed type"
    print "string: " + new_Str
    print num
    
similar_Types([11,22,15])
#This is a function that will take any list and separate the strings from intergers or floats and will return a sentence based on what types of values are in the list and the sum of the listed items or a new string of the items
