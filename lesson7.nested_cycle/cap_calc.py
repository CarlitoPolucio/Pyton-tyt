invest_money = int(input("invested money per month: "))
percent = float(input("Year capitalization: "))
withdrawal = int(input("withdrawal per month: "))
period = int(input("invest period: "))
count = 1
get_month_cap = 0
total_invest = invest_money
monthly_invest = 0
cap_total_count = 0

while period > 0:
    period -= 1
    count += 1
    get_month_cap = ((total_invest * percent) / 12) // 1
    total_invest += invest_money + get_month_cap
    monthly_invest = invest_money + get_month_cap
    cap_total_count += get_month_cap
    if count > 12:
        #total_invest -= withdrawal
        invest_money = 0
    print(f"{count} month. Total invest: {total_invest},get month cap. {get_month_cap}, monthly invest {monthly_invest}. total percentage {cap_total_count}")

