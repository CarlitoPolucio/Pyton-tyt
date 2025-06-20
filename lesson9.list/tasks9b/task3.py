user_list = []
while True:
    user_choice = input("Do you want to [add] or [remove] a film: ")
    if user_choice == "add":
        film = input("inter the film: ")
        position = input("inter position in the rating: ")
        if not position.isdigit():
            print("Position Error")
            continue
        if not film in user_list:
            user_list.insert((int(position) - 1), film)
            print(f"Your list:{user_list})")
        else:
            user_list.remove(film)
            user_list.insert((int(position) - 1), film)
            print(f"Film is already in the list. position has been changed on {position}, Your list:{user_list})")
    elif user_choice == "remove":
        film = input("inter the film: ")
        if film in user_list:
            user_list.remove(film)
            print(f"Your list: {user_list}")
        else:
            print("film is not in list")
    else:
        print("Wrong value. Try again.")

