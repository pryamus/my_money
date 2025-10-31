class Money(object):
    def __init__(self, rub: int, kop: int):
        self.rub = rub + kop // 100
        self.kop = kop % 100 # копейки не должны превышать 99

    def get_rub(self):
        """ self - это ссылка на конкретный экземпляр при вызове метода. """
        return self.rub

    def get_kop(self):
        return self.kop

    def __str__(self) -> str:
        return f'{self.rub} руб. {self.kop} коп.'

    def __add__(self, other):
        """ Реализация оператора +. Главные - это левый операнд.
            Dunder(magic) метод вызывается неявно, когда объект участвует в
            соответствующей операции.
        """
        return Money(self.rub + other.rub, self.kop + other.kop)

    def __sub__(self, other):
        """ Реализация оператора - (вычитание)"""
        pass

    def __truediv__(self, other):
        """ Реализация оператора / (деление)"""
        pass


if __name__ == '__main__':
    money1 = Money(20, 120)
    money2 = Money(30, 390)
    print(f'{money1.rub = }, {money1.kop = }')
    # Скопировать строку: Ctrl + D
    print(f'{money2.rub = }, {money2.kop = }')
    # Явный вызов явных методов
    print(money1.get_rub(), money1.get_kop())  # Money.get_rub(self=money1)
    print(money1)
    print(money2)
    # Проверка работы оператора +
    money3 = money1 + money2
    print(money3)
    print("Атрибуты экземпляра:", vars(money1)) # вернет словарь полей(fields)
