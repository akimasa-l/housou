import create_message
import sendmessage_LINE


def main():
    messages = create_message.create_messages(create_message.get_raw_songs())
    sendmessage_LINE.sendmessage_all(messages)


if __name__ == '__main__':
    main()
