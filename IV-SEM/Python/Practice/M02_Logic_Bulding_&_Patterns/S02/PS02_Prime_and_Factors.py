"""
#Print all the factors of a given number
input : 12
output : 1 2 3 4 5 6 12'''
N = int(input())
for i in range(1,N//2+1):
    if N%i==0:
        print(i,end=" ")
print(N)

#Print the no of factors of the given number
N = int(input())
count = 0
for i in range(1,N+1):
    if N%i==0:
        count+=1
print(count)

#Check whether the given number is prime or not
N = int(input())
if N<=1:
    print("Not Prime")
else:
    for i in range(2,N):
        if N%i==0:
            print("Not Prime")
            break 
    else:
        print("Prime")

#Print all prime numbers between given range
n = int(input())
m = int(input())
for i in range(n,m+1):
    counter = 0
    for j in range(2,i//2+1):
        if i%j == 0:
            counter += 1
    if counter == 0:
        print(i,end=" ")

#Check if the given number is a factorial or not
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
n = int(input())
if n < 0:
    print("Factorial not defined")
else:
    print("Factorial is:", factorial(n))

#GCD
input: 12 24
output: 12
"""

    