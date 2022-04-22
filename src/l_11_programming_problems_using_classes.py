class Student:
    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa
        self.__clubs = set()
        self.__active = True

    def set_name(self, name):
        self.__name = name

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def add_club(self, club):
        self.__clubs.add(club)

    def remove_club(self, club):
        self.__clubs.remove(club)

    def set_active(self, active):
        self.__active = active

    def print_details(self):
        print(f'Student: {self.__name}')
        print(f'{self.__gpa}, {self.__clubs}, {self.__active}')


s = Student('Denys', 3.8)

s.print_details()

s.add_club('Yoga')

s.print_details()

s.add_club('yoga')

s.print_details()

s.set_gpa(3.9)

s.print_details()

student_details_list = [
    {'name': 'Anna', 'gpa': '3.6', 'clubs': ['tennis', 'chess']},
    {'name': 'Vadym', 'gpa': '3.5', 'clubs': ['tennis'], 'active': False},
    {'name': 'Max', 'gpa': '3.4', 'clubs': ['football', 'chess']},
    {'name': 'Vova', 'gpa': '3.3', 'is_honors_student': True}
]


def get_students(student_detail_list):
    student_list = []

    for student_details in student_detail_list:
        if 'name' not in student_details or 'gpa' not in student_details:
            continue
        s = Student(student_details['name'], student_details['gpa'])

        if 'clubs' in student_details:
            for club in student_details['clubs']:
                s.add_club(club)

        if 'active' in student_details:
            s.set_active(student_details['active'])

        student_list.append(s)

    return student_list


for i in get_students(student_details_list):
    i.print_details()
