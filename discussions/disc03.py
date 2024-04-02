def count_partitions(n, m):
    if (n == 0):
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

def multiply(m, n):
    if(m == 0 or n == 0): return 0
    else: return m + multiply(m, n-1)

def hailstone(n):
    print(n)
    if(n == 1): return 1
    elif(n % 2 == 1): return 1 + hailstone(n * 3 + 1)
    else: return 1 + hailstone(n // 2)

def merge(n1, n2):
    if(n1 == 0): return n2
    elif(n2 == 0): return n1
    elif n1 % 10 < n2 % 10: return merge(n1 // 10, n2) * 10 + n1 % 10
    else: return merge(n1, n2 // 10) * 10 + n2 % 10

def make_func_repeater(f, x):
    def repeat(n):
        if(n > 1): return f(repeat(n - 1))
        else: return f(x)
    return repeat

def is_prime(n):
    def prime_helper(k):
        if k == 1:
            return True
        elif k == 0 or n % k == 0: # k == 0 is added to deal with the case of is_prime(1)
            return False
        else:
            return prime_helper(k - 1)
    return prime_helper(n - 1)