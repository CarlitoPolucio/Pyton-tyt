hours = int(input("Work hours: "))
credit = int(input("Loan balance: "))
food = int(input("Food expenses: "))

expenses = credit + food
salary = (200 * hours) // 2 ** 3 + hours
to_work_sum = expenses - salary
need_hours = to_work_sum // 26 + 1

if salary >= expenses:
    print(f"Your salary is {salary}$. It is enough, you can relax!")
else:
    print(f"Go to work, man! You are missing {to_work_sum}$. It is {need_hours} hours.")

# Исправление + оптимизация:
hours = int(input("Work hours: "))
credit = int(input("Loan balance: "))
food = int(input("Food expenses: "))

HOURS_FACTOR = 26  # Константы(не меняющиеся значения в потоке выполнения) принято писать в uppercase и разделять слова _
expenses = credit + food
salary = (200 * hours) / 8 + hours

if salary >= expenses:
    print(f"Your salary is {salary}$. It is enough, you can relax!")
else:
    to_work_sum = expenses - salary
    need_hours = to_work_sum // HOURS_FACTOR
    if need_hours == 0:
        need_hours = 1
    else:
        need_hours = need_hours if to_work_sum % HOURS_FACTOR == 0 else need_hours + 1  # Подобная проверка-выражение называется тернарной операцией и служит сокращением.
    print(f"Go to work, man! You are missing {to_work_sum}$. It is {int(need_hours)} hours.")


