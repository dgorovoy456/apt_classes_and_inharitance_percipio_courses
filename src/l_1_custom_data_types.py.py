class Student:
    pass


print(type(Student))

object_1 = Student()

object_2 = Student()

print(object_1)

print(object_2)

print(isinstance(object_1, Student))

print(isinstance(object_2, Student))

print('\n###############################################################\n')

object_1.name = 'Michel'

object_1.email = 'Michel@gmail.com'

print(object_1.name)

print(object_1.email)

object_2.name = 'Denys'

object_2.email = 'Denys@gmail.com'

print(object_2.name)

print(object_2.email)

