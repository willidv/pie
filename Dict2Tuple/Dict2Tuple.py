def dict_2_Tuple(dict):
    new_dict=[]
    for key,value in dict.iteritems(): 
        x= key,value
        new_dict.append(x)
    print new_dict
dict_2_Tuple({
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
})