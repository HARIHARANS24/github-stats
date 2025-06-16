import os
import requests

token = os.getenv("ACCESS_TOKEN")
headers = {"Authorization": f"token {token}"}

user = "HARIHARANS24"  # Replace with your username
r = requests.get(f"https://api.github.com/users/{user}", headers=headers)

with open("generated/overview.txt", "w") as f:
    f.write(str(r.json()))
