user_dict = {}
while True:
    new_phone = input("Enter name and numba via space, thank you: ")
    to_add = new_phone.split()
    if to_add[0] in user_dict:
        print("Already in book")
        continue
    elif new_phone == "0":
        break
    user_dict.update({to_add[0]: to_add[1] for _ in range(2)})
    print(user_dict)
