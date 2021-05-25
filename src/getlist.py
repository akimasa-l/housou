import requests
import typing
# list[list[str]]
URL = "https://docs.google.com/spreadsheets/d/1lD3B1g7XZU4RDhw9KoZJY6-86NpAtPJqm4Unf0Ovumw/export?gid=0&format=tsv"


def getlist() -> "list[list[str]]":
    response = requests.get(URL)
    print(response.encoding)
    response.encoding = "utf-8"
    text = response.text
    l = text.split("\r\n")
    ans = [i.split("\t")for i in l]
    print(ans)
    return ans
