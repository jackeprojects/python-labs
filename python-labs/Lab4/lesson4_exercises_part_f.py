# Part F, Applied challenge: Event registration processor

# 1. Create functions to normalize a participant name, validate age range using boolean return values,
# calculate registration fee based on age/student status, and create a participant dictionary
def normalize_name(name):
    return name.strip().title()


def valid_age(age):
    return age >= 18 and age <= 65


def registration_fee(age, is_student):
    if valid_age(age):
        fee = 100  # full price
    else:
        fee = 60  # discount for minors and seniors

    if is_student:
        fee *= 0.9 # 10% off for students

    return fee


def create_participant(name, age, is_student):
    name = normalize_name(name)
    fee = registration_fee(age, is_student)
    participant = {"name": name, "age": age, "is_student": is_student, "fee": fee}

    return participant


# 2. Create 8 participant dictionaries using the functions
joseph = create_participant("Joseph", 54, False)
angela = create_participant("Angela", 26, True)
connor = create_participant("Connor", 17, True)
adam = create_participant("Adam", 7, True)
george = create_participant("George", 86, False)
jasmine = create_participant("Jasmine", 25, False)
sasha = create_participant("Sasha", 54, True)
naomi = create_participant("Naomi", 54, False)
print(naomi)


# 3. Write a function that receives the participant list and returns the total expected registration revenue
participants = [joseph, angela, connor, adam, george, jasmine, sasha, naomi]

def registration_revenue(participants):
    total_fees = 0
    for participant in participants:
        total_fees += participant["fee"]

    return total_fees

print(registration_revenue(participants))


# 4. Write a function that only returns student participants
def get_student_participants(participants):
    students = []
    for participant in participants:
        if participant["is_student"]:
            students.append(participant)

    return students

print(get_student_participants(participants))


# 5. Write a function that returns the oldest participant
def get_oldest_participant(participants):
    age = 0
    oldest_participant = {}
    for participant in participants:
        if age < participant["age"]:
            age = participant["age"]
            oldest_participant = participant

    return oldest_participant

print(get_oldest_participant(participants))


# 6. Write a function that creates a readable summary string for one participant
def format_participant(participant):
    return f"Name: {participant['name']}, Age: {participant['age']}, Student: {participant['is_student']}, Fee: {participant['fee']}"

print(format_participant(joseph))


# 7. Keep input/output responsibilities separate from calculation functions as much as possible
# I feel like I already have input/output separate enough