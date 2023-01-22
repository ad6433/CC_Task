
tax = 18/100
products = {}
users = {}
admins = {}

class product:
    
    def __init__(self, Id, name, price, stock, profit = 0, discount = 0):
        self.Id = Id
        self.name = name
        self.price = price
        self.stock = stock
        self.profit = profit
        self.discount = discount

    def cost(self, amount):
        return self.price * amount * (1 - self.discount / 100)

    def sold(self, amount):
        self.stock -= amount
        self.profit += self.cost(amount)

    
class perishableProd(product):

    def __init__(self, Id, name, price, stock, expiry_date, profit = 0, discount = 0):
        super().__init__(self, Id, name, price, stock, profit, discount)
        self.expiry_date = expiry_date


class customer():

    def __init__(self, Id, name, passwd, room, cart = []):
        self.__Id = Id
        self.name = name
        self.room = room
        self.cart = cart
        self._passwd = passwd

    def add_to_cart(self, product, qty):
        self.cart.append([product,qty])

    def payment(self, amount, mode):
        return True

    def billing(self):
        data = [[p[0].Id, p[0].name, p[0].price, p[1], p[0].cost(p[1])] for p in self.cart]
        total = sum([row[4] for row in data]) * (1 + tax)
        for i in data:
            print(*i)


class admin():

    def __init__(self, Id, passwd): 
        self.Id = Id
        self._passwd = passwd
    
    def add_category(self, name):
        products[name] = {}

    def add_product(self, Id, name, category, price, stock):
        products[category][Id] = product(Id, name, price, stock)

    def remove_product(self, category, Id):
        del products[category][id]
    
    def profit(self, category, Id):
        return products[category][Id].profit

# Test Admin/User
admins['admin'] = admin('admin', '0000')
users['2040A7PS8828P'] = customer('2040A7PS8828P', 'Paul', 'pass', 520)


def credentials():
    print('\nEnter Login Details')
    Id = input('Enter Id: ')
    passwd = input('Enter Password: ')
    return Id, passwd

def login():
    while True:
        print('Login\n1. User\n2. Admin')
        T = int(input('Enter Choice: '))
        if T == 2:
            Id, passwd = credentials()
            if Id in admins:
                if admins[Id]._passwd == passwd:
                    return 0, admins[Id]
                else:
                    print('Password did not match')
            else:
                print('No such Admin')
        elif T == 1:
            Id, passwd = credentials()
            if Id in users:
                if users[Id]._passwd == passwd:
                    return 1, users[Id]
                else:
                    print('Password did not match')
            else:
                print('No such User')

def user_menu(user):
    while True:
        print('User Menu\n1. Browse Categories\n2. Search for item\n3. Billing\n4. Logout')
        C = int(input('Enter Choice: '))
        if C == 1:
            print('Categories')
            for i, cat in enumerate(products):
                print(i + 1,'. ',cat)
            C = input('Enter category : ')
            for i, item in enumerate(products[C]):
                print(i + 1,'. ',item.name,' : ',item.price)
            I = input('Enter Item: ')
            I = products[C][I]
            qty = int(input('Enter qty : '))
            user.add_to_cart(I, qty)
        elif C == 2:
            I = input('Enter name of product: ')
            for cat in products:
                for product in products[cat]:
                    if product.name == I:
                        qty = int(input('Enter qty : '))
                        user.add_to_cart(product, qty)
            else:
                print('Product not found')
        elif C == 3:
            user.billing
        elif C == 4:
            return 0
        elif C == 5:
            print('Please enter a valid value')

def admin_menu(admin):
    while True:
        print('Admin Menu\n1. View Profits\n2. Manipulate Catalogue\n3. Logout')
        T = int(input('Enter Choice: '))
        if T == 1:
            for cat in products:
                for Id in products[cat]:
                    product = products[cat][Id]
                    print(product.Id,product.name,product.profit,sep=' : ')
        elif T == 2:
            print('Manipulation\n1. add a product\n2. add a category')
            C = int(input('Enter Choice: '))
            if C == 1:
                Id = input('Enter Id: ')
                name = input('Enter name: ')
                category = input('Enter Category: ')
                price = int(input('Enter Price: '))
                stock = int(input('Enter current stock: '))
                admin.add_product(Id, name, category, price, stock)
            elif C == 2:
                name = input('Enter category name: ')
                admin.add_category(name)
        elif T == 3:
            return 0
        else:
            print('Please Enter a valid value')
                

while True:
    L = login()
    if L[0] == 0:
        admin_menu(L[1])
    elif L[0] == 1:
        user_menu(L[1])






        
        






    
