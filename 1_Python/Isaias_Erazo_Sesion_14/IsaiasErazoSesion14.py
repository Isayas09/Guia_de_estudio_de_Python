# Clase principal
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)


persona_1 = Person("john", "snow")
persona_1.print_name()


# Clase Secundaria
class Student(Person):  # Herencia de metodos y atributos de "Classs person"
    pass


student_1 = Student("Albert", "Einstein")
student_1.print_name()


# Agregar funcion. __init__
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Funcion "Super()"
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        pass


# Agregar Propiedades a la clase Heredada
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


student_1 = Student("Mike", "Tyson", 2009)
print(student_1.print_name())


# Agregar Metodo
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Bienvenido", self.fname, self.lname, "a la clase del", self.graduationyear
        )


student_1 = Student("Mike", "Tyson", 2009)
student_1.welcome()


# Ejemplo
class Animal:
    def __init__(self, name, nfeet, raza):
        self.name = name
        self.nfeet = nfeet
        self.raza = raza


class Cat(Animal):
    def __init__(self, name, nfeet, raza):
        super().__init__(name, nfeet, raza)


gatito = Cat("Jaco", 4, "Angora")
print("El nombre del gato es: ", gatito.name)
print("El numero de patas del gato es: ", gatito.nfeet)
print("La raza del gato es: ", gatito.raza)
print("\n")


class Dog(Animal):
    def __init__(self, name, nfeet, raza, year):
        super().__init__(name, nfeet, raza)
        self.year = year


perrito = Dog("Doki", 4, "Labrador", 12)
print("El nombre del perro es: ", perrito.name)
print("El numero de patas del perro es: ", perrito.nfeet)
print("La raza del perro es: ", perrito.raza)
print("Los year del perro son: ", perrito.year)
print("\n")

# Polimorfismo

x = "Hello, World"
print("x tiene: ", len(x))

mytuple = ("cat", "dog", "fish", "horse")
print("mytuple tiene: ", len(mytuple))

mydict = {"nombre": "Jonh", "Apellido": "Doe"}
print("mydict tiene: ", len(mydict))
print("\n")

# Polimorfismo para Clases


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("a conducir")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("a Navegar")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("a Volar")


carro_1 = Car("Tojota", "Gorrola")
bote_1 = Boat("Bavarita", "Yachts")
avion_1 = Plane("Boeing", "AirBus")

for it in (carro_1, bote_1, avion_1):
    it.move()
print("\n")
