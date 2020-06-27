class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

    def delay(self, amount):  #возможность задержать полет, это новый метод с названием задержка
        self.duration += amount  #срок который был раньше, к нему прибавляем сумму
                                 # Мы собираемся сделать f1.delay, чтобы вызвать метод задержки, передавая в качестве аргумента количество
                                 # Так что задержка технически принимает два аргумента - себя и количество

def main():
        f1 = Flight(origin="New York", destination="Paris", duration=540)
        f1.delay(100)
        f1.print_info()


if __name__ == "__main__":
    main()
