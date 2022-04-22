class Student:
    name = ''
    score = 0
    active = True


a1 = Student()

print(a1.name, a1.score, a1.active)

print('\n###########################################################\n')

a1.name = 'John'
a1.score = 50

print(a1.name, a1.score, a1.active)


s2 = Student()

print(s2.name, s2.score, s2.active)
