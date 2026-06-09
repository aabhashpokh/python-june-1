# list

# a = [1, 23, 4, 5, 1, 2, 5, 4]
# b = ["parash", "rajesh", "aabhash"]

# print(type(a))

# print(a)

# print(len(a))

# print(b)

# print(b[0])

# print(b[-1])

# every data type can be stored
# data = [1, 2, 3, "hello", "test", 1.0, True, None]

# slicing (starting & end, starting only, ending only, no starting no ending)

# print(data[0:5])  # case 1

# method od adding item

# append (adding one data at a time at the end of the list)

# data = [1, 2, 3, 4, 5, 6]
# data.append(9)
# data.append(0)
# print(data)

# # insert (adding data in the list but nt replacing)

# data = [1, 2, 3, 4, 5, 6]
# data.insert(10, 1.5)
# print(data)

# extend (adiing 2 list but doesn't create new variable)

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# b.extend(a)
# a.extend(b)

# print(a)
# print(b)

# # concat (+)

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c = b + a
# print(c)
# print(a, b)

# for substracting list

# delete (del)

data = [1, 2, 4, 5, 6, 8, 9]
del data[0]
del data[2]
print(data)

# remove
data = [1, 2, 4, 5, 6, 8, 9]
data.remove(1)

print(data)

# pop

data = [5, 6, 7, 8, 1, 2, 3, 4, 1, "hello"]
last_data = data.pop()
data.pop(5)
print(data)

print(last_data)

# clear

data = [5, 6, 7, 8, 1, 2, 3, 4, 1, "hello"]
data.clear()
print(data)


# workout example (Write a program to find largest number in a list using if-else.)

a = [23, 41, 7, 6, 32, 45, 90, 1]

largest = a[0]

for num in a:
    if num > largest:
        largest = num
    else:
        largest = largest

print(largest)


# create new line
 hahaha 
hehehe
