i = 0
while i < 5:
    checkerboard = ""
    if i%2 == 0:
        checkerboard= checkerboard + "* * * * *"
    elif i%2 != 0:
        checkerboard = checkerboard +" * * * * *"
    i = i + 1
    print checkerboard
