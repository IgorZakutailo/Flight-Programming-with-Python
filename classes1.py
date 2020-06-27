class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration


def main():

    # create flight.
    f = Flight(origin="New York", destination="Paris", duration=540)

    # Change the value of a variable.
    f.duration += 10 #если рейс задержали, я могу увеличить длительность полета на 10мин

    # Print details about flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)

print(main())
