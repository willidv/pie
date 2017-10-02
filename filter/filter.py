def filter(value):
    if type(value) == int:
        if value > 100:
            print "That's a big number!"
        else:
            print "That's a small number!"
    elif type(value) == str:
        if len(value) > 50:
            print "Long sentence."
        else:
            print "Short sentence."
    elif type(value) == list:
        if len(value) >=10:
            print "Big List!"
        else:
            print "Short List!"

filter([1,2,3,6,7,8,9,8])