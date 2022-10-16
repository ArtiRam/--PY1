def count_of_month(money_capital, spend, increase, salary, month=0):

    while money_capital > 0:
        if month == 0:
            spend = spend
        else:
            spend = spend * increase + spend

        money_capital = money_capital + salary - spend
        month += 1

    return print(month - 1)


count_of_month(money_capital=10000, spend=6000, increase=0.05, salary=5000)
