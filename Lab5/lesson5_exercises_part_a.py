# Part A, Scope

# 1. Create global var course_name, function that create local var with the same name, print and explain result
course_name = "Python Fundamentals"
print(course_name)

def local_course():
    course_name = "C# Fundamentals"
    print(course_name)

local_course()
print(course_name)
# The value change of course_name exists only inside of the function,
# only way to take it outside of the scope is to return the value


# 2. Create function with local var counter and show it doesn't remain outside function
def local_counter():
    counter = 0

#print(counter)  # NameError, counter is not defined


# 3. Create function that modifies a global numeric var without global keyword, observe probelm, then rewrite and return new value
global_number = 13
print(global_number)

# def modify_number():
#     global_number += 1  # UnboundLocalError, can't increase value since global_number isn't a local var
#     print(global_number)

# modify_number()

def modify_number(value):
    return value + 1  # return the new value instead of modifying

global_number = modify_number(global_number)
print(global_number)


# 4. Create nested function and demonstrate a simple enclosing-scope lookup
def outer_function():
    outer_message = "This is a message"
    def inner_function():
        print(outer_message)

    inner_function()

outer_function()


# 5. Create examples that avoid shadowing built-ins
numbers = [2, 5, 1, 7, 3]
message = "this is a str"
total = sum(numbers)
lowest_number = min(numbers)

print(numbers)
print(message)
print(total)
print(lowest_number)