num = int(input("Введите четырёхзначное число: "))
result1 = num // 1000
result2 = result1 * 1000
result3 = num - result2
result4 = result3 // 100
result5 = num % 10
result6 = num - result5
result7 = (result6 % 100) // 10

print(result1, result4, result7, result5)
