def draw_Stars(list):
    for i in list:
        if type(i) == int:
            print i * "*" 
        elif type(i) == str:
            print i[0].lower() * len(i) 
draw_Stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
#This is a function that will iterate through an array(list). If the element in the array is an integer, it will print out the length of the integer in stars. If the element in the array is a string, it will print out the first letter of the string times the length of the string
