# F STRINGS

name = "Bryan"
print(f"Hi my name is {name}")
x = f"Hi my name is {name}"
print(x)

# UNPACKING

tup = (1,2,3,4,5)
lst = [1,2,3,4,5]
str = "hello"
dict1 = {"a": 1, "b": 2}
coords = [1,2]

a, b, c, d, e = tup # a = 1, b = 2, c = 3, d = 4, e = 5
print(a, b, c, d, e)

# MULTIPLE ASSIGNMENTS

width, height = 400, 600
print(f"Before: width = {width}, height = {height}")
# temp = width
# width = height
# height = temp
# Instead of creating a temp variable to swap two variables, you can easily do it like this in Python.
width, height = height, width
print(f"After: width = {width}, height = {height}")

# COMPREHENSIONS

x = [i for i in range(10) if i % 2 == 0]
print(x)

# OBJECT MULTIPLICATION

word = "hello" * 5
print(word)
word_list = ["hello"] * 5
print(word_list)

# INLINE/TERNARY CONDITION

w = 1 if 2 > 3 else 0
print(w)

# ZIP FUNCTION

names = ["Billy", "Jack", "Penny"]
ages = [45, 66, 22]
eye_colors = ["blue", "black", "green"]

print(list(zip(names, ages, eye_colors)))

# ARGS/KWARGS

args = [1,2,3]
print(*args)

# FOR ELSE & WHILE ELSE

search = [1, 2, 3, 4, 5]
target = 9

for i in search:
    if i == target:
        print("I found it! :)")
        break
else:
    print("I didn't find it :(")