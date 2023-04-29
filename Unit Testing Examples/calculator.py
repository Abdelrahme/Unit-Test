
def add(x , y):
    return x+y

def multiply (x,y):
    return x*y

def divide (x,y):
    if y == 0:
        raise ValueError('cannot divide by zero')
    return x/y

def subtract (x,y):
    return x-y

def addTen(x):
    if type(x) not in [int,float]:
        raise TypeError('Only Accept Numbers')
    
    return x+10