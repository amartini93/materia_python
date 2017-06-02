__author__ = 'aldo_martini'
import sys
from classes_loader import create_classes
from evaluations_loader import set_evaluations
from schedule_loader import create_schedules
from personas_loader import create_personas, update_coolness, assign_groups


classes = create_classes()
#print(classes)
evaluations = set_evaluations()
#print(evaluations)
students, professors = create_personas()
#print(students)
#print(professors)
schedules = create_schedules()
#print(schedules)
students = update_coolness(students)
students = assign_groups(students)
#print(students)
globals
classes, evaluations, students, professors

class Main_menu:
    def __init__(self):
        self.options = {
                        "1": self.login,
                        "2": self.search,
                        "3": self.end
                        }

    def display_menu(self):
        print("""
            Menu:
                1: Login
                2: Consultar datos
                3: Salir
            """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Ingrese Opcion: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print("{} no es una opcion valida".format(choice))

    def login(self):
        usser = input('Ingrese usuario: ')
        password = input('Ingrese contraseña: ')
        count = 0
        for log_in in professors:
            if usser == log_in.usser and password == log_in.password:
                professor = professors[count]
                professor.logged = True
                print('Bienvenido profesor {}'.format(log_in.name))
                log = professor.log_in()
                break
            else:
                count += 1
        count = 0
        for log_in in students:
            if usser == log_in.usser and password == log_in.password:
                student = students[count]
                student.set_time()
                print('Bienvenid@!!')
                log = student.log_in()
                break
            else:
                count += 1
        if log != True:
            print('Nombre de usuario o contraseña incorrectos')

    def search(self):
        nrc = input('Ingrese el NRC del curso que desea buscar. ')
        for classes in schedules:
            if nrc == classes.nrc:
                print('La clase de {}, nrc: {}.\n'
                      'del profesor {}\n'
                      'se imparte los dias: {}'.format(classes.name, classes.nrc, classes.professors, classes.schedule))

    def add_class(self, student):
        student.take_class()

    def show_schedule(self, student):
        student.show_schedule()


    def end(self):
        sys.exit()



if __name__ == '__main__':
    Main_menu().run()