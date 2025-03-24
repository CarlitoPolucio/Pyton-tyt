def null(prices):
    new_prices = [x if x > 0 else 0 for x in prices]
    return new_prices


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
print(null(original_prices))