def square(number):
    return number * number

result = square(5)
print(result) # Outputs: 25


gloabl_var = 10 # Global varible

def print_global():
    print(gloabl_var) # Accessing global varible

print_global() # Outputs: 10 


def my_function():
    local_var = 5 # Local variable
    print(local_var) # Accessing the local variable

my_function() #outputs 5
print(local_var) # Causes an error because the local variable does not exist at the global scope

global_var = 20 # Global variable

def my_function():
    global_var = 30  # local variable shadows the global variable
    print(global_var) # Outputs 20 (global variable remains unchanged)

my_function()
print(global_var) # Outputs: 20 (global variable remains unchanged)

