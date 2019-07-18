def hcf(x,y):  # Using the Euclidean Algorithm to compute the highest common factor
    if x < y:
        y,x = x,y
    if x % y == 0:
        return y  # The result will return only the hcf of x and y
    else:
        x , y= y ,x % y
        return hcf(x,y)


def lcm(x,y):  # By the lemma(The multiplication of lcm(x,y) and hcf(x,y) is equal to x times y
    return x * y / hcf(x,y)

