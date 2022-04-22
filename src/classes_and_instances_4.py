class Student:
    def __init__(self, name):
        self.name = name
        self.email = name + '.' + '@gmail.com'


a1 = Student('Denys')

a2 = Student(name='Anna')

print(a1)
print(a1.name)
print(a1.email)

a1.name = 'Some'

print(a1.name)
print(a1.email)