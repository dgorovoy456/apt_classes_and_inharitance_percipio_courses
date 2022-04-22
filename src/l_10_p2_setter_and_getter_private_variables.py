class Dog:
    """
    This is a class which defines a dog.
    This includes cute dogs as well as ferocious dogs.
    """
    __species = 'canine'

    def __init__(self, name, breed):
        self.__name = name
        self.__breed = breed
        self.__tricks = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_breed(self):
        return self.__breed

    def set_bread(self, breed):
        self.__breed = breed

    def add_trick(self, trick):
        self.__tricks.append(trick)

    def print_details(self):
        print('My name is %s and I am a %s and I can do tricks: %s'
              % (self.__name, self.__breed, self.__tricks))


d1 = Dog('Tayson', 'Reachback')

d1.print_details()

d1.add_trick('roll over')

d1.print_details()

d1.set_bread('Labrador')

d1.print_details()

