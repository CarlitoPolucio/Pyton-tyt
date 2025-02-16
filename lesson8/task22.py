def comparison(a, b):
    comp = a + b
    if str(f"{a:.2e}") == str(f"{comp:.2e}"):
        return "Budget hasn't changed"
    else:
        return "Budget has changed"

budget = float(input("Enter the budget: "))
income = float(input("Enter the income: "))

print(comparison(budget,income))