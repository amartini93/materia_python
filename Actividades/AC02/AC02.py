__author__ = 'aldo_martini'

class Headphones:
    def __init__(self, f_max='', f_min='', res='', rep='', **kwargs):
        self.f_max = f_max
        self.f_min = f_min
        self.res = res
        self.rep = rep

    def listen(self, song):
        print('La cancion {}, esta siendo escuchada desde un audifono.'.format(song))


class Over_ear(Headphones):
    def __init__(self, aislation='', **kwargs):
        super().__init__(**kwargs)
        self.aislation = aislation


class Intraurales(Headphones):
    def __init__(self, discomfort='', **kwargs):
        super().__init__(**kwargs)
        self.discomfort = discomfort


class Inalambric(Headphones):
    def __init__(self, m_range='', **kwargs):
        super().__init__(**kwargs)
        self.m_range = m_range
        self.listening = False

    def listen(self, song):
        if self.listening == True:
            print('La cancion {}, esta siendo escuchada desde un audifono inalambrico.'.format(song))

    ##revisa si el audifono esta en rango para escuchar##
    def connect(self, r_range):
        self.listening = False
        if self.m_range < r_range:
            print('No se puede conectar. Acerquese al reproductor')
        else:
            self.listening = True

class Bluetooth(Inalambric):
    def __init__(self, origin='', **kwargs):
        super().__init__(**kwargs)
        self.origin = origin
        self.listening = False

    def listen(self, song):
        print('La cancion {}, esta siendo escuchada desde un audifono con Bluetooth.'.format(song))

    ##revisa si el audifono esta en rango para escuchar##
    def connect(self, r_range):
        self.listening = False
        if self.m_range < r_range:
            print('No se puede conectar. Acerquese al reproductor')
        else:
            self.listening = True


bluetooth1 = Bluetooth(origin='samsung galaxyII', m_range=10, f_max=20, f_min=10, res=5, rep=2)
bluetooth1.connect(20)
bluetooth1.listen('Snow')
bluetooth2 = Bluetooth(origin='samsung galaxyII', m_range=10, f_max=20, f_min=10, res=5, rep=2)
bluetooth2.connect(5)
bluetooth2.listen('Monarchy of Roses')
inalambrico1 = Inalambric(m_range=20, f_max=20, f_min=10, res=5, rep=2)
inalambrico1.connect(30)
inalambrico2 = Inalambric(m_range=30, f_max=20, f_min=10, res=5, rep=2)
inalambrico2.connect(30)
inalambrico1.listen('Wet Sand')
inalambrico2.listen('Wet Sand')
inalambrico2.connect(40)
inalambrico2.listen("Can't Stop")
inalambrico2.connect(20)
inalambrico2.listen("Can't Stop")
headphones1 = Headphones(f_max=20, f_min=10, res=5, rep=2)
headphones1.listen('Dosed')


