
numbers = int(input("nums: "))

count = 0
number_sum_counter = 0

while count != numbers:
    count += 1
    num = int(input("Enter the num: "))
    number_sum_counter += num
answer = number_sum_counter / numbers
print(answer)