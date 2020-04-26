from .exercises import (
    EXERCISES,
    S_NO_EQUIP
)
import math
import random


class Generator:
    def __init__(self, volume, sets, formatter=None):
        self.volume = volume
        self.sets = sets
        self.formatter = formatter

    @staticmethod
    def get_exercises(exercise_type, exclude=None, secondary=None, equipment=None):
        if exclude is None:
            exclude = []

        if secondary is None:
            secondary = []

        if equipment is None:
            equipment = [S_NO_EQUIP]

        # filter by type
        choices = list(filter(lambda i: exercise_type == i[1], EXERCISES))
        # filter by exclude
        choices = list(filter(lambda i: i[0] not in exclude, choices))
        # filter by equipment
        choices = list(filter(lambda i: len(list(set(i[2]) & set(equipment))) > 0, choices))
        # filter by secondary type
        if len(secondary) > 0:
            choices = list(filter(lambda i:  len(list(set(i[2]) & set(secondary))) > 0, choices))
        if len(choices) == 0:
            return None
        return random.choice(choices)

    def generate_by_template(self, template):
        workouts = []
        for t, s in template['exercises']:
            reps = math.floor(1 / len(template['exercises']) * self.volume / self.sets)
            e = self.get_exercises(t,
                                   exclude=list(map(lambda x: x[0][0], workouts)),
                                   secondary=s)
            if e is None:
                continue
            workouts.append((e, math.floor(e[3]*reps)))

        if self.formatter is None:
            return workouts
        else:
            self.formatter.generator = self
            return self.formatter.format(workouts, template)
