__author__ = 'aldo_martini'

import sys

class Professor_menu:
    def __init__(self, professor):
        self.professor = professor
        self.options = {
                        "1": self.give_permission,
                        }

    def display_menu(self):
        print("""
            Menu:
                1: Dar permiso
                2: Salir
            """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Ingrese Opcion: ")
            if choice == '2':
                break
            else:
                action = self.options.get(choice)
                if action:
                    action()
                else:
                    print("{} no es una opcion valida".format(choice))
        return


    def give_permission(self):
        self.professor.give_permission()


    def end(self):
        sys.exit()



if __name__ == '__main__':
    Professor_menu().run()
