__author__ = 'aldo_martini'

from student_menu import Student_menu
from professor_menu import Professor_menu
from schedule_loader import create_schedules, Schedule
from evaluations_loader import set_evaluations

schedules = create_schedules()
#print(schedule)
evaluations = set_evaluations()

globals
schedules, evaluations

class Person:
    def __init__(self, password='', name='', usser='', idols='', app_class='', **kwargs):
        self.password = password
        self.name = name
        self.usser = usser
        self.idols = idols
        self.app_class = app_class


class Student(Person):
    students = []
    groups = {'1': ['08:30', '10:30'], '2': ['09:30', '11:30'], '3': ['10:30', '12:30'], '4': ['11:30', '13:30'],
              '5': ['12:30', '14:30'], '6': ['13:30', '15:30'], '7': ['14:30', '16:30'], '8': ['15:30', '17:30'],
              '9': ['16:30', '18:30'], '10': ['17:30', '19:30']}
    schedule = []
    for day in range(5):
        blocks = []
        for block in range(8):
            blocks.append([])
        schedule.append(blocks)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.to_take = []
        self.coolness = 0
        self.group = None
        self.time_start = None
        self.time_end = None
        self.logged = False
        self.schedule = Student.schedule
        self.credits = 0
        self.evaluations = {}
        self.exceptions = []

    def update_schedule(self, _class):
        ## data=[[ncat_days, nayud_days, nlab_days], [ncat_block, nayud_block, nlab_block]
        data = self.make_schedule(_class)
        for day in data[0][0]:
            for block in data[1][0]:
                self.schedule[day][block] = 'Catedra ' + _class.name + ' ' + _class.campus
        for day in data[0][1]:
            for block in data[1][1]:
                self.schedule[day][block] = 'Ayudantia ' + _class.name + ' ' + _class.campus
        for day in data[0][2]:
            for block in data[1][2]:
                self.schedule[day][block] = 'Lab ' + _class.name + ' ' + _class.campus
        print('Haz inscrito el curso: {}'.format(_class.name))


    def set_time(self):
        self.time_start = Student.groups[self.group][0]
        self.time_end = Student.groups[self.group][1]

    def log_in(self):
        self.logged = False ##pormientras, hasta que haga una funcion para desloguear
        while True:
            time = input('Ingrese la hora actual en formato\n'
                     'hh:mm\n')
            if len(time.split(':')) != 2:
                print('Formato de la hora mal ingresado, intentelo denuevo')
            else:
                break
        time = time.split(':')
        group_time_start = self.time_start.split(':')
        group_time_end = self.time_end.split(':')
        if int(time[0]) not in range(int(group_time_start[0]), int(group_time_end[0]) + 1):
            print('No estas ingresando en el horario que corresponde\n'
                  'Intentalo  denuevo entre {} y {}'.format(self.time_start, self.time_end))
            return
        else:
            if int(time[0]) == int(self.time_start[0]) and int(time[1]) < int(self.time_start[1]):
                print('No estas ingresando en el horario que corresponde\n'
                      'Intentalo  denuevo entre {} y {}'.format(self.time_start, self.time_end))
                return
            elif int(time[0]) == int(self.time_end[0]) and int(time[1]) > int(self.time_end[1]):
                print('No estas ingresando en el horario que corresponde\n'
                      'Intentalo  denuevo entre {} y {}'.format(self.time_start, self.time_end))
                return
            else:
                print('Logueaste en tu horario')
                self.logged = True
                Student_menu(self).run()
                return True

    ##chequea los requisitos, retorna True o False, por el momento no verifica equivalencias
    def check_requirements(self, initials):
        for _class in Schedule.requirements:
            if _class.initials == initials:
                requirements = _class.requirements[0]
                #print(requirements)
                #print(self.app_class)
                if requirements[0] == 'No tiene':
                    return True
                else:
                    if len(requirements) == 1:
                        if requirements[0] in self.app_class:
                            print('Si cumple los requisitos')
                            return True
                        elif requirements[0] not in self.app_class:
                            print('No cumple el requisito: {}'.format(requirements[0]))
                            return False
                        if requirements[0][-1] == 'c':
                            requirements[0] = requirements[0].replace('c', '')
                            if requirements[0] not in self.to_take:
                                print(print('No cumple el co-requisito: {}'.format(requirements[0])))
                                return False

                    else:
                        for option in requirements:
                            if not isinstance(option, list):
                                option = [option]
                            if len(option) == 1:
                                if option[0][-1] == 'c':
                                    #print(option)
                                    option[0] = option[0].replace('c', '')
                                    #print(option)
                                    if option[0] in self.to_take:
                                        print('Cumple el co-requisisto: {}'.format(option))
                                        return True
                                if option[0] in self.app_class:
                                    print('Si cumple los requisitos')
                                    return True
                            else:
                                for _class in option:
                                    if _class[-1] == 'c':
                                        _class = _class.replace('c', '')
                                        if _class not in self.to_take:
                                            print('No cumple el co-requisito: {}'.format(_class))
                                            return False
                                    if _class not in self.app_class:
                                        print('No cumple el requisito: {}'.format(_class))
                                        return False
                        print('Si cumple los requisitos')
                        return True

    def make_schedule(self, _class):
        schedule = _class.schedule
        for kind,time in schedule.items():
            #print(kind)
            #print(time)
            if kind == 'hora_cat' and len(time) <= 1:
                cat_days = []
                ncat_block = []
            elif kind == 'hora_cat' and len(time) > 1:
                time = time.split(':')
                if len(time[0].split('-')) > 1:
                    cat_days = time[0].split('-')
                elif len(time[0].split('-')) == 1:
                    cat_days = time[0]
                if len(time[1].split(',')) > 1:
                    cat_block = time[1].split(',')
                    ncat_block = []
                    for block in cat_block:
                        ncat_block.append(int(block) - 1)
                elif len(time[1].split(',')) == 1:
                    ncat_block = [int(time[1]) - 1]
                #ncat_block = {kind: ncat_block}
            elif kind == 'hora_lab' and len(time) <= 1:
                lab_days = []
                nlab_block = []
            elif kind == 'hora_lab' and len(time) > 1:
                time = time.split(':')
                if len(time[0].split('-')) > 1:
                    lab_days = time[0].split('-')
                elif len(time[0].split('-')) == 1:
                    lab_days = time[0]
                if len(time[1].split(',')) > 1:
                    lab_block = time[1].split(',')
                    nlab_block = []
                    for block in lab_block:
                        nlab_block.append(int(block) - 1)
                elif len(time[1].split(',')) == 1:
                    nlab_block = [int(time[1]) - 1]
                #nlab_block = {kind: nlab_block}
            elif kind == 'hora_ayud' and len(time) <= 1:
                ayud_days = []
                nayud_block = []
            elif kind == 'hora_ayud' and len(time) > 1:
                time = time.split(':')
                if len(time[0].split('-')) > 1:
                    ayud_days = time[0].split('-')
                elif len(time[0].split('-')) == 1:
                    ayud_days = time[0]
                if len(time[1].split(',')) > 1:
                    ayud_block = time[1].split(',')
                    nayud_block = []
                    for block in ayud_block:
                        nayud_block.append(int(block) - 1)
                elif len(time[1].split(',')) == 1:
                    nayud_block = [int(time[1]) - 1]
                #nayud_block = {kind: nayud_block}
        ## cambie los dias y bloques a N°, para poder trabajar más facil en la matriz del horario
        ## probablemente exista una forma más elegante de hacerlo, pero me da flojera pensar más :/
        ncat_days = []
        for day in cat_days:
            if day == 'L':
                ncat_days.append(0)
            elif day == 'M':
                ncat_days.append(1)
            elif day == 'W':
                ncat_days.append(2)
            elif day == 'J':
                ncat_days.append(3)
            elif day == 'V':
                ncat_days.append(4)
        nlab_days = []
        for day in lab_days:
            if day == 'L':
                nlab_days.append(0)
            elif day == 'M':
                nlab_days.append(1)
            elif day == 'W':
                nlab_days.append(2)
            elif day == 'J':
                nlab_days.append(3)
            elif day == 'V':
                nlab_days.append(4)
        nayud_days = []
        for day in ayud_days:
            if day == 'L':
                nayud_days.append(0)
            elif day == 'M':
                nayud_days.append(1)
            elif day == 'W':
                nayud_days.append(2)
            elif day == 'J':
                nayud_days.append(3)
            elif day == 'V':
                nayud_days.append(4)
        #print(ncat_days, nlab_days, nayud_days)
        #print(ncat_block, nlab_block, nayud_block)
        return [ncat_days, nayud_days, nlab_days], [ncat_block, nayud_block, nlab_block]

    def check_schedule(self, _class):
        data = self.make_schedule(_class)
        for day in data[0][0]:
            for block in data[1][0]:
                if len(self.schedule[day][block]) != 0:
                    print('Tiene tope con la cátedra')
                    return False
        for day in data[0][1]:
            for block in data[1][1]:
                if len(self.schedule[day][block]) != 0:
                    print('Tiene tope con la ayudantia')
                    return False
        for day in data[0][2]:
            for block in data[1][2]:
                if len(self.schedule[day][block]) != 0:
                    print('Tiene tope con el lab')
                    return False
        #ndays = [ncat_days, nayud_days, nlab_days]
        #nblocks = [ncat_block, nayud_block, nlab_block]
        return True

    def check_vacancies(self, _class):
        if _class.av < 1:
            print('No quedan vacantes')
            return False
        else:
            _class.occ += 1
            _class.av -= 1
            return True

    def check_credits(self, credits):
        max_credits = 55 + ((6 - int(self.group)) * 2)
        if self.credits + credits > max_credits:
            print('Ya llegaste a tu máximo de créditos!!')
            return False
        else:
            return True

    def check_evaluations(self, _class):
        for evaluation in evaluations:
            if _class.initials == evaluation.initials:
                break
        evaluation = evaluation.date.split(' - ')
        day = evaluation[0]
        time = evaluation[1]
        #print(day, time)
        if time == 'NA':
            self.evaluations[day] = time
            return True
        if day in self.evaluations and time == self.evaluations[day]:
            return False
        else:
            self.evaluations[day] = time
            #print(self.evaluations)
            return True

    def check_campus(self, _class):
        data = self.make_schedule(_class)
        for day in data[0][0]:
            for block in data[1][0]:
                if len(self.schedule[day][block + 1]) != 0:
                    campus = self.schedule[day][block + 1].split(' ')
                    campus = campus[2]
                    if campus != _class.campus:
                        print('Tiene tope con la cátedra')
                        return False
                elif len(self.schedule[day][block - 1]) != 0:
                    campus = self.schedule[day][block - 1].split(' ')
                    campus = campus[2]
                    if campus != _class.campus:
                        print('Tiene tope con la cátedra')
                        return False
        for day in data[0][1]:
            for block in data[1][1]:
                if len(self.schedule[day][block + 1]) != 0:
                    campus = self.schedule[day][block + 1].split(' ')
                    campus = campus[2]
                    if campus != _class.campus:
                        print('Tiene tope con la ayudantia')
                        return False
                elif len(self.schedule[day][block - 1]) != 0:
                    campus = self.schedule[day][block - 1].split(' ')
                    campus = campus[2]
                    if campus != _class.campus:
                        print('Tiene tope con la ayudantia')
                        return False
        for day in data[0][2]:
            for block in data[1][2]:
                if len(self.schedule[day][block + 1]) != 0:
                    campus = self.schedule[day][block + 1].split(' ')
                    campus = campus[2]
                    if campus != _class.campus:
                        print('Tiene tope con el lab')
                        return False
                elif len(self.schedule[day][block - 1]) != 0:
                    campus = self.schedule[day][block - 1].split(' ')
                    campus = campus[2]
                    if campus != _class.campus:
                        print('Tiene tope con el lab')
                        return False
        #ndays = [ncat_days, nayud_days, nlab_days]
        #nblocks = [ncat_block, nayud_block, nlab_block]
        return True

    def take_class(self):
        while True:
            nrc = input('Ingrese el NRC de la clase que desea agregar al horario: ')
            count = 0
            for _class in schedules:
                if nrc == _class.nrc:
                    _class = schedules[count]
                    print('Intentando ingresar el nrc ' + _class.nrc)
                    break
                count += 1
            if count == len(schedules):
                print('El NRC ingresado no existe, porfavor ingrese otro')
            else:
                req = self.check_requirements(_class.initials)
                sch = self.check_schedule(_class)
                vac = self.check_vacancies(_class)
                cred = self.check_credits(_class.credits)
                ev = self.check_evaluations(_class)
                camp = self.check_campus(_class)
                print(req, sch, vac, cred, ev, camp)
                if _class in self.exceptions:
                    if req:
                        self.update_schedule(_class)
                        self.to_take.append(_class)
                        _class.accept_student(self)
                        print('Tienes inscritos los siguientes ramos:')
                        for _class in self.to_take:
                            print(_class.initials)
                        self.credits += _class.credits
                        print('Tienes {} créditos inscritos'.format(self.credits))
                elif req and sch and vac and cred and ev and camp:
                    self.update_schedule(_class)
                    self.to_take.append(_class)
                    _class.accept_student(self)
                    print('Tienes inscritos los siguientes ramos:')
                    for _class in self.to_take:
                        print(_class.initials)
                    self.credits += _class.credits
                    print('Tienes {} créditos inscritos'.format(self.credits))
                break

    def show_schedule(self):
        schedule = self.schedule
        for day in schedule:
            for block in day:
                print(block)

    def delete_class(self):
        while True:
            for i in self.to_take:
                print(i.nrc, i.initials)
            print('Escribe "salir" para salir.')
            nrc = input('Que clase deseas botar? ')
            if nrc == 'salir':
                return
            count = 0
            for _class in self.to_take:
                if nrc == _class.nrc:
                    _class = self.to_take[count]
                    break
                count += 1
            if count == len(self.to_take):
                print('El nrc ingresado, no se encuentra entre tus ramos')
            else:
                #print(self.to_take)
                #print(_class)
                self.to_take.remove(_class)
                ## data=[[ncat_days, nayud_days, nlab_days], [ncat_block, nayud_block, nlab_block]
                data = self.make_schedule(_class)
                for day in data[0][0]:
                    for block in data[1][0]:
                        self.schedule[day][block] = []
                for day in data[0][1]:
                    for block in data[1][1]:
                        self.schedule[day][block] = []
                for day in data[0][2]:
                    for block in data[1][2]:
                        self.schedule[day][block] = []
                _class.student_drop(self)
                print('Haz borrado el curso: {}'.format(_class.initials))

    def __repr__(self):
        return 'Alumno {}, bacanosidad: {}'.format(self.name, self.coolness)


