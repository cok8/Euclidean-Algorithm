def Euclidean_Algorithm(x,y):
    if x < y:
        y,x = x,y
    if x % y == 0:
        print("hcf({},{}) = {}".format(x,y,y))
        return
    else:
        old_x, old_y  = x,y
        x , y= y ,x % y
        print("hcf({},{}) = ".format(old_x,old_y), end='')
        return Euclidean_Algorithm(x,y)


switch = 1
while switch == True:
    try:
        x = int(input("Input the first number"))
        y = int(input("Input the second number"))
        Euclidean_Algorithm(x,y)
        switch = 0
    except ValueError:
        print("Please input a number")

