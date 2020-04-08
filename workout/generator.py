from .exercises import (
    get_exercises,
    T_SHOULDER,
    T_LEGS,
    T_CORE,
    T_BACK,
    T_ABS,
    T_CARDIO,
)
import math


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
        formatted.append("{} {} sets of {}".format(e[0][0], sets, e[1]))
    return formatted


def generate_balanced(volume, sets):
    template = [
        (T_SHOULDER, 1),
        (T_BACK, 1),
        (T_LEGS, 1),
        (T_CORE, 1),
        (T_ABS, 1),
        (T_CARDIO, 1),
    ]
    workout = _generate_by_template(volume, sets, template)
    return _format_workout(workout, sets)