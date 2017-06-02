__author__ = 'aldo_martini'


class Requirement:
    def __init__(self, initials, equivalties, requirements):
        self.initials = initials
        self.equivalties = equivalties
        self.requirements = requirements

    def __repr__(self):
        return 'Requerimientos ingresados para {}.'.format(self.initials)


def create_requirements():
    requirements_list = []

    with open('requisitos.txt', 'r') as text:
        text = text.read()\
            .replace('  ', '').replace('{', '')\
            .replace('"', '').replace(',', '')\
            .replace('(', '').replace(')', '')\
            .split('}')
        text.pop(-1) ## hay que sacar el ultimo valor, porque no es una persona.
        for data in text:
            data = data.split('\n')
            data.pop(0) ##para corregir vacios en la lista
            data.pop(0) ##para corregir vacios en la lista
            for line in data:
                line = line.split(': ')
                if len(line) > 1:
                    if line[0] == 'equiv':
                        equivalties = line[1]
                    elif line[0] == 'sigla':
                        initials = line[1]
                    elif line[0] == 'prerreq':
                        requirements = line[1]
                        posibilities = []
                        if len(requirements.split(' o ')) == 1:
                            if len(requirements.split(' y ')) == 1:
                                posibilities.append([requirements])
                            else:
                                requirements = requirements.split(' y ')
                                posibilities.append([requirements])
                        else:
                            classes = []
                            requirements = requirements.split(' o ')
                            for posibility in requirements:
                                if len(posibility.split(' y ')) == 1:
                                    classes.append(posibility)
                                else:
                                    posibility = posibility.split(' y ')
                                    classes.append(posibility)
                            posibilities.append(classes)

            requirements_list.append(Requirement(initials, equivalties, posibilities))
    return requirements_list
