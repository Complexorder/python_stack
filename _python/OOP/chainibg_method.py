class User:
    def __init__(self, name, email_address, account_balance):
        self.name = name			
        self.email = email_address		
        self.account_balance = account_balance

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):	
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

user1 = User("mohmad", "mohamad@gmail.com", 1000)
user2 = User("sarah", "sarah@gmail.com", 1500)
user3 = User("nael", "nael@gmail.com", 900)

user1.make_deposit(1000).make_deposit(500).make_withdrawal(500).display_user_balance()

#  user2.make_deposit(100)
# user2.make_deposit(900)
# user2.make_withdrawal(300)
# user2.make_withdrawal(400)
# user2.desplay_user_method()

user2.make_deposit(100).make_deposit(900).make_withdrawal(300).make_withdrawal(400).display_user_balance()

# user3.make_deposit(3000)
# user3.make_withdrawal(400)
# user3.make_withdrawal(500)
# user3.make_withdrawal(200)
# user3.desplay_user_method()

user3.make_deposit(3000).make_deposit(400).make_withdrawal(500).make_withdrawal(200).display_user_balance()