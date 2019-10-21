# программа получает на вход количество месяцев, за которые человек хочет накопить денег
# на покупку товара (period of time). далее пользователь вводит свою зарплату (salary) и
# количество расходов за месяц (costs_number). позже пользователь вводит сколько денег
# было потрачено (costs). программа высчитвает сколько денег было накоплено (save).
# затем человек вводит цену желаемого товара (price of product) и программа выдает
# насколько хорошо справился человек.

period = int(input('Period of time: '))
rest = 0
save = 0
for i in range(period):
    salary = int(input('Salary: '))
    costs_number = int(input('Number of costs during month: '))
    for j in range(costs_number):
        costs = int(input('How much money spent: '))
        rest = salary - costs
        salary = rest
    save += rest
print('You saved: ', save)
price = int(input('Price of product: '))
if save > price:
    print('Good job!')
elif save == price:
    print('Could be better, but enough')
else:
    print('Not enough! Think more.')