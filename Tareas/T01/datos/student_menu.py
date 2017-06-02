__author__ = 'aldo_martini'

import sys

class Student_menu:
    def __init__(self, student):
        self.student = student
        self.options = {
                        "1": self.add_class,
                        "2": self.delete_class,
                        "3": self.show_schedule,
                        }

    def display_menu(self):
        print("""
            Menu:
                1: Agregar clase
                2: Botar ramo
                3: Mostrar horario
                4: Salir
            """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Ingrese Opcion: ")
            if choice == '4':
                break
            else:
                action = self.options.get(choice)
                if action:
                    action()
                else:
                    print("{} no es una opcion valida".format(choice))
        return


    def add_class(self):
        self.student.take_class()

    def show_schedule(self):
        self.student.show_schedule()

    def delete_class(self):
        self.student.delete_class()

    def end(self):
        sys.exit()



if __name__ == '__main__':
    Student_menu().run()
