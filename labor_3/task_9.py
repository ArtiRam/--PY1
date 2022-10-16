def money_counter(salary, spend, months, increase):
    need_money = 0
    for i in range(1, months + 1):
        if i == 1:
            spend = spend
        else:
            spend = spend * increase + spend

        need_money += spend - salary
    return print(int(need_money))


money_counter(salary=5000, spend=6000, months=10, increase=0.03)
