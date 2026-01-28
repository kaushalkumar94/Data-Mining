# Integer data type
a = 10

# Float data type
b = 3.14

# Complex data type
c = 2 + 3j

# String data type
d = "Kaushal Kumar"

# Boolean data type
e = True

# Print values and their types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

#2. VARIABLES IN PYTHON (Dynamic Typing)
# Python allows changing the type of variable at runtime

x = 10          # x is integer
print(x, type(x))

x = "Hello"     # now x is string
print(x, type(x))

x = 3.5         # now x is float
print(x, type(x))


#3. SCOPE OF VARIABLES.
# Global variable
x = 100

def my_function():
    # Local variable
    y = 50
    print("Inside function:")
    print("x (global) =", x)
    print("y (local) =", y)

my_function()

print("Outside function:")
print("x =", x)


#4. BASIC DATA STRUCTURES IN PYTHON
# Creating a list
my_list = [1, 2, 3, "Kaushal", 5.5]

# Printing list
print("Original list:", my_list)

# Accessing elements
print("First element:", my_list[0])

# Modifying list (because list is mutable)
my_list[0] = 100
print("Modified list:", my_list)

# Adding new element
my_list.append(999)
print("After append:", my_list)

# Removing element
my_list.remove(2)
print("After remove:", my_list)


# Creating a tuple
my_tuple = (10, 20, 30, "Python")

print("Tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])

# Tuple is immutable, so this will cause error:
# my_tuple[0] = 100   Not allowed

print("Tuple cannot be modified (immutable)")


# Creating a set
my_set = {1, 2, 3, 4, 4, 5}

# Duplicate values are automatically removed
print("Set:", my_set)

# Adding element
my_set.add(10)
print("After adding:", my_set)

# Removing element
my_set.remove(3)
print("After removing:", my_set)

# Creating a dictionary (key-value pair)
my_dict = {
    "name": "Kaushal",
    "age": 21,
    "branch": "CSE"
}

print("Dictionary:", my_dict)

# Accessing value using key
print("Name:", my_dict["name"])

# Modifying value
my_dict["age"] = 22
print("Updated dictionary:", my_dict)

# Adding new key-value
my_dict["college"] = "UIET"
print("After adding new key:", my_dict)

# Removing a key
del my_dict["branch"]
print("After deletion:", my_dict)

#FUNCTIONS
# Function to add two numbers
def add(a, b):
    return a + b

# Function call
result = add(5, 3)
print("Result:", result)

#LOOPS
# Printing numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Printing numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
#IF-ELSE CONDITION

age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


