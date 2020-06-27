class Flight:

    counter = 1  # счетчик, который позволит мне пронумеровать каждый из моих рейсов

    def __init__(self, origin, destination, duration):

        # Keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1 #первый созданный нами рейс имеет ID 1, +1(будем обновлять этот счетчик каждый раз, когда создадим новый рейс)

        # Keep track of passengers.
        self.passengers = []  #список пассажиров, начинается как пустой, потому что когда мы впервые создадим рейс, никто не является пассажиром этого рейса

# последние три строчки - это то же самое, что мы видели раньше.
# Мы отслеживаем происхождение и пункт назначения, и продолжительность этого полета,
# чтобы чтобы хранить всю эту информацию внутри нашего объекта "Полет"


        # Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:") #распечатываем список пассажиров
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p): # p - это и есть имя пассажира
        self.passengers.append(p) # добавляем пассажира
        p.flight_id = self.id # устанавливаем идентификатор рейса пассажира
        # мы обновляем объект Пассажир, чтобы отслеживать, какой рейс с которым он ассоциируется


class Passenger:

    def __init__(self, name):
        self.name = name  # Всё, что сейчас делает класс Пассажиров, это отслеживание своего собственного имени.


def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)

    # Create passengers
    alice = Passenger(name='Alice')
    bob = Passenger(name='Bob')

    # Add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()

if __name__ == "__main__":
    main()
