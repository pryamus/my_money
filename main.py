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
        return f'{self.rub} руб. {self.kop:02d} коп.'

    def __add__(self, other):
        """ Реализация оператора +. Главные - это левый операнд.
            Dunder(magic) метод вызывается неявно, когда объект участвует в
            соответствующей операции.
        """
        return Money(self.rub + other.rub, self.kop + other.kop)

    def __mul__(self, scalar: int):
        """ Реализуем умножение числа на монету. """
        return Money(self.rub * scalar, self.kop * scalar)

    def __rmul__(self, scalar: int):
        """ self(money instance) будет правым операндом и он
            будет вызывать этот dunder метод"""
        return self * scalar  # реализовали через self.__mul__()


if __name__ == '__main__':
    money1 = Money(20, 120)
    money2 = Money(30, 390)
    print(f'{money1.rub = }, {money1.kop = }')
    # Скопировать строку: Ctrl + D
    print(f'{money2.rub = }, {money2.kop = }')
    # Явный вызов явных методов
    print(money1.get_rub(), money1.get_kop())  # Money.get_rub(self=money1)
    print(money1, money2)
    # Проверка работы оператора +
    money3 = money1 + money2
    print(money3)
    print("Атрибуты экземпляра:", vars(money1)) # вернет словарь полей(fields)
    money4 = money1 * 5  # money1.__mul__(5)
    print(money4)
    money5 = 5 * money1 # 5.__mul__(money1) -> NotImplemented -> money1.__rmul__(5) -> Done
    print(money5)
