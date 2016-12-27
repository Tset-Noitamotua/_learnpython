class Person:
    

    def __init__(self, vorname, nachname, geburtsdatum):
        self._vorname = vorname
        self._nachname = nachname
        self._geburtsdatum = geburtsdatum
        
    def __str__(self):

        ret = self._vorname + " " + self._nachname
        ret += ", " + self._geburtsdatum
        return  ret
        
class Angestellter(Person):
    

    def __init__(self, vorname, nachname, geburtsdatum, personalnummer):
        Person.__init__(self, vorname, nachname, geburtsdatum)
        # alternativ:
        #super().__init__(vorname, nachname, geburtsdatum)
        self.__personalnummer = personalnummer
        
    
    
if __name__ == "__main__":
    x = Angestellter("Homer", "Simpson", "09.08.1969", "007")
    print(x)
