def index_sum(massive, divider):
    answer = 0
    for  i, num in enumerate(massive):
        if num % divider == 0:
            answer += i
    return answer


user_list = 1, 3, 4, 6, 7, 9
K = 3

print(index_sum(user_list, K))