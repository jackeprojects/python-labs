# Why is building SQL with an f-string dangerous, and why is a '?' placeholder safe?
# When using f-string, anything the user inputs will be used in the query
# This can be exploited by using keywords to change the query
# For example, user can enter in OR, AND, 1=1 (which means True)

# Using '?' separates the users input from the query
# Which makes the users input get treated like a value instead of being appended to the query
# So whatever the user inputs will now be treated as plain text instead and searched for