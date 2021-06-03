import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def draw(self, num):
        random.shuffle(self.contents)
        drawn = self.contents[-num:]
        self.contents = self.contents[:-num]
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for i in range(num_experiments):
        hat_copy = hat.copy()
        balls_drawn = hat_copy.draw(num_balls_drawn)
