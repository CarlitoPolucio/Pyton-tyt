user_input = input("Enter the text: ")

count = -1

for letter in user_input:
    count += 1

index_a = -1
index_b = 0

while index_a != count:
    index_a += 1
    index_b -= 1
    if user_input[index_a] != user_input[index_b]:
        print("it is not palindrome")
        break
else:
    print("it is palindrome")

