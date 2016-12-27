class A():

    # Klassenattribute werden ausserhalb von Methoden-
    # definitionen formuliert
    counter = 0
    
    def __init__(self):
        self.__priv = 'Ich bin privat'
        self._prot = 'Ich bin protected'
        self.pub = 'Ich bin public'
        # Jede Instanziierung der Klasse erhoeht den
        # counter um einz
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1
        del(self)

    @staticmethod
    def Anzahl_Instanzen():
        return A.counter

if __name__ == '__main__':
    print(A.Anzahl_Instanzen())
    x = A()
    print(A.Anzahl_Instanzen())
    print(x.Anzahl_Instanzen())


