'''
sample input : 1234
sample output: 4

sample input : 12236
sample output : 5


num = int(input())
count = 0
while num > 0:
    count += 1
    num = num // 10
print(count)


sample input : 1234
sample output : 10

sample input: 45678
sample output: 30

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    sum = sum + (num % 10)
    num = num // 10          

print(sum)


sample input : 1234
sample output : 4 2

sample input: 45678
sample output: 8 7 6

n = int(input())
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10

sample input : 1234
sample output : 2 4

sample input: 45678
sample output: 4 6 8

def reverse(num):
    rev = 0
    while num > 0:
        rev = (rev*10) + (num % 10)
        num = num // 10
    return rev

n = reverse(int(input()))
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit,end=" ")
    n = n // 10

n = int(input())
temp = reverse(n)

print(temp == n)
if temp == n:
    print(True)
else:
    print(False)
print(True) if temp == n else print(False)
'''