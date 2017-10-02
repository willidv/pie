def identical_strings(list_one, list_two):
    for i in range(0,len(list_two)):  
        if list_one[i] == list_two[i] :
            print "the lists are same" 
        else:
            print "the lists are the different"
            break
identical_strings(['celery','carrots','bread','cream'], ['celery','carrots','bread','cream'])