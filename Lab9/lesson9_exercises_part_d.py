# Part D, isinstance()

# 1. Create a base class User and a subclass AdminUser(User)
class User:
    def __init__(self):
        pass


class AdminUser(User):
    pass


# 2. Create and AdminUser object
admin_1 = AdminUser()


# 3. Use isinstance() to check whether the object is an AdminUser, a User, and a str
# 4. Print all 3 results
print(isinstance(admin_1, AdminUser))
print(isinstance(admin_1, User))
print(isinstance(admin_1, str))


# 5. In a comment, explain why the AdminUser object is also considered an instance of User
# because AdminUser inherits everything from User, so instance recognized it as both AdminUser and User