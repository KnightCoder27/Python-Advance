# Reduce:

import functools

lis = [1, 3, 5, 6, 2,7]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# Frozenset:

favourite_subject = ["OS", "DBMS", "Algo"]
f_subject = frozenset(favourite_subject) 
f_subject[1] = "Networking"
