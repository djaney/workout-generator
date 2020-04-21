from .exercises import (
    EXERCISES
)
import math
import random


class Generator:
    def __init__(self, volume, sets, formatter=None):
        self.volume = volume
        self.sets = sets
        self.formatter = formatter

    @staticmethod
    def get_exercises(exercise_type, exclude=None):
        if exclude is None:
            exclude = []

        choices = list(filter(lambda i: exercise_type == i[1] and i[0] not in exclude, EXERCISES))
        if len(choices) == 0:
            return None
        return random.choice(choices)

    def generate_by_template(self, template):
        workouts = []
        for t, val in template['exercises']:
            reps = math.floor(val / len(template['exercises']) * self.volume / self.sets)
            e = self.get_exercises(t, exclude=list(map(lambda x: x[0][0], workouts)))
            if e is None:
                continue
            workouts.append((e, math.floor(e[3]*reps)))

        if self.formatter is None:
            return workouts
        else:
            self.formatter.generator = self
            return self.formatter.format(workouts, template)
