# Part B, *args

# 1. Write add_all(*numbers), return sum without sum()
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total

print(add_all(1, 2, 3, 5, 32, 4, 4))


# 2. Write average(*numbers), decide what should happen when no numbers are supplied
def average(*numbers):
    total = 0
    if len(numbers) == 0:
        print("No numbers to sum")
        return
    else:
        for number in numbers:
            total += number

        return total / len(numbers)

print(average(2, 1, 5, 2, 1, 43))


# 3. Write longest_word(*words), return longest word
def longest_word(*words):
    if len(words) == 0:
        return
    else:
        longest = words[0]
        for word in words:
            if len(word) > len(longest):
                longest = word
        return longest

print(longest_word("balloon", "fundamental", "crane", "ostentatious"))


# 4. Write build_sentence(separator, *words), return one joined string
def build_sentence(separator, *words):
    sentence = ""
    if len(words) == 0:
        return
    else:
        for word in words:
            if sentence == "":
                sentence = word
            else:
                sentence = sentence + separator + word
        return sentence

print(build_sentence(" ", "apples", "oranges", "kiwi"))


# 5. Write describe_scores(studen_name, *scores), return name, number of scores, and average
adam_scores = [1, 2, 3 , 7, 2, 5, 2, 6, 2]


def describe_scores(student_name, *scores):
    total = 0
    if len(scores) == 0:
        return
    else:
        for score in scores:
            total += score
            
        return f"{student_name} has a total of {total}, with an average of {average(*scores):.1f}"

print(describe_scores("Adam", *adam_scores))