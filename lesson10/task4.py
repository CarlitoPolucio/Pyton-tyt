def tasks(main_list, first, second, third):
    main_list += first + second + third
    return main_list, len([main_list[:].remove(num) for num in main_list if num == 0])


main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0]
first_company = [0, 0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

print(tasks(main, first_company, second_company, third_company))

