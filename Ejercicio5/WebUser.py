
# Definición de la clase UserState y OrderStatus como tipo Enum

from enum import Enum

class UserState(Enum):
    New = "New"
    Active = "Active"
    Blocked = "Blocked"
    Banned = "Banned"

class OrderStatus(Enum):
    New = "New"
    Hold = "Hold"
    Shipped = "Shipped"
    Delivered = "Delivered"
    Closed = "Closed"

# Definimos WebUser, Customer, Account, ShoopingCart, LineItem, Product, Order, Payment

class WebUser:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self,login_id: str, password: str, state: UserState):
        self.login_id = login_id
        self.password = password
        self.state = state
        self.shopping_cart = None # Puede existir un WebUser sin tener aun un carrito creado.

    #Para printear el objeto
    def __str__(self):
        return f"WebUser(login={self.login_id},state={self.state.value}, carroo={self.shopping_cart})"

class Customer:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self,id: str, address: str, phone: str, email: str):
        self.id = id
        self.address = address
        self.phone = phone
        self.email = email
        self.account = None 

class Account:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self,id: str, billing_address: str, is_closed: bool, open: str, closed: str):
        self.id = id
        self.billing_address = billing_address
        self.is_closed = is_closed
        self.open = open
        self.closed = closed
        self.orders = []

class Product:
#Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self, id: str, name: str, supplier: str):
        self.id = id
        self.name = name
        self.supplier = supplier

class LineItem:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self, quantity: int, price: float, product: Product):
        self.quantity = quantity
        self.price = price
        self.product = product

class ShoppingCart:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self,created: str):
        self.created = created
        self.items = [] 
    def add_item(self, producto: Product):
        self.items.append(producto)


class Payment:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self, id: str, paid: str, total: float, details: str):
        self.paid = paid
        self.id = id
        self.total = total
        self.shipped = None
        self.details = details

    def __str__(self):
        return f"Pago hecho a fecha{self.paid} con un total de {self.total}"
        


class Order:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def __init__(self, number: str, ordered: str, ship_to: str, status: OrderStatus, total: float):
        self.number = number
        self.ordered = ordered
        self.ship_to = ship_to
        self.shipped = None
        self.status = status
        self.total = total
        self.cart = None
        self.payments = []

    def add_item(self, pago: Payment):
        self.payments.append(pago)
    
    def __str__(self):
        return f"Pedido con numero{self.number} fecha que ha sido solicitado{self.ordered} orden para {self.ship_to} cuyo carrito es {self.cart} y cuyos pedidos son {self.payments}"

