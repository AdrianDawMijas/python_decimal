
from WebUser import ShoppingCart, UserState, WebUser, Customer, Payment, Account, LineItem, Order, Product,OrderStatus

cesar = WebUser("2","1234",UserState.Banned)
alan = WebUser("3","1234",UserState.Active)
adrian = WebUser("4","1234",UserState.Blocked)

cesarCustom = Customer("2","casa","000000000","cesaro@chatgpt.com")
alanCustom = Customer("3","casa","000000000","alansito@chatgpt.com")
adrianCustom = Customer("4","casa","000000000","papi@chatgpt.com")

cesarAccount = Account("2","casita",True,"hoy","jamas")
alanAccount = Account("3","casita",False,"hoy","jamas")
adriansitoAccount = Account("4","casita",True,"hoy","jamas")

manzana = Product("1","manzana","Manzanero")
pera = Product("1","pera","Peron")
banana = Product("1","banana","Banano")

linea1 = LineItem(3,5.4,manzana)
linea2 = LineItem(3,5.4,pera)
linea3 = LineItem(3,5.4,banana)


cesarKart= ShoppingCart("hoy")
cesarKart.add_item(linea1)
cesarKart.add_item(linea2)
cesarKart.add_item(linea3)

pedido = Order("1","Hoy","Pepe", OrderStatus.Delivered,5.5)
pedido.cart=cesarKart

pago = Payment("1","hoy",4.5,"Va genial")
pedido.add_item(pago)

print(pedido)