class Professor(Person):
    professors = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logged = False

    def log_in(self):
        self.logged = True
        Professor_menu(self).run()
        return True

    def give_permission(self):
        while True:
            print('"Salir" para salir')
            nrc = input('Ingrese el nrc de uno de sus cursos ')
            if nrc == 'salir':
                break
            count = 0
            for _class in schedules:
                if nrc == _class.nrc:
                    if self.name in _class.new_professors:
                        break
                    else:
                        print('Usted no imparte el curso: {} de {}'.format(_class.nrc, _class.name))
                count += 1
            if count == len(schedules):
                print('El nrc ingresado no existe')
            else:
                break
        while True:
            print('"Salir" para salir')
            name = input('Ingrese nombre del alumno al que desea permitirle cursar el ramo ')
            if name == 'salir':
                break
            count = 0
            for student in Student.students:
                if name == student.name:
                    break
                count += 1
            if count == len(Student.students):
                print('No se pudo encontrar al alumno {}'.format(name))
            else:
                break
        student.exceptions.append(_class)
        print('Al estudiante {}, se le ha permitido ingresar el curso {}'.format(student.name, _class.initials))

    def __repr__(self):
        return 'Profesor: {}'.format(self.name)



##Procesar .txt
def create_personas():
    students_list = []
    professors_list = []
    with open('personas.txt', 'r') as text:
        text = text.read()\
            .replace('  ', '').replace('{', '')\
            .replace('"', '').replace(',', '')\
            .split('}')
        text.pop(-1) ## hay que sacar el ultimo valor, porque no es una persona.
        for data in text:
            data = data.split('\n')
            data.pop(0) ##para corregir vacios en la lista
            data.pop(0) ##para corregir vacios en la lista
            for line in data:
                line = line.split(': ')
                if len(line) > 1 and line[0] != 'idolos' and line[0] != 'ramos_pre':
                    if line[0] == 'nombre':
                        name = line[1]
                    elif line[0] == 'clave':
                        password = line[1]
                    elif line[0] == 'alumno' and line[1] == 'SI':
                        student = 'si'
                    elif line[0] == 'alumno' and line[1] == 'NO':
                        student = 'no'
                    elif line[0] == 'usuario':
                        usser = line[1]
                elif len(line) > 1 and line[0] == 'idolos' and line[0] != ']' and line[0] != '':
                    turn = 'idols_turn'
                    idols = []
                elif len(line) > 1 and line[0] == 'ramos_pre' and line[0] != ']' and line[0] != '':
                    turn = 'app_class_turn'
                    app_class = []
                else:
                    if turn == 'idols_turn':
                        idols.append(line[0])
                    elif turn == 'app_class_turn':
                        app_class.append(line[0])
            if student == 'si':
                Student.students.append(Student(password=password, name=name, usser=usser, idols=idols[0:-1], app_class=app_class[0:-2]))
            else:
                Professor.professors.append(Professor(password=password, name=name, usser=usser, idols=None, app_class=None))
            #print(name, password, student, usser)
            #idols_list.pop(0)
            #idols_final = data[0].index(']')

    return Student.students, Professor.professors

