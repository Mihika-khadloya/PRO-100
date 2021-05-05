class Atm(object):
    def __init__(self,cardNumber, pinNumber, balanceAmount):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.balanceAmount=balanceAmount

    def CashWithdrawl(self, amount):
        self.amount=amount
        
        print(amount, "has been withdrawn from your account.")

    def BalanceEnquiry(self, amount, balanceAmount):
        amountLeft= self.balanceAmount-self.amount
        print(amountLeft, "is left in your account.")


john=Atm(12345, 1004, 30000)
john.CashWithdrawl(10000)
john.BalanceEnquiry(10000, 30000)