def add(x, y):
    """Add Funtion """
    return x + y

def subtract(x, y):
    """Subtract Fucntion"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x /y

add1 = add(10, 5)
