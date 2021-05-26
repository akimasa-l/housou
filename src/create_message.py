import datetime
import re

import getlist
import search_youtube

IS_DATE_FORMAT = re.compile(r"\d+/\d+", flags=re.ASCII)


def get_message():
    l = getlist.getlist()
    today = datetime.datetime.today()
    for i in l:
        if IS_DATE_FORMAT.fullmatch(i[1]):
            # print(i[1])
            date = datetime.datetime.strptime(i[1], "%m/%d")
            if today.day == date.day and today.month == date.month:
                return i[2:]


def get_search_keyword(message: list[str]) -> list[str]:
    it = iter(message)
    return [search_youtube.get_url(search_youtube.search(f"{i} {j}")) for i, j in zip(it, it)if i != "" and j != ""]


def main():
    message = get_message()
    print(get_search_keyword(message))


if __name__ == '__main__':
    main()
