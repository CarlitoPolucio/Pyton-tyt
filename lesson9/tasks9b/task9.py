def goods_change(goods_list):
    user_fruit = input("Enter fruit and its price [apple 100]: ").split()
    goods_list.append(user_fruit)
    return [[x for x in fruit if str(x).isalpha()] + [int(x) * 1.08 for x in fruit if str(x).isdigit()] for fruit in goods_list]


goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print(goods_change(goods))