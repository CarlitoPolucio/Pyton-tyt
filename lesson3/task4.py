first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
numbers_sum = int(input("Enter the sum of the numbers: "))
right_answer = first_number + second_number
if right_answer == numbers_sum:
    print("Answer is right!")
else:
    print(f"Wrong answer. Right one is {right_answer}.")