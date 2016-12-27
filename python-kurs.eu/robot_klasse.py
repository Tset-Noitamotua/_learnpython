class Roboter:
    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr

    def __repr__(self):
        return "Roboter(\"" + self.name + "\"," + str(self.baujahr) + ")"

    def SageHallo(self):
        print('Hallo, mein Name ist ' + self.name)

    def NeuerName(self, name):
        self.name = name

    def NeuesBaujahr(self, baujahr):
        self.baujahr = baujahr

    def HoleNamen(self):
        return self.name

    def HoleBaujahr(self):
        return str(self.baujahr)

if __name__ == '__main__':
    x = Roboter('Marvin', 1979)

    x_str = str(x)
    print(x_str)
    print("Typ von x_str: ", type(x_str))
    neu = eval(x_str)
    print("Typ von neu: ", type(neu))
