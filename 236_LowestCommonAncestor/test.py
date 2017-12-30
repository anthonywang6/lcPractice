def product(a,b):
    return a*b

mytuple = (3,2)
mydict = {'a':3, 'b':2}
print(product(*mytuple))
print(product(**mydict))
