class BankAccount:
    def __init__(self, owner, balance, rate=0.12):
        self._owner = owner        
        self._rate = rate          
        self.__balance = 0         
        self.balance = balance     

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс має бути числом")
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним")
        self.__balance = value

    @property
    def monthly_interest(self):    
        return self.__balance * self._rate / 12


acc = BankAccount("Іван", 10000)
print("Баланс:", acc.balance)

for bad in (-500, "багато"):
    try:
        acc.balance = bad
    except (ValueError, TypeError) as e:
        print(type(e).__name__, ":", e)

print("Відсотки за місяць:", acc.monthly_interest)
acc.balance = 20000
print("Після зміни балансу:", acc.monthly_interest)

try:
    print(acc.__balance)
except AttributeError as e:
    print("AttributeError:", e)

print("Через name mangling:", acc._BankAccount__balance)
