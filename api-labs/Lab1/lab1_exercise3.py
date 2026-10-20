from api_client import get_json
from dotenv import load_dotenv
import os
import requests

# 1. Create token
# Created a fine-grained PAT

# 2. Store it safely
# Stored it in .env file

# 3. Call the API with the token
load_dotenv()
gh_token = os.getenv("GITHUB_TOKEN")

user_input = input("Enter a GitHub username: ")
repos = get_json(f"https://api.github.com/users/{user_input}/repos",
                 params={"sort": "pushed", "per_page": 5},
                 headers={"Authorization": f"Bearer {gh_token}"})

if repos is not None:
    if repos:
        for repo in repos:
            print(repo["name"])
    else:
        print("User does not have any public repos")


# 4. Prove that the token is used
response = requests.get(f"https://api.github.com/users/{user_input}/repos",
                        params={"sort": "pushed", "per_page": 5},
                        headers={"Authorization": f"Bearer {gh_token}"},
                        timeout=5)
print(response.headers["X-RateLimit-Limit"])  # Prints 5000

response = requests.get(f"https://api.github.com/users/{user_input}/repos",
                        params={"sort": "pushed", "per_page": 5},
                        timeout=5)
print(response.headers["X-RateLimit-Limit"])  # Prints 60


# 5. Break the token on purpose
bad_token = gh_token + "s"
response = requests.get(f"https://api.github.com/users/{user_input}/repos",
                        params={"sort": "pushed", "per_page": 5},
                        headers={"Authorization": f"Bearer {bad_token}"},
                        timeout=5)
print(response.json())  # Bad credentials: 401

# 401 means server doesn't know who I am
# 403 means server knows me but I don't have permissions