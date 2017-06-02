__author__ = 'aldo_martini'

from requirements_loader import create_requirements

class Schedule:
    requirements = create_requirements()
    def __init__(self, nrc, name, initials, campus, avaliable, occupied, credits, professors, schedule):
        self.nrc = nrc
        self.name = name
        self.initials = initials
        self.campus = campus
        self.av = avaliable
        self.occ = occupied
        self.credits = credits
        self.professors = professors
        self.schedule = schedule
        self.students_list = []
        self.new_professors = []

        for professor in self.professors:
            if len(professor.split(' ')) == 2:
                name = professor.replace(',', '').split(' ')
                first_name = name[1]
                last_name = name[0]
                self.new_professors.append(first_name + ' ' + last_name)
            else:
                name = professor.split(' ')
                first_name = name[-1]
                last_name = ''
                for chunk in name[0:-1]:
                    last_name += chunk + ' '
                last_name = last_name.rstrip(' ')
                self.new_professors.append(first_name + ' ' + last_name)

    def accept_student(self, student):
        self.students_list.append(student)
        self.av -= 1
        self.occ += 1
        print(self.students_list)

    def student_drop(self, student):
        self.students_list.remove(student)
        self.av += 1
        self.occ -= 1
        print(self.students_list)

    def __repr__(self):
        return 'Horario para {} creado.'.format(self.nrc)


def create_schedules():
    schedule_list = []

    with open('cursos.txt', 'r', encoding='utf8') as text:
        text = text.read()\
            .replace('  ', '').replace('{', '')\
            .replace('"', '').replace('[', '')\
            .replace(']', '').split('}')
        text.pop(-1) ## hay que sacar el ultimo valor, porque no es una persona.
        for data in text:
            data = data.split('\n')
            data.pop(0) ##para corregir vacios en la lista
            data.pop(0) ##para corregir vacios en la lista
            name = None
            professors = []
            schedule = {}
            hora_cat = ''
            sala_cat = ''
            hora_ayud = ''
            sala_ayud = ''
            hora_lab = ''
            sala_lab = ''
            for line in data:
                line = line.split(': ')
                if len(line) == 1:
                    if len(line[0]) > 0:
                        professors.append(line[0])
                elif line[0] == 'profesor' and line[1] != '':
                    professors.append(line[1])
                elif line[0] == 'hora_cat':
                    hora_cat = line[1]
                    hora_cat = hora_cat.rstrip(',')
                elif line[0] == 'sala_cat':
                    sala_cat = line[1]
                    sala_cat = sala_cat.replace(',', '')
                elif line[0] == 'hora_ayud':
                    hora_ayud = line[1]
                    hora_ayud = hora_ayud.rstrip(',')
                elif line[0] == 'sala_ayud':
                    sala_ayud = line[1]
                    sala_ayud = sala_ayud.replace(',', '')
                elif line[0] == 'hora_lab':
                    hora_lab = line[1]
                    hora_lab = hora_lab.rstrip(',')
                elif line[0] == 'sala_lab':
                    sala_lab = line[1]
                    sala_lab = sala_lab.replace(',', '')
                elif line[0] == 'NRC':
                    nrc = line[1]
                    nrc = nrc.replace(',', '')
                elif line[0] == 'curso':
                    name = line[1]
                    name = name.replace(',', '')
                elif line[0] == 'sigla':
                    initials = line[1]
                    initials = initials.replace(',', '')
                elif line[0] == 'campus':
                    campus = line[1]
                    campus = campus.replace(',', '')
                elif line[0] == 'ofr':
                    avaliable = line[1]
                    avaliable = avaliable.replace(',', '')
                    avaliable = int(avaliable)
                elif line[0] == 'ocu':
                    occupied = line[1]
                    occupied = occupied.replace(',', '')
                    occupied = int(occupied)
                elif line[0] == 'cred':
                    credits = line[1]
                    credits = credits.replace(',', '')
                    credits = int(credits)
                else:
                    professors = []

            schedule['hora_cat'] = hora_cat
            schedule['sala_cat'] = sala_cat
            schedule['hora_ayud'] = hora_ayud
            schedule['sala_ayud'] = sala_ayud
            schedule['hora_lab'] = hora_lab
            schedule['sala_lab'] = sala_lab
            schedule_list.append(Schedule(nrc, name, initials, campus, avaliable, occupied, credits, professors, schedule))
            #values.append(professors)
            #values.append(schedule)
            #schedule_dict[nrc] = values
    return schedule_list