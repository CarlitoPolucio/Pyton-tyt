def to_find(detail):
    price = 0
    shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
            ['обод', 2000], ['шатун', 200], ['седло', 2700]]
    amount = [item for sublist in shop for item in sublist].count(detail)
    for sublist in shop:
        for i, value in  enumerate(sublist):
            if value == detail:
                price += sublist[i + 1]
    return price, amount


need_find = "седло"
print(to_find(need_find))