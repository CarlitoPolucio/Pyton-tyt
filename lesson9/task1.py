num_list = []
while True:
    user_number = int(input("Enter number: "))
    num_list.append(user_number)
    sc_degree = [x ** 2 for x in num_list]
    th_degree = [x ** 3 for x in num_list]
    fd_degree = [x ** 4 for x in num_list]

    print(sc_degree, th_degree, fd_degree)