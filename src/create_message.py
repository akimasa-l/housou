import datetime
import re

import getlist
import search_youtube

IS_DATE_FORMAT = re.compile(r"\d+/\d+", flags=re.ASCII)


def get_raw_songs():
    l = getlist.getlist()
    today = datetime.datetime.today()
    for i in l:
        if IS_DATE_FORMAT.fullmatch(i[1]):
            # print(i[1])
            date = datetime.datetime.strptime(i[1], "%m/%d")
            if today.day == date.day and today.month == date.month:
                return i[2:]


def get_songs(raw_songs: list[str]):  # (曲名,歌手名)のtuple
    it = iter(raw_songs)
    return [(song, singer) for song, singer in zip(it, it)if song != "" and singer != ""]


def get_search_keyword(raw_songs: list[str]) -> list[str]:
    return [search_youtube.get_url(search_youtube.search(f"{song} {singer}")) for song, singer in get_songs(raw_songs)]


def create_messages(raw_songs):
    songs = get_songs(raw_songs)
    message = "本日お送りする曲は！\n"
    for song, singer in songs:
        message += f"{singer}の{song},\n"
    message += "です！"
    return get_search_keyword(raw_songs)+[message]


def main():
    raw_songs = get_raw_songs()
    print(get_search_keyword(raw_songs))


if __name__ == '__main__':
    main()
