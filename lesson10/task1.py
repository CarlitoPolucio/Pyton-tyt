def animals(array):
    array.insert(1, "bear")
    array.remove("elephant")
    return array, f"lion is in cage: {array.index("lion") + 1}, monkey is in cage: {array.index("monkey") + 1}"


zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print(animals(zoo))
