
def birthyear():
    year = input('Ввведите год рождения А.С.Пушкина: ')
    while year != '1799':
        print("Не верно")
        year = input('Ввведите год рождения А.С.Пушкина:')


def birthday():
    day = input('Ввведите день рождения Пушкин: ')
    while day != '06.06':
        print("Не верно")
        day = input('Ввведите день рождения Пушкин: ')


def pushkin():
    birthyear()
    birthday()


pushkin()
print('Верно')