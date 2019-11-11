import itertools

from solution import Solution

class SolutionGenerator:

    def __init__(self, directions, seq_a, seq_b, max_solutions):
        self.directions = directions
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.max_solutions = max_solutions

    def __iter__(self):
        return itertools.islice(self.find_solutions(), self.max_solutions)

    def find_solutions(self, curr_seq_a = '', curr_seq_b = '', pos=None):
        if pos is None:
            x, y = self.directions.shape[0] - 1, self.directions.shape[1] - 1
        else:
            x, y = pos

        if x == 0 and y == 0:
            yield Solution(curr_seq_a[::-1], curr_seq_b[::-1])
        # fast forward without recurence and just append what is required
        elif x == 0:
            yield Solution('_' * y + curr_seq_a[::-1], self.seq_b[:y] + curr_seq_b[::-1])
        elif y == 0:
            yield Solution(self.seq_a[:x] + curr_seq_a[::-1], '_' * x + curr_seq_b[::-1])
        else:      
            # check arrows and run function from new position in directions matrix
            if self.directions.is_up(x, y):
                next_seq_a = curr_seq_a + self.seq_a[x-1]
                next_seq_b = curr_seq_b + '_'
                yield from self.find_solutions(next_seq_a, next_seq_b, (x-1, y))

            if self.directions.is_left(x, y):
                next_seq_a = curr_seq_a + '_'
                next_seq_b = curr_seq_b + self.seq_b[y-1]
                yield from self.find_solutions(next_seq_a, next_seq_b, (x, y-1))
                
            if self.directions.is_diag(x, y):
                next_seq_a = curr_seq_a + self.seq_a[x-1]
                next_seq_b = curr_seq_b + self.seq_b[y-1]
                yield from self.find_solutions(next_seq_a, next_seq_b, (x-1, y-1))
        