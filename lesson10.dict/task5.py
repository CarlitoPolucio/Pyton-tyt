incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

to_remove = [sym for sym in incomes.keys() if incomes[sym] == min(incomes.values())]
print(sum(incomes.values()), to_remove)
del incomes[to_remove[0]]
print(incomes)

