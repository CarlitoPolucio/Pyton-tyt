import random

original_prices = [random.randint(-50, 50) for x in range(1, 10)]

new_prices = [0 if x < 0 else x for x in original_prices[:]]

print("Мы потеряли:", abs(sum(original_prices) - sum(new_prices)))
