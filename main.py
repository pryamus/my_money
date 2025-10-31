class Money:
    def __init__(self, rub: int, kop: int):
        self.rub = rub + kop // 100
        self.kop = kop % 100 # копейки не должны превышать 99


if __name__ == '__main__':
    money1 = Money(20, 120)
    money2 = Money(30, 330)
    print(f'{money1.rub = }, {money1.kop = }')
    # Скопировать строку: Ctrl + D
    print(f'{money2.rub = }, {money2.kop = }')
