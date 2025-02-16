def index(weight, height):
    return weight / (height ** 2)

def index_checker(weight_index):
    if weight_index < 18.5:
        return "deficit"
    elif 18.5 <= weight_index < 25:
        return "OK"
    elif 25 <= weight_index < 30:
        return "Excess"
    else:
        return "Fat"

w = float(input("Enter weight (kg): "))
h = float(input("Enter height (m): "))

print(index_checker(index(w, h)))

