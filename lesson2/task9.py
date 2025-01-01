apples = int(input("Сколько у вас яблок (тонн), гайз?: "))
print("Доступные ящики: 3, 5, 6 тонн")
box_type = int(input("Введите подходящий тип ящиков: "))
result1 = apples // box_type
result2 = apples % box_type
print(f"Вы получите {result1} полных ящиков,", end=" ")
print(f"и {result2} тонн яблок останется")

