__author__ = 'aldo_martini'

rooms_list = []

class Room:
    def __init__(self, length='', width='', max_p=''):
        self._heigth = 2
        self._length = length
        self._width = width
        self._max_p = max_p
        self._p_inside = 0

    @property
    def area(self):
        return self._length * self._width

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __add__(self, other):
        print('No se pueden unir estos espacios')


class Room_seats(Room):
    def __init__(self, seats= '', **kwargs):
        super().__init__(**kwargs)
        self._seats = seats
        self.av_seats = seats

    def __add__(self, other):
        if not (type(self) is type(other)):
            print('Imposible unir los espacios')
            return

        new_length = self._length + other._length
        new_width = self._width + other._width
        new_max_p = self._max_p + other._max_p
        new_seats = self._seats + other._seats
        return Room_seats(seats=new_seats, length=new_length, width=new_width, max_p=new_max_p)

    def __lt__(self, other):
        if isinstance(other, Room_seats):
            return self._seats < other._seats
        return self.area < other.area

    def __gt__(self, other):
        if isinstance(other, Room_seats):
            return self._seats > other._seats
        return self.area > other.area

    def __repr__(self):
        return 'Asientos: {}, Largo: {}, Ancho: {}, Personas: {}'.format(self._seats, self._length, self._width, self._max_p)

class Underground(Room):
    def __init__(self, **kwargs):
        print('Subterraneo creado')
        super().__init__(**kwargs)

class Classroom(Room_seats):
    def __init__(self, **kwargs):
        print("Sala de clases creada")
        super().__init__(**kwargs)


class Meeting_room(Room_seats):
    def __init__(self, **kwargs):
        print("Sala de reuniones creada")
        super().__init__(**kwargs)


class Person:
    def __init__(self, name):
        self.name = name

    def enter_room(self, room):
        print('{} entra a la sala: {}/{}, {}/{}'.format(self.name,
                                                        room.av_seats,
                                                        room._seats,
                                                        room._p_inside,
                                                        room._max_p))


class Student(Person):
    def enter_room(self, room):
        if room._p_inside < room._max_p:
            if isinstance(room, Room_seats) and room.av_seats > 0:
                room.av_seats -= 1
                room._p_inside += 1
                super().enter_room(room)
                print('{} entra a la sala.'.format(self.name))
            elif not isinstance(room, Room_seats):
                room._p_inside += 1
                print('{} entra al subterraneo.'.format(self.name))
            else:
                print('{} no ha podido entrar.'.format(self.name))


class Professor(Person):
    def enter_room(self, room):
        if room._p_inside < room._max_p:
            if isinstance (room, Meeting_room) and room.av_seats > 0:
                room.av_seats -= 1
            room._p_inside += 1
            super().enter_room(room)
        else:
            pass
        print('{} no ha podido entrar.'.format(self.name))


rooms_list.append(Classroom(width=5, length=20, max_p=25, seats=6))
rooms_list.append(Classroom(width=3, length=10, max_p=10, seats=6))
rooms_list.append(Meeting_room(width=10, length=15, max_p=30, seats=10))
rooms_list.append(Underground(width=20, length=20, max_p=40))
print(rooms_list[0] == rooms_list[1])
print(rooms_list[0] > rooms_list[2])
print(rooms_list[0] > rooms_list[3])
print(rooms_list[0] < rooms_list[3])
print(rooms_list[3] > rooms_list[0])
rooms_list.append(rooms_list[0] + rooms_list[1])
rooms_list.append(rooms_list[0] + rooms_list[2])
rooms_list.append(rooms_list[2] + rooms_list[2])
rooms_list.append(rooms_list[3] + rooms_list[3])
print(rooms_list)

personas = []
personas.append(Student("Belen"))
personas.append(Student("Patricio"))
personas.append(Student("Jaime"))
personas.append(Student("Marco"))
personas.append(Student("Rodrigo"))
personas.append(Professor("Karim"))
personas.append(Professor("Christian"))
personas.append(Professor("Extra"))
for p in personas:
    p.enter_room(rooms_list[1])


