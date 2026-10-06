# Part B, Return values

# 1. Write is_even(number), returning True/False
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(35231))


# 2. Write get_larger(a, b), return larger value without using max()
def get_larger(a, b):
    if a > b:
        return a
    else:
        return b

print(get_larger(1, 3))


# 3. Write classify_score(score), return PASS or FAIL
def classify_score(score):
    if score >= 50:
        return "PASS"
    else:
        return "FAIL"

print(classify_score(73))


# 4. Write full_name(first_name, last_name), return formatted str
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(full_name("John", "Doe"))


# 5. Write calculate_discount(price, percent), return discounted price
def calculate_discount(price, percent):
    return price * (1 - percent / 100)

print(calculate_discount(164, 25))


# 6. Show why print(result) inside function isn't the same as return result
def add_print(a, b):
    print(a + b)


def add_return(a, b):
    return a + b

saved_result_1 = add_print(1, 3)
saved_result_2 = add_return(1, 3)

print(saved_result_1)
print(saved_result_2)