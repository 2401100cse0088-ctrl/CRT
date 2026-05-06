'''
Break: used to exit a loop prematurely when a certain condition is met.
Continiue: used to skip the current iteration of a loop and move to the next iteration.
'''
'''
#break 
for i in range(1,11):
    if i==5:
        break
    print(i, end=" ")
#output: 1 2 3 4
'''
'''
#continue
for i in range(1,11):
    if i==5:
        continue
    print(i, end=" ")
#output: 1 2 3 4 6 7 8 9 10
'''
'''
#Password validation 
original_password = "Ashrith123"
for i in range(3):
    password = input()
    if password == original_password:
        print("Login Successful")
        break
else:
    print("Account Locked")
'''
