from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, pair, rate):
        pass


class RateService:                      
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def set_rate(self, pair, rate):
        for o in self.observers:        
            o.update(pair, rate)


class Display(Observer):
    def update(self, pair, rate):
        print(f"[Табло] {pair} = {rate}")


class Alert(Observer):
    def __init__(self, limit):
        self.limit = limit

    def update(self, pair, rate):
        if rate > self.limit:
            print(f"[ТРИВОГА] {pair} вище {self.limit}!")


class History(Observer):
    def __init__(self):
        self.data = []

    def update(self, pair, rate):
        self.data.append((pair, rate))



service = RateService()
display, history = Display(), History()
service.attach(display)
service.attach(Alert(42))
service.attach(history)

service.set_rate("USD/UAH", 41.0)
service.set_rate("USD/UAH", 42.5)

service.detach(display)                 
service.set_rate("EUR/UAH", 45.0)
print("Історія:", history.data)



class EmailNotifier(Observer):
    def __init__(self, address):
        self.address = address

    def update(self, pair, rate):
        print(f"[Email {self.address}] {pair} = {rate}")


service.attach(EmailNotifier("user@example.com"))
service.set_rate("USD/UAH", 43.0)
