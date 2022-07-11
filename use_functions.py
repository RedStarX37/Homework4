
balance = 0
history = {}

def increase_balance():
    global balance  # я уяснил, что использование глобальных переменных нежелательно, но решил, что хоть где-то попробовать надо, да и счёл, что здесь это будет к месту
    summ = input('Укажите сумму пополнения: ')
    balance += int(summ)
    print('Ваш баланс: ' + str(balance) + '\n')


def purchase():
    global balance #см. выше
    global history #см. выше
    print('')
    price = input('Укажите сумму покупки: ')
    if int(price) <= balance:
        good = input('Укажите название покупки: ')
        history.update({str(good): str(price)})
        print('Поздравляем с покупкой!')
        balance -= int(price)
        print('Ваш баланс: ' + str(balance) + '\n')
    else:
        print('Недостаточно средств.\n')


def purchase_hist():
    global history  # см. выше
    print('')
    for key, value in history.items():
        print(key, value)
    print('')


while True:
    print('1. Пополнение счета\n2. Покупка\n3. История покупок\n4. Выход')
    selection = input('Выберите пункт меню: ')
    if selection == '1':
        increase_balance()
        pass
    elif selection == '2':
        purchase()
        pass
    elif selection == '3':
        purchase_hist()
        pass
    elif selection == '4':
        print('')
        print('Спасибо что пользуетесь услугами нашего банка!')
        break
    else:
        print('Неверный пункт меню.')
        print('')