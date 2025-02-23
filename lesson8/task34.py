x = 1
answer = 1
answer_min_check = 0
while x > 0:
    answer = x ** 3 - 3 * x ** 2 - 12 * x + 10
    if answer > 0:
        print(answer, x)
        break
    else:
        answer_min_check = answer
    x -= 0.001
    print(answer, x)