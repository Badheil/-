import requests
import json
import pickle

users = requests.get('https://jsonplaceholder.typicode.com/users')
data = {user["id"]: {
    "id": user["id"],
    "username": user["username"],
    "email": user["email"],
    "posts": 0,
    "comments": 0
    } for user in json.loads(users.text)
    }

ids = [id for id in data]
for i in ids:
    posts = requests.get('https://jsonplaceholder.typicode.com/users/{}/posts'.format(i))
    posts = json.loads(posts.text)
    data[i]["posts"] = len(posts)
    for post in posts:
        comments = requests.get(f'https://jsonplaceholder.typicode.com/comments/{post["id"]}')
        comments = json.loads(comments.text)
        if data[i]["email"] == comments["email"]:
            data[i]["comments"] += 1

response = requests.post(
        "https://webhook.site/9e47c6ac-79e0-49b0-b95a-398b24fd2a22",\
        data= json.dumps({"statistics": [data[id] for id in data]})
        )
with open("solution.pickle", 'wb') as f:
    pickle.dump(response, f)

    
# with open("solution.pickle", 'rb') as f:
#     data_new = pickle.load(f)



# info = json.dumps({"statistic": [data[id] for id in data]})
# stud = {}
# star = {}
# star = json.loads(info)
# print(star)
# star['statistic'] = sorted(star["statistic"], key=lambda v: v["id"])
# print(star['statistic'])




        # print(post["id"])
    # print(json.loads(comments.text))