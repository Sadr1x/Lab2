from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @property
    @abstractmethod
    def fee_rate(self):            
        pass

    @abstractmethod
    def validate(self, amount):     
        pass

    @abstractmethod
    def charge(self, amount):      
        pass

    def total_with_fee(self, amount):   
        return round(amount * (1 + self.fee_rate), 2)


class CardProcessor(PaymentProcessor):
    fee_rate = 0.02

    def validate(self, amount):
        if amount <= 0:
            raise ValueError("Сума має бути додатною")

    def charge(self, amount):
        return f"Картка: списано {self.total_with_fee(amount)} грн"


class PayPalProcessor(PaymentProcessor):
    fee_rate = 0.035

    def validate(self, amount):
        if not 0 < amount <= 10000:
            raise ValueError("PayPal: сума від 0 до 10000")

    def charge(self, amount):
        return f"PayPal: списано {self.total_with_fee(amount)} грн"



class Logger:
    def log(self, text):
        print("LOG:", text)


class Discount:
    def __init__(self, percent):
        self.percent = percent

    def apply(self, amount):
        return amount * (1 - self.percent / 100)


class Checkout:
    def __init__(self, processor, logger, discount):
        self.processor = processor      
        self.logger = logger            
        self.discount = discount        

    def pay(self, amount):
        amount = self.discount.apply(amount)    
        try:
            self.processor.validate(amount)     
            self.logger.log(self.processor.charge(amount))
        except ValueError as e:
            self.logger.log(f"Відхилено: {e}")


try:
    PaymentProcessor()
except TypeError as e:
    print("TypeError:", e)

for p in (CardProcessor(), PayPalProcessor()):
    print(type(p).__name__, p.fee_rate, p.total_with_fee(1000))

shop = Checkout(CardProcessor(), Logger(), Discount(10))
shop.pay(2000)
shop.pay(-5)
shop.processor = PayPalProcessor()      
shop.pay(20000)
shop.pay(500)
