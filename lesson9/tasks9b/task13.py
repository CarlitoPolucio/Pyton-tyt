def buddies_count(guests):
    while True:
        come_check = input("пришёл(1) или ушёл?(0): ")
        if come_check == "1":
            add = input("Who: ")
            guests.append(add)
            if len(guests) > 6:
                print("You need to care about less than six nigs >>>", guests)
        elif come_check == "0":
            delete = input("Who: ")
            guests.remove(delete)
            print(guests)
        else:
            if len(guests) > 6:
                print(f"{len(guests) - 6} nigs stayed outside. good night")
            else:
                return "good night"


guest = ["Семён", "Данил", "Саша", "Серафим", "Солидол"]
print(buddies_count(guest))

