class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description =''):
        self.ledger.append({'amount':amount,'description':description})

    def withdraw(self,amount,description =''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount':-amount,
                'description':description
                })
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance +=item['amount']
        return balance

    def transfer(self,amount,category):
        if self.withdraw(amount,f'Transfer to {category.name}'):
            category.deposit(amount,f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self,amount):
        return self.get_balance()>= amount

    def __str__(self):
        result = self.name.center(30,'*')+'\n'

        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = item['description'][:23]
            spaces = 30 - len(description) - len(amount)
            result+=description+(" "*spaces)+amount+'\n'
        result +=f'Total: {self.get_balance():.2f}'
        return result

    def __iter__(self):
        return iter(self.ledger)

def create_spend_chart(categories):
    spent = []

    for category in categories:
        total = 0

        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']

        spent.append(total)

    total_spent = sum(spent)


    percentages = []

    for amount in spent:
        percentage = int(amount / total_spent * 100)
        percentage = percentage // 10 * 10
        percentages.append(percentage)


    result = "Percentage spent by category\n"


    for level in range(100, -1, -10):
        result += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                result += " o "
            else:
                result += "   "
            
        result += " \n"

 
    result += "    " + "---" * len(categories) + "-\n"
    
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        result += "     "

        for category in categories:
            if i < len(category.name):
                result += category.name[i] + "  "
            else:
                result += "   "

        if i < max_length - 1:
            result += "\n"
    print(result)
    return result.rstrip("\n")
    

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
auto = Category('Auto')
food.transfer(50, clothing)
auto.deposit(1000, 'initial deposit')
auto.withdraw(10.15, 'groceries')
clothing.withdraw(10.15, 'groceries')
print(food)
print(clothing)
print(auto)
categories = [food,clothing,auto]
create_spend_chart(categories)
