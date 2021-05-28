import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
