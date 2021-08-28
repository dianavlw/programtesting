"""
    You are writing a computer program for an electronic vending machine to give you the optimal change for an item's cost.

    Create your own class in Python that takes in 

    Two arguments:
    -TOTAL PRICE
    -USERS AMOUNT PAID. 
    
    This class will have a method optimal_change which will output a string with the optimal change. Here it is in action:

    OUTPUT:
    change_maker = ChangeMaker(62.13, 100)

    change_maker.optimal_change()

    > "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

    change_maker2 = ChangeMaker(31.51, 50)
    change_maker2.optimal_change()
    > "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."


"""
class Change():

    def __init__(self, total_price, amount_paid):
        self.total_price = total_price
        self.amount_paid = amount_paid


    def __str__():
