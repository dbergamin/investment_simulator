from datetime import date


class Simulation:

    def __init__(self, start_date: date = None):
        if start_date is None:
            start_date = date.today()

        self.start_date = start_date
        self.current_date = date.today()
        self.current_tick = 0

    def tick(self):
        self.current_tick += 1


# Runnable as the main class
if __name__ == '__main__':
    simulation = Simulation(date.today())
    print("Hello world!")
    simulation.tick()
    print(simulation.current_tick)
