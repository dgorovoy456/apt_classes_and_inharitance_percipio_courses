from pprint import pprint


class Dog:
    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed

    def print_details(self):
        print('My name is %s and I am a %s' % (self.__name, self.__breed))

    def change_name(self, name):
        self.__name = name


d1 = Dog('Tayson', 'Reachbeck')

d1.print_details()

d1.change_name('Hanna')

d1.print_details()