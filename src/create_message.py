import datetime
import re

import getlist

IS_DATE_FORMAT = re.compile(r"\d+/\d+", flags=re.ASCII)


def get_message():
    l = getlist.getlist()
    today = datetime.datetime.today()
    for i in l:
        if IS_DATE_FORMAT.fullmatch(i[1]):
            print(i[1])
            date = datetime.datetime.strptime(i[1], "%m/%d")
            if today.day == date.day and today.month == date.month:
                print(i[2:])


if __name__ == '__main__':
    get_message()
