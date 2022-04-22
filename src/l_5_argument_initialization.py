class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = f'{first}.{last}@gmail.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def uppercase(self):
        self.first = self.first.upper()
        self.last = self.last.upper()

    def email(self):
        return f'{self.mail}'


a1 = Student('Denys', 'Horovyi')

print(a1.fullname())
print(a1.email())

print(Student.fullname(a1))

print('\n##############################################################\n')

a1.uppercase()


print(a1.fullname())
print(a1.email())

print(Student.fullname(a1))

