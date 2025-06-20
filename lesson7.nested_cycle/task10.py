user_input = int(input("Enter the size of matrice: "))

one = "1"
two = "2"
zero = "0"
counter = 1
two_counter = 0

print(" ".join(zero * (user_input - 1)),"" + one)

for num in range(2, user_input + 1):
    counter += 1
    two_counter += 1
    values = " ".join(zero * (user_input - counter) + one + two * two_counter)
    print(values)
