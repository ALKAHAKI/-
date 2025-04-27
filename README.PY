class Plane:
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity
        self.passengers = []

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            passenger.board_plane(self)
            print(f"Пасажир {passenger.name} зайняв місце в літаку {self.model}.")
        else:
            print("Немає вільних місць у літаку!")

    def __str__(self):
        return f"Літак {self.model}, кількість пасажирів: {len(self.passengers)}/{self.capacity}"


class Passenger:
    def __init__(self, name):
        self.name = name
        self.plane = None

    def board_plane(self, plane):
        self.plane = plane

    def __str__(self):
        if self.plane:
            return f"{self.name} летить на літаку {self.plane.model}"
        else:
            return f"{self.name} чекає на рейс"


# Створення об'єктів
plane = Plane("Boeing 737", 2)
passenger1 = Passenger("Олександр")
passenger2 = Passenger("Марія")
passenger3 = Passenger("Іван")

# Посадка пасажирів
plane.board_passenger(passenger1)
plane.board_passenger(passenger2)
plane.board_passenger(passenger3)

# Виведення результатів
print(plane)
print(passenger1)
print(passenger2)
print(passenger3)