def create_txt_coolness(list):
    for student in list:
        for others in list:
            if student.name in others.idols:
                student.coolness += 1
    list = sorted(list, key=lambda student: student.coolness, reverse=True) ##espero que no tengan problemas con que usara lambda,
                                                                            ## no creo que vaya encontra de lo que intentan evaluar
                                                                            ## en esta tarea, es una optimización de hecho.
    highest_coolness = list[0].coolness
    for student in list:
        student.coolness = round(student.coolness/highest_coolness, 3)
    with open('bacanosidad.txt', 'w', encoding='utf8') as text:
        for student in list:
            text.write(student.name + '    ' + str(student.coolness) + '\n')
    return list
a = create_personas()
old = create_txt_coolness(a[0]) ## archivo bacanosidad.txt
def new_cool():
    with open('bacanosidad.txt', 'r', encoding='utf8') as text:
        coolness_dict = {}
        for line in text:
            line = line.split('    ')
            coolness_dict[line[0]] = line[1].replace('\n', '')
        return coolness_dict

##original = new_cool()

def add_coolness(old_list, original_coolness):
    with open('bacanosidad_final.txt', 'w', encoding='utf8') as text:
        for student in old_list:
            for cool_guy in student.idols:
                for others in old_list:
                    if cool_guy == others.name:
                        others.coolness += round(float(original_coolness[student.name])/len(student.idols), 3)
        old_list = sorted(old_list, key=lambda student: student.coolness, reverse=True)
        for student in old_list:
            text.write(student.name + '  ' + str(round(student.coolness, 3)) + '  ' + original_coolness[student.name] + '\n')
##a = add_coolness(old, cool)

def update_coolness(list):
    with open('bacanosidad_final.txt', 'r', encoding='utf8') as text:
        coolness_dict = {}
        for line in text:
            line = line.replace('\n', '').split('  ')
            coolness_dict[line[0]] = line[1]
        for student in list:
            student.coolness = coolness_dict[student.name]
        list = sorted(list, key=lambda student: student.coolness, reverse=True) ##el orden final variará un poco,
                                                                                ## el punto flotante
                                                                                ##hace que el total sea un poco distinto.
        return list

updated = update_coolness(old)

def assign_groups(list):
    count = 1
    group = 1
    for student in list:
        if count % 435 != 0:
            student.group = str(group)
            count += 1
        else:
            count = 1
            group += 1
            student.group = str(group)
    return list

groups = assign_groups(updated)
#for student in groups:
    #print(student.name, student.group, student.set_time(), student.time_start, student.time_end)



