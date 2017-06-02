__author__ = 'aldo_martini'

class Evaluation:
    def __init__(self, initials, kind, section, date):
        self.initials = initials
        self.kind = kind
        self.section = section
        self.date = date

    def __repr__(self):
        return '{} del ramo {} ha sido fijada.'.format(self.kind, self.initials)


def set_evaluations():
    evaluations_list = []

    with open('evaluaciones.txt', 'r', encoding='utf8') as text:
        text = text.read()\
            .replace('  ', '').replace('{', '')\
            .replace('"', '').replace('[', '')\
            .replace(']', '').replace(',', '')\
            .split('}')
        text.pop(-1) ## hay que sacar el ultimo valor, porque no es una persona.
        for data in text:
            data = data.split('\n')
            data.pop(0) ##para corregir vacios en la lista
            data.pop(0) ##para corregir vacios en la lista
            for line in data:
                if len(line.split(': ')) != 1:
                    line = line.split(': ')
                    if line[0] == 'sigla':
                        initials = line[1]
                    elif line[0] == 'tipo':
                        kind = line[1]
                    elif line[0] == 'sec':
                        section = line[1]
                    elif line[0] == 'fecha':
                        date = line[1]
            evaluations_list.append(Evaluation(initials, kind, section, date))
    return evaluations_list