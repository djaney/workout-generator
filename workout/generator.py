from .exercises import (
    T_UPPER,
    T_LOWER,
    T_CORE,
    T_CARDIO,
    EXERCISES
)
import math
import random

def _generate_by_template(volume, sets, template):
    workouts = []
    for t, val in template:
        reps = math.floor(val / len(template) * volume / sets)
        e = get_exercises(t, exclude=list(map(lambda e: e[0][0], workouts)))
        if e is None:
            continue
        workouts.append((e, math.floor(e[3]*reps)))

    return workouts


def _format_workout(workout, sets):
    formatted = []
    for e in workout:
        formatted.append("{} x {}".format(e[0][0], e[1]))
    formatted = "\n".join(formatted)
    return formatted + "\n\nDo {} sets of each exercise".format(sets)


def generate_balanced(volume, sets):
    template = [
        (T_UPPER, 1),
        (T_LOWER, 1),
        (T_CORE, 1),
        (T_CARDIO, 1),
    ]
    workout = _generate_by_template(volume, sets, template)
    return _format_workout(workout, sets)


def get_exercises(exercise_type, exclude=None):
    if exclude is None:
        exclude = []

    choices = list(filter(lambda i: exercise_type == i[1] and i[0] not in exclude, EXERCISES))
    if len(choices) == 0:
        return None
    return random.choice(choices)
