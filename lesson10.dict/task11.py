goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [  # Лампа
        {'quantity': 27, 'price': 42},
    ],
    '23456': [  # Стол
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [  # Диван
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [  # Стул
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good, code in goods.items():
    count = 0
    for inf in store[code]:
        count += inf["quantity"] * inf["price"]
    print(f"{good}: {count}", end="\n")







