import json

import requests

with open("../youtube/api_key.txt") as f:
    API_KEY = f.read().rstrip()
#print("API key: " + API_KEY)


def search(keyword: str):
    url = f"https://www.googleapis.com/youtube/v3/search?type=video&part=snippet&q={keyword}&key={API_KEY}"
    response = requests.get(url)
    response.encoding = "UTF-8"
    data: dict = json.loads(response.text)
    return data


def get_url(data: dict):
    return "https://www.youtube.com/watch?v="+data["items"][0]["id"]["videoId"]


def main():
    data = search("キセキ GReeeeN")
    print(json.dumps(data, indent=4))
    print(get_url(data))


if __name__ == "__main__":
    main()
