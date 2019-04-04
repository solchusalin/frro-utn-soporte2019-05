import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        format = "%d/%m/%Y %H:%M:%S"
        self.nacimiento=datetime.datetime.strptime(nacimiento, format)

    def edad(self):
        edad = (datetime.datetime.now() - self.nacimiento).days
        return int(edad / 365)

p = Persona("19/02/1997 14:13:00")
assert (p.edad() == 22)


