def Natural_sum(n):
    s = 0
    for i in range(n,n-1):
        s += i
    return s

print(Natural_sum(5))
print(Natural_sum(10))


def Natural_sum1(n):
    s = 0
    if n == 1:
        return 1
    else:
        return n + Natural_sum1(n-1)
    

print(Natural_sum1(5))
print(Natural_sum1(10))


