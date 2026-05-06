""" 
#To print even numbers from list
li = [1,2,3,4,5]
#output:[2,4]
for i in li:
    if i % 2 == 0:
        print(i)    

#To print square of the numbers from the list
li = [1,2,3,4,5]
#output:[1,4,9,16,25]
res = []
for i in li:
    res.append(i**2)
print(res)

#To print even square of the numbers from the list
li = [1,2,3,4,5]
#output:[4,16]
res = []
for i in li:
    if i % 2 == 0:
        res.append(i)
print(res)
#ans = [i for i in li if i % 2 == 0]
#print(ans)

#combining of strings
li = ['a','b','c']#'a b c'
res = ""
for ch in li:
    res = res + ch + " "
print(res)
#print("@".join(li))

1. Pyramid
n = 4
Output:
    *
   * *
  * * *
 * * * *

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

2. Inverted Pyramid
n = 4
Output:
* * * * 
 * * *
  * *
   *
n = int(input())
for i in range(n,0,-1):
      print(" "*(n-i)+"* "*i)

3. Diamond
n = 4
Output:
   * 
  * *
 * * *
* * * *
 * * *
  * *
   *

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

4. Number Pyramid
n = 4
Output:
   1
  1 2
 1 2 3
1 2 3 4

n = int(input())
for i in range(1, n + 1):
    numbers = " ".join(str(j) for j in range(1, i + 1))
    print(" " * (n - i) + numbers)

5. Hollow Pyramid
n = 4
Output:
   *
  * *
 *   *
*******

n = int(input())
for i in range(1, n + 1):
    if i == n:
        print("*" * (2 * n - 1))
    else:
        print(
            " " * (n - i) +
            "".join(
                ["*" if j == 0 or j == 2*i-2 else " "
                 for j in range(2*i - 1)]
            )
        )
"""