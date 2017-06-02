__author__ = 'aldo_martini'

class Classes:
    def __init__(self, total, eng, apr, name, initials, credits, section, campus, ret, nrc):
        self.total = total
        self.avaliable = total
        self.occupied = 0
        self.eng = eng
        self.apr = apr
        self.name = name
        self.initials = initials
        self.credits = credits
        self.section = section
        self.campus = campus
        self.ret = ret
        self.nrc = nrc

    def __repr__(self):
        return 'La clase de "{}" ha sido creada.'.format(self.name)

def create_classes():
    classes_list = []

    with open('cursos.txt', 'r', encoding='utf8') as text:
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
                line = line.split(': ')
                if line[0] == 'ofr':
                    total = line[1]
                elif line[0] == 'eng':
                    eng = line[1]
                elif line[0] == 'apr':
                    apr = line[1]
                elif line[0] == 'curso':
                    name = line[1]
                elif line[0] == 'sigla':
                    initials = line[1]
                elif line[0] == 'cred':
                    credits = line[1]
                elif line[0] == 'sec':
                    section = line[1]
                elif line[0] == 'campus':
                    campus = line[1]
                elif line[0] == 'retiro':
                    ret = line[1]
                elif line[0] == 'NRC':
                    nrc = line[1]
            classes_list.append(Classes(total, eng, apr, name, initials, credits, section, campus, ret, nrc))
    return classes_list