credit = int(input("sum of credit: "))
pay = int(input("month pay: "))
year_percent = int(input("year percent: "))
grace_period = int(input("grace period: "))
loan_date = int(input("Enter the loan date: "))

count = 1
percent_counter = 0
first_month_percent = 0
overpayment = 0

print("As paying data has been taken first day of the month, because banks count interest on balance every day.")
print("So advise is take credit in the last day of month")

first_month_days = 30 - loan_date
if first_month_days > 0:
    first_month_percent = (credit * (year_percent / 100) // 365) * first_month_days
    percent_counter = first_month_percent

while credit > 0:
    credit -= pay
    count += 1
    percent = (credit * (year_percent / 100)) // 12
    percent_counter += percent
    if count == grace_period + 1:
        credit += percent_counter
        print(f"interest accrued: {percent_counter} ", end="")
    elif count > grace_period + 1:
        credit += percent
        if credit < 0 or percent < 0:
            credit = 0
            percent = 0
        print(f"interest accrued: {percent} ", end="")
    print(f"Month {count}. Credit: {credit}" )

print(f"Overpayment: {percent_counter} ")

