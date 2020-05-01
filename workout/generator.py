from .exercises import (
    EXERCISES,
    S_NO_EQUIP
)
import math
import random
from .config import Config


class Generator:
    def __init__(self, volume, reps, formatter=None):
        self.volume = volume
        self.reps = reps
        self.formatter = formatter

    @staticmethod
    def _get_choices(exercises, exercise_type, exclude=None, secondary=None, equipment=None):
        if exclude is None:
            exclude = []

        if secondary is None:
            secondary = []

        if equipment is None:
            equipment = [S_NO_EQUIP]

        # filter by type
        choices = list(filter(lambda i: exercise_type == i[1], exercises))
        # filter by exclude
        choices = list(filter(lambda i: i[0] not in exclude, choices))
        # filter by equipment
        choices = list(filter(lambda i: len(list(set(i[2]) & set(equipment))) > 0, choices))
        # filter by secondary type
        if len(secondary) > 0:
            choices = list(filter(lambda i:  len(list(set(i[2]) & set(secondary))) > 0, choices))
        return choices

    @staticmethod
    def get_exercises(*argv, **kwargs):
        c = Config()
        choices = Generator._get_choices(c.get_exercises(), *argv, **kwargs)
        if len(choices) == 0:
            return None
        return random.choice(choices)

    @staticmethod
    def _calculate_sets(exercises, volume, reps):
        return math.floor(1 / exercises * volume / reps)

    def generate_by_template(self, template):
        workouts = []
        for t, s in template['exercises']:
            Generator._calculate_sets(len(template['exercises']), self.volume, self.reps)
            sets = math.floor(1 / len(template['exercises']) * self.volume / self.reps)
            e = self.get_exercises(t,
                                   exclude=list(map(lambda x: x[0][0], workouts)),
                                   secondary=s)
            if e is None:
                continue
            workouts.append((e, math.floor(e[3]*self.reps), sets))

        if self.formatter is None:
            return workouts
        else:
            self.formatter.generator = self
            return self.formatter.format(workouts, template)
