from pprint import pprint


class Dog:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    def print_details(self):
        print('My name is %s and I am a %s' % (self.__name, self.__breed))


d1 = Dog('Tayson', 'Reachbeck')

d1.print_details()

d1.__name = 'Nemo'

d1.print_details()

pprint(Dog.__dict__)
print(d1.__dict__)

d1._Dog__name = 'Namo'

d1.print_details()
