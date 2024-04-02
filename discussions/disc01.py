def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(49)
    False
    """
    i = 2
    while(i < n/2):
        if(n % i == 0): return False
        i+=1
    return True