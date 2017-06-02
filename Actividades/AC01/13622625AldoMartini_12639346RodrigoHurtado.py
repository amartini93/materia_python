class Universe:
    def __init__(self):
        self.fields_list = []

    def add_field(self, field):
        self.fields_list.append(field)

class Field:
    def __init__(self, RA_max, RA_min, DEC_max, DEC_min):
        self.ra_max = RA_max
        self.ra_min = RA_min
        self.dec_max = DEC_max
        self.dec_min = DEC_min
        self.stars = []

    def add_star(self, star):
        self.stars.append(star)

class Star:
    def __init__(self, RA, DEC, s_id, s_type):
        self.ra = RA
        self.dec = DEC
        self.id = s_id
        self.type = s_type
        self.observations = []

    def add_observation(self, time, bright, error):
        lista = [time, bright, error]
        self.observations.append(lista)

AA21 = Star(21, 16, 104, 'Binaries')
AA21.add_observation('01/02/21015_10:47', 15, 1)
AA21.add_observation('02/02/21015_10:47', 16, 2)
AA21.add_observation('03/02/21015_10:47', 14, 3)
AA21.add_observation('04/02/21015_10:47', 15, 1)

AA22 = Star(30, 17, 105, 'Binaries')
AA22.add_observation('01/01/21015_10:47', 15, 1)
AA22.add_observation('02/01/21015_10:47', 16, 2)
AA22.add_observation('03/01/21015_10:47', 14, 3)
AA22.add_observation('04/01/21015_10:47', 15, 1)

AA23 = Star(29, 18, 106, 'Mira')
AA23.add_observation('01/01/21015_11:47', 15, 1)
AA23.add_observation('02/01/21015_11:47', 16, 2)
AA23.add_observation('03/01/21015_11:47', 14, 3)
AA23.add_observation('04/01/21015_11:47', 15, 1)

BB21 = Star(35, 21, 107, 'Mira')
BB21.add_observation('01/01/21015_21:47', 15, 1)
BB21.add_observation('02/01/21015_21:47', 16, 2)
BB21.add_observation('03/01/21015_21:47', 14, 3)
BB21.add_observation('04/01/21015_21:47', 15, 1)

BB22 = Star(34, 20, 108, 'Cepheids')
BB22.add_observation('01/01/21015_22:47', 15, 1)
BB22.add_observation('02/01/21015_22:47', 16, 2)
BB22.add_observation('03/01/21015_22:47', 14, 3)
BB22.add_observation('04/01/21015_22:47', 15, 1)

BB23 = Star(33, 19, 109, 'Cepheids')
BB23.add_observation('01/01/21015_23:47', 15, 1)
BB23.add_observation('02/01/21015_23:47', 16, 2)
BB23.add_observation('03/01/21015_23:47', 14, 3)
BB23.add_observation('04/01/21015_23:47', 15, 1)

ASP = Field(31, 24, 22, 14)
ASP.add_star(AA21)
ASP.add_star(AA22)
ASP.add_star(AA23)

ASD = Field(40, 32, 30, 15)
ASD.add_star(BB21)
ASD.add_star(BB22)
ASD.add_star(BB23)

universo = Universe()
universo.add_field(ASD)
universo.add_field(ASP)

print(AA21.observations)
print(ASP.stars)
print(universo.fields_list)
for i in ASP.stars:
    print(i.observations)
for i in ASD.stars:
    print(i.observations)