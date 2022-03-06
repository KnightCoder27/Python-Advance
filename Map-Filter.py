# Map

# SYNTAX : map(fun, iter)

def addition(n):
    return n + n
  
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

#ALITER:
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

#Filter

def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False  
sequence = ['p','f','a','j','e','i','c','u']
filtered = filter(fun, sequence)
  
print('The filtered letters are:')
for s in filtered:
    print(s)
