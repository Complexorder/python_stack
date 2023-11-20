class User:
    def __init__(self, name, email_address):
        self.name = name			
        self.email = email_address		
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):	
    	self.account_balance -= amount

    def desplay_user_method(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

user1 = User("mohmad", "mohamad@gmail.com")
user2 = User("sarah", "sarah@gmail.com")
user3 = User("nael", "nael@gmail.com")

user1.make_deposit(1000)
user1.make_deposit(500)
user1.make_deposit(500)
user1.make_withdrawal(500)
user1.desplay_user_method()

user2.make_deposit(100)
user2.make_deposit(900)
user2.make_withdrawal(300)
user2.make_withdrawal(400)
user2.desplay_user_method()

user3.make_deposit(3000)
user3.make_withdrawal(400)
user3.make_withdrawal(500)
user3.make_withdrawal(200)
user3.desplay_user_method()

user1.transfer_money(user3,200)

user1.desplay_user_method()
user3.desplay_user_method()