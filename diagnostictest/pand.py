class Board:
    def __init__(self, city_count, epicenter):
        if city_count <= 0:
            raise ValueError("Board needs at least one city")

        if epicenter < 1 or epicenter > city_count:
            raise IndexError("epicenter city number out of range")

        self.size = city_count
        self.epicenter = epicenter - 1
        self.day = 0

        self.states = ["."] * self.size
        self.infected_at = [None] * self.size

        self.states[self.epicenter] = "X"
        self.infected_at[self.epicenter] = 0

    def move(self, city_number):
        index = self._city_index(city_number)

        caseload = self._caseload(index)

        self._spread()

        return caseload

    def infected_city_numbers(self):
        infected = []

        for index in range(self.size):
            if self.states[index] == "X":
                infected.append(index + 1)

        return infected

    def _spread(self):
        infected_indexes = []

        for index in range(self.size):
            if self.states[index] == "X":
                infected_indexes.append(index)

        for index in infected_indexes:
            if index - 1 >= 0:
                self.states[index - 1] = "X"
                if self.infected_at[index - 1] is None:
                    self.infected_at[index - 1] = self.day + 1

            if index + 1 < self.size:
                self.states[index + 1] = "X"
                if self.infected_at[index + 1] is None:
                    self.infected_at[index + 1] = self.day + 1

        self.day += 1

    def _caseload(self, index):
        if self.infected_at[index] is None:
            return 0

        return self.day - self.infected_at[index] + 1

    def _city_index(self, city_number):
        if city_number < 1 or city_number > self.size:
            raise IndexError("city number out of range")

        return city_number - 1

class Solver:
    def __init__(self, board):
        self.board = board
        self.inspections = []

    def solve(self):
        possible_epicenters = set(range(1, self.board.size + 1))
        time_step = 0
        #optimizes the solver by limiting how many times it can call move().
        max_moves = self.board.size

        while len(possible_epicenters) > 1 and time_step < max_moves:
            city_number = (time_step % self.board.size) + 1

            caseload = self.board.move(city_number)

            self.inspections.append((city_number, time_step, caseload))

            possible_epicenters = {
                epicenter
                for epicenter in possible_epicenters
                # Keep this epicenter only if it would produce the same caseload.
                if self._expected_caseload(epicenter, city_number, time_step) == caseload
            }

            time_step += 1

        if len(possible_epicenters) == 1:
            return possible_epicenters.pop()

        return None

    def _expected_caseload(self, epicenter, city_number, time_step):
        distance = abs(epicenter - city_number)

        if time_step < distance:
            return 0

        return time_step - distance + 1

