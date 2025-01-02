hours = int(input("Work hours: "))
credit = int(input("Loan balance: "))
food = int(input("Food expenses: "))

expenses = credit + food
salary = (200 * hours) // 2**3 + hours
to_work = expenses - salary
need_hours = to_work // 26 + 1

if salary >= expenses:
    print(f"Your salary is {salary}$. It is enough, you can relax!")
else:
    print(f"Go to work, man! You are missing {to_work}$. It is {need_hours} hours.")


