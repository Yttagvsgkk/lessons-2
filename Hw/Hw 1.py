class Person:
    def __init__(self, nema, age, city):
        self.nema = nema
        self.age = age
        self.city = city

    def introduce(self):
        return f"Привет, меня зовут {self.nema}, мне {self.age} лет, я живу в {self.city}"


    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


woman = Person('Милана', 20, 'Бишкек')
print(woman.introduce())
men = Person('Михаил', 16, 'Москва')
men = Person('Максим', 18, 'Алматы')


print(men.is_adult())
print(men.is_adult())

print(woman)