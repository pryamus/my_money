# ===================================================
# ООП - это объектно-ориентированное программирование
# ===================================================
# Зачем нам нужно ООП?
# Составные части: абстракция, полиморфизм, инкапсуляция, наследование
# Использовать ООП ради ООП.
# Инструмент под задачу.
# Суть ИТ - автоматизация реальных объектов через модели.
# Есть много хороших и полезных типов данных: int, str, float, list, dict, ...

# Есть абстракции: Person, Employee, Car, Factory, House, Profit
# ООП - это механизм(возможность) создания своих типов(классов) данных через описание свойств и поведения
# attributes(fields + methods)

# =====
# Класс
# =====
# Класс - это шаблон. Мы хотим на основе шаблона создать много представителей
# этого типа данных - экземпляров(instances)
# Смысл в том, что набор атрибутов(свойств) будет у всех одинаковый, но значения этих свойств будут разные,
# свои собственные.
# Пример: класс Car, field - color

class Person:
    name = "Ivan"
    surname = "Petrov"
    age = 18


# Класс один, а нам нужно много человек
# print(Person.name)
# print(Person.surname)
# print(Person.age)

# Instance - экземпляр
# person1 = Person()
# person2 = Person()
# print("before:", person1.name, person1.surname)
# print("before:", person2.name, person2.surname)
# person1.name = "Petr"
# person2.surname = "Sidorov"
# print("after:", person1.name, person1.surname)
# print("after:", person2.name, person2.surname)

# Можно ли сразу создавать экземпляры с собственными значениями? Да, конечно.
# Различие между функциями и методами
# Метод - это функция, которая связана с определенным типом данных(экземпляром класса)
# lst = [3.23, 4.23]
# s = 'hello'
# print(sum(lst), min(lst), max(lst), len(s), round(lst[0], 1)) # это функции
# print(s.upper()) # это метод
# lst.append(100.23) # это метод
# lst.sort()
# print(lst)

class Money(object):
    def __init__(self, rub: int, kop: int):
        """ dunder(magic) - неявный метод. Конструктор класса.
            self - это ссылка на конкретный экземпляр и это всегда первый позиционный аргумент.

        """
        self.rub = rub + kop // 100
        self.kop = kop % 100 # копейки не должны превышать значения 99

    def get_rub(self):
        """ self - это ссылка на конкретный экземпляр при вызове метода """
        return self.rub

    def get_kop(self):
        """ self - это ссылка на конкретный экземпляр при вызове метода """
        return self.kop

    def __str__(self) -> str:
        return f'{self.rub} руб. {self.kop:02d} коп.'

    def __add__(self, other):
        """ Реализация оператора +. Главный это левый операнд
            dunder(magic) метод вызывается неявно, когда объект участвует в соответствующей операции
            m1 + m2 -> m1.__add__(m2)
        """
        return Money(self.rub + other.rub, self.kop + other.kop)

    def __mul__(self, scalar):
        """ Реализация оператора *.  Главный это левый операнд. """
        return Money(self.rub * scalar, self.kop * scalar)

    def __rmul__(self, scalar):
        """ Реализация оператора *.  Главный это правый операнд. """
        return self * scalar



if __name__ == "__main__":
    money1 = Money(20, 120)
    money2 = Money(30, 390)
    print(f'{money1.rub = }, {money1.kop = }')
    # Вызов явного метода
    print("money1", money1.get_rub(), money1.get_kop())
    print(f'{money2.rub = }, {money2.kop = }')
    print("money2", money2.get_rub(), money2.get_kop())
    print(money1)
    money3 = money1 + money2
    print('money3:', money3)
    money4 = money1 * 5
    print('money4:', money4)
    money5 = 5 * money1 # 5.__mul__(money1) -> NotImplemented -> money1.__rmul__(5)