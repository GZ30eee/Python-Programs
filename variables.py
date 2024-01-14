# Global Variable
globalVar = "I'm a global variable"

def demo_variables():
    # Local Variable
    localVar = "I'm a local variable"
    
    # Accessing global variable inside function
    print(globalVar)
    
    # Accessing local variable inside function
    print(localVar)

# Calling function to print variables
demo_variables()

# Casting and getting the type
num = 123
print("Integer:", num)
num = str(num)
print("After casting to string:", num)
print("Type after casting:", type(num))

# Variable naming conventions
camelCaseVar = "I'm a camel case variable"
PascalCaseVar = "I'm a Pascal case variable"
snake_case_var = "I'm a snake case variable"

# Many values to multiple variables
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global keyword
def demo_global_keyword():
    global globalVar
    globalVar = "I'm a modified global variable"

demo_global_keyword()
print(globalVar)
