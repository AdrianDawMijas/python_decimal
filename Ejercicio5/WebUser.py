
# Definición de la clase UserState y OrderStatus como tipo Enum

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
    def _init_(self,login_id: str, password: str, state: UserState):
        self.login_id = login_id
        self.password = password
        self.state = state
        self.shopping_cart = None # Puede existir un WebUser sin tener aun un carrito creado.

    #Para printear el objeto
    def _str_(self):
        return f"WebUser(login={self.login_id},state={self.state.value})"

class Customer:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def _init_(self,id: str, address: str, phone: str, email: str):
        self.id = id
        self.address = address
        self.phone = phone
        self.email = email
        self.account = None 

class Account:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def _init_(self,id: str, billing_address: str, is_closed: bool, open: str, closed: str):
        self.id = id
        self.billing_address = billing_address
        self.is_closed = is_closed
        self.open = open
        self.closed = closed
        self.orders = []

class ShoopingCart:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def _init_(self,created: str):
        self.created = created
        self.items = [] 

class LineItem:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def _init_(self, quantity: int, price: float):
        self.quantity = quantity
        self.price = price

class Order:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def _init_(self, number: str, ordered: str, ship_to: str, status: OrderStatus, total: float):
        self.number = number
        self.ordered = ordered
        self.ship_to = ship_to
        self.shipped = None
        self.status = status
        self.total = total
        self.items = []
        self.payments = []

class Product:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def _init_(self, id: str, name: str, supplier: str):
        self.id = id
        self.name = name
        self.supplier = supplier

class Payment:
    #Constructor, declaramos variables para obligar a que sean de los tipos indicados
    def _init_(self, id: str, paid: str, total: float, details: str):
        self.number = number
        self.ordered = ordered
        self.ship_to = ship_to
        self.shipped = None
        self.status = status
        self.total = total
        
