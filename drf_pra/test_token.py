import requests

JWT_TOKEN = (
     "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
     "eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNjA0Mzk2MDM4LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjA0Mzk1NzM4fQ."
     "DMmTVFxtLr1AJyFa8x5vrwI4gc2rBTgXJoH_1LFY4iw"
)

# "eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwiZXhwIjoxNjA0Mzk1NTEwLCJlbWFpbCI6IiJ9"

headers = {
    'Authorization': f'JWT {JWT_TOKEN}',
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())