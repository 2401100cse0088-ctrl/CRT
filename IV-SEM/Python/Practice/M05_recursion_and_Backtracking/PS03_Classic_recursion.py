def Fibonacci(n):
    if n <= 0:
        return "Provide a +ve number"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)
    

print(Fibonacci(5))



def GCD(a,b):
    while b != 0:
        a,b = b,a%b
    return a

print(GCD(4,10))