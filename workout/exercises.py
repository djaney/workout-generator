import random

T_UPPER = 1
T_LOWER = 2
T_CORE = 3
T_CARDIO = 4

S_RUNNING = 100
S_ONE_PER_SIDE = 200
S_SECONDS = 300
S_NO_EQUIP = 400

# name, primary group, secondary group, reps scale (multiply reps)
EXERCISES = [
    # Upper body
    ("Push-up", T_UPPER, [S_NO_EQUIP], 1),
    ("Plyometric Push-up", T_UPPER, [S_NO_EQUIP], 1),

    # Core
    ("Inchworm", T_CORE, [S_NO_EQUIP], 1),
    ("Superman", T_CORE, [S_NO_EQUIP], 1),
    ("Crunches", T_CORE, [S_NO_EQUIP], 1.5),
    ("Plank", T_CORE, [S_SECONDS], 2),
    ("Side plank", T_CORE, [S_SECONDS, S_ONE_PER_SIDE], 2),
    ("Leg raise", T_CORE, [S_NO_EQUIP], 1.5),
    ("Russian twist", T_CORE, [S_NO_EQUIP], 1.5),
    ("Cocoon crunches", T_CORE, [S_NO_EQUIP], 1.5),
    ("Bycicle crunch", T_CORE, [S_NO_EQUIP], 1.5),

    # Lower body
    ("Lunges", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),
    ("Squat", T_LOWER, [S_NO_EQUIP], 1),
    ("Squat Jumps", T_LOWER, [S_NO_EQUIP], 1),
    ("Single leg hip thrust", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),
    ("Single leg romanian deadlift", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),
    ("Single leg glute bridge", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),

    # Cardio
    ("Burpees", T_CARDIO, [S_NO_EQUIP], 1),
    ("High knees", T_CARDIO, [S_NO_EQUIP], 1.5),
]


