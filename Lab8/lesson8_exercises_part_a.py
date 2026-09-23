# Part A, Mutable default arguments

# 1. Create a BatTeam calss with name and a default parameter members=[], add an add_member() method
class BadTeam:
    def __init__(self, name, members = []):
        self.name = name
        self.members = members

    def add_member(self, member_name):
        self.members.append(member_name)


# 2. Create 2 BadTeam ojbects without prividing a members list, add a member to only one team and print both lists,
# explain in a comment what happened
bad_team_1 = BadTeam("Bad Team 1")
bad_team_2 = BadTeam("Bad Team 2")
bad_team_2.add_member("Jane")

print(bad_team_1.members)
print(bad_team_2.members)
# members list gets updated in both objects since they share the same instance of members list,
# this is because the list is created on class definition and not object instansiation


# 3. Create a corrected Team class using None as the default value and create a new list inside __init__
class Team:
    def __init__(self, name, members = None):
        self.name = name
        self.members = members if members is not None else []

    def add_member(self, member_name):
        self.members.append(member_name)


# 4. Repeat the test with 2 Team objects and show that each now has its own list
team_1 = Team("Team 1")
team_2 = Team("Team 2")
team_2.add_member("John")

print(team_1.members)
print(team_2.members)