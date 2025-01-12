educational_grant = int(input("Enter the grant: "))
expenses = int(input("Enter the expenses: "))

count = 0
educational_grant *= 10
expenses_counter = expenses

while count != 9:
    count += 1
    expenses *= 1.03
    expenses //= 1
    expenses_counter += expenses
    print(expenses, expenses_counter)

answer = educational_grant - expenses_counter
if answer < 0:
    answer //= -1
    print(f"need also: {answer}")
else:
    print(f"money is enough: {answer} gonna left")
