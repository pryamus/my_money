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
print(Person.name)
print(Person.surname)
print(Person.age)

# Instance - экземпляр
person1 = Person()
person2 = Person()
print("before:", person1.name, person1.surname)
print("before:", person2.name, person2.surname)
person1.name = "Petr"
person2.surname = "Sidorov"
print("after:", person1.name, person1.surname)
print("after:", person2.name, person2.surname)