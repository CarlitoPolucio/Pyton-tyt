import os

if __name__ == '__main__':
    user_name = input("Enter username: ")
    with open(os.path.join(os.getcwd(), "chat.txt"), mode="a+", encoding="UTF-8") as chat:
        while True:
            user_action = input("Write your massage (press enter to see the current chat): ")
            if user_action != "":
                chat.write(f"{user_name}: {user_action}\n")
            else:
                chat.seek(0)
                for line in chat.readlines():
                    print(line, end="")

