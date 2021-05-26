import json

import requests

with open("../../line/accesstoken.txt") as f:
    BearerToken = f.read().rstrip()


def sendmessage(to, content):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {BearerToken}"}
    message = {"type": "text", "text": content}
    messages = [message]
    body = {
        "to": to,
        "messages": messages,
    }
    print(body)
    h = requests.post(url, headers=headers, data=json.dumps(body))
    print(h.text)


def gettoto():
    with open("../../line/dburl.txt") as f:
        dburl = f.read().rstrip()
    a = requests.get(dburl)
    toto: list[str] = json.loads(a.text)
    return toto


def sendmessage_all(contents: list[str]):
    for to in gettoto():
        for content in contents:
            sendmessage(to, content)
