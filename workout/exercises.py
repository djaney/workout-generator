import random

T_SHOULDER = 1
T_LEGS = 2
T_CORE = 4
T_BACK = 8
T_ABS = 16
T_CARDIO = 32

# name, primary group, secondary group, reps scale (multiply reps)
EXERCISES = [
    ("Push-up", T_SHOULDER, [], 1),
    ("Superman", T_BACK, [], 1),
    ("Lunge-lunge-squat", T_LEGS, [], 1),
    ("Burpees", T_CARDIO, [T_SHOULDER, T_LEGS, T_CORE], 1),
    ("Shuffle Burpees", T_CARDIO, [T_SHOULDER, T_LEGS, T_CORE], 0.8),
    ("Inchworm", T_SHOULDER, [T_CORE], 1),
]


def get_exercises(exercise_type, exclude=None):
    if exclude is None:
        exclude = []

    choices = list(filter(lambda i: exercise_type == i[1] and i[0] not in exclude, EXERCISES))
    if len(choices) == 0:
        return None
    return random.choice(choices)
