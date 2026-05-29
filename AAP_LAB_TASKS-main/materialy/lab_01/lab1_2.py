# TODO: Implementacja deskryptora Typed
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Wartość pola '{self.name}' musi być typu {self.expected_type.__name__}, otrzymano: {type(value).__name__}")
        
        instance.__dict__[self.name] = value

class Osoba:
    imie = Typed(str)
    wiek = Typed(int)
    
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

#Testowe funkcje
#Sukces
jakub = Osoba("Jakub", 50)
print(f"Utworzono: {jakub.imie}, Wiek: {jakub.wiek}")

#Error
bledna_osoba = Osoba(123, 25) 

#Error
jakub.wiek = "pięćdziesiąt"