import copy
import random
from collections import Counter, defaultdict

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def draw(self, num):
        drawn = []
        for i in range(min(num, len(self.contents))):
            n = random.randint(0, len(self.contents) - 1)
            drawn.append(self.contents.pop(n))
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        success = True

        for key, value in expected_balls.items():
            if defaultdict(int, Counter(balls_drawn))[key] < value:
                success = False
                break

        if success:
            successes += 1

    return successes / num_experiments
