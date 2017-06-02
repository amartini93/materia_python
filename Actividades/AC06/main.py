__author__ = 'aldo_martini'

class Reporte:
    id = 0
    yellow = []
    blue = []
    orange = []
    red = []
    green = []
    def __init__(self, year, month, day, color, time, cause):
        self.year = year
        self.month = month
        self.day = day
        self.color = color
        self.time = time
        self.cause = cause
        self.id = Reporte.id + 1
        Reporte.id = self.id

    def get_color_list(self):
        color = input('Que color desea buscar? ')
        if color == 'amarillo':
            for patient in Reporte.yellow:
                print(patient)
        elif color == 'azul':
            for patient in Reporte.blue:
                print(patient)
        elif color == 'naranja':
            for patient in Reporte.orange:
                print(patient)
        elif color == 'rojo':
            for patient in Reporte.red:
                print(patient)
        elif color == 'verde':
            for patient in Reporte.green:
                print(patient)

    def __repr__(self):
        return 'Id: {}, año: {}, mes: {}, día: {}, color: {}, hora: {}, motivo de alta: {}'.format(self.id, self.year,
                                                                                                   self.month, self.day,
                                                                                                   self.color, self.time,
                                                                                                   self.cause)




with open('Reporte.txt', 'r', encoding='utf8') as text:
    text = text.read().split('\n')
    patients_list = []
    count = 1
    for patient in text:
        patient = patient.split('\t')
        patient = (Reporte(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))
        if patient.color == 'amarillo' and patient.year == '2013' and len(Reporte.yellow) != 10:
            Reporte.yellow.append(patient)
            patients_list.append(patient)
            count += 1
        elif patient.color == 'azul' and patient.year == '2013' and len(Reporte.blue) != 10:
            Reporte.blue.append(patient)
            patients_list.append(patient)
            count += 1
        elif patient.color == 'naranja' and patient.year == '2013' and len(Reporte.orange) != 10:
            Reporte.orange.append(patient)
            patients_list.append(patient)
            count += 1
        elif patient.color == 'rojo' and patient.year == '2013' and len(Reporte.red) != 10:
            Reporte.red.append(patient)
            patients_list.append(patient)
            count += 1
        elif patient.color == 'verde' and patient.year == '2013' and len(Reporte.green) != 10:
            Reporte.green.append(patient)
            patients_list.append(patient)
            count += 1
        else:
            count += 1
        if len(patients_list) == 50:
            print('Se han leído {} lineas'.format(count))
            break
for patient in patients_list:
    print(patient.id)
    print(patient.color)

patients_list[0].get_color_list()