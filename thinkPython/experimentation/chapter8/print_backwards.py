def print_backwards(x):
    """
    Prints given string (x) backwards
    
    >>> print_backwards("abc")
    c
    b
    a
 
    
    """
    index = -1
    while index >= -len(x):
        print x[index]
        index += -1

