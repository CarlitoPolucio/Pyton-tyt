def out_matrix(array):
    output = f"{array[0]} \n{array[1]} \n{array[2]}"
    return output.replace(",", " ")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(out_matrix(matrix))
