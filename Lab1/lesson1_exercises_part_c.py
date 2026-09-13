# Part C, Strings

# 1. Store a sentence, print length, uppercase, lowercase, and stripped version
sentence = "  the quick brown fox jumps over the lazy dog.  "
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.strip())

# 2. Ask for first name and last name, create formatted full name using f-string
first_name = input("What's your first name?: ")
last_name = input("What's your last name?: ")
print(f"Hello {first_name} {last_name}!")


# 3. Given "python programming", print first, last, first 6, last 11 chars, and reversed
given_string = "python programming"
print(f"First char: {given_string[0]}")
print(f"Last char: {given_string[-1]}")
print(f"First 6 chars: {given_string[:6]}")
print(f"Last 11 chars: {given_string[-11:]}")
print(f"Reversed: {given_string[::-1]}")


# 4. Username generator, given first and last name, remove surrounding white space,
# create username using first 3 chars of first name, 5 first chars of last name
username_first_name = input("What's your first name?: ").strip().lower()
username_last_name = input("What's your last name?: ").strip().lower()
username = username_first_name[:3] + username_last_name[:5]
print(f"Your username is {username}")


# 5. Given an email address, extract parts before and after "@"
email_address = input("What's your email address?: ")
if "@" in email_address:
    email_username, at, domain_extension = email_address.partition("@")
    print(email_username)
    print(domain_extension)


# 6. Create sentence using "Java", replace the word with "Python", and print both sentences
programming_sentence = "Java is an island in Indonesia"
programming_sentence_edited = programming_sentence.replace("Java", "Python")
print(programming_sentence)
print(programming_sentence_edited)