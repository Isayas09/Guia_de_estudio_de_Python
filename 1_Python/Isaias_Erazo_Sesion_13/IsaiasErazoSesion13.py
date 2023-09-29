# instanciando la clase 'car' y creando un objeto de el
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


carro = Car("tollotta", "korrola", "2023")
print(f"descripcion del carro: {carro.brand}, {carro.model}, {carro.year}")


class Student:
    def __init__(
        self,
        name,
        age,
    ):
        self.name = name
        self.age = age
        self.grades = []

    def __str__(self):
        return f"{self.name}, {self.age}"

    def add_grade(self, grade):
        self.grades.append(grade)

    def print_info(self):
        print(f"Estudiante:{self.name}, Edad:{self.age}, Calificaciones:{self.grades}")


# Instanciando la clase
estudiante = Student("luigi", 23)

estudiante.add_grade(10)
estudiante.add_grade(6)
estudiante.add_grade(7)
estudiante.add_grade(9)
estudiante.add_grade(8)

estudiante.print_info()
print("\n")
# ----------------------------------------------------------------
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


circulo = Circle(3)
print(f"El perimetro es: {circulo.calculate_perimeter()}")
print(f"El perimetro es: {circulo.calculate_area()}")
print("\n")


# ---------------------------------------------------------
class Bank:
    def __init__(self):
        self.accounts = {}

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
        else:
            self.accounts[account_number] = amount

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
            else:
                print("Fondos insuficientes")
        else:
            print("Cuneta invalida o  no encontrada")

    def get_balance(self, account_number):
        return self.accounts.get(account_number, 0)


banco = Bank()
banco.get_balance("C1234")

banco.deposit("C0007", 200)
banco.get_balance("C007")

banco.deposit("C006", 500)
print(banco.get_balance("C006"))

print("\n")


# ----------------------------------------
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class OnlineStore:
    def __init__(self):
        self.inventory = {}
        self.total_sales = 0

    def add_product(self, product, amount):
        if product in self.inventory:
            self.inventory[Producto] += amount
        else:
            self.inventory[Producto] = amount

    def purchase(self, carrito, porcentaje_impuesto=0):
        total_sin_impuesto = self.calcular_total(carrito)
        total_con_impuesto = total_sin_impuesto * (1 + porcentaje_impuesto / 100)

    def show_sales(self, carrito):
        total = 0
        for product, amount in carrito.items():
            total += product.precio * amount
            return total

    def descuento(self, product, porcentaje_descuento):
        if product in self.inventory:
            precio_original = product.precio
            precio_descuento = precio_original * (1 - porcentaje_descuento / 100)
            product.precio = precio_descuento
