def find_Characters(list,val):
    new_list = []
    for i in list:
        for j in i:
            if  j == val:
                new_list.append(i)
    print new_list
find_Characters(['hello','world','my','name','is','Anna'],"o")
