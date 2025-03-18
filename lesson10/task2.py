def employees(array):
    [array.remove(num) for num in array if num == 0]
    return f"{len(array)} Employees left, they have next wages: {array}. Minimum wage is {min(array)}, maximum wage is {max(array)}"


wages = [0, 11, 0, 18, 13, 0, 14, 0, 15, 13]
print(employees(wages))
