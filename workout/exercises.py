import random

T_UPPER = 1
T_LOWER = 2
T_CORE = 4
T_CARDIO = 8

# name, primary group, secondary group, reps scale (multiply reps)
EXERCISES = [
    # Upper body
    ("Push-up", T_UPPER, [], 1),
    ("Plyometric Push-up", T_UPPER, [], 1),

    # Core
    ("Inchworm", T_CORE, [T_UPPER], 1),
    ("Superman", T_CORE, [], 1),

    # Lower body
    ("Lunge-lunge-squat", T_LOWER, [], 1),
    ("Squat", T_LOWER, [], 1),
    ("Squat Jumps", T_LOWER, [], 1),

    # Cardio
    ("Burpees", T_CARDIO, [T_UPPER, T_LOWER, T_CORE], 1),
    ("High knees", T_CARDIO, [T_UPPER, T_LOWER, T_CORE], 1),
]


