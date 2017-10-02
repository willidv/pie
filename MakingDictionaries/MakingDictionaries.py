def Making_Dictionaries(list1,list2):
    new_dict = {}
    zipped = zip(list1,list2)
    zipped_dict = dict(zipped)   
    print zipped_dict
Making_Dictionaries(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"],["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])