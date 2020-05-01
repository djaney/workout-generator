T_UPPER = 1
T_LOWER = 2
T_CORE = 4
T_CARDIO = 8

S_RUNNING = 16
S_ONE_PER_SIDE = 32
S_SECONDS = 64
S_NO_EQUIP = 128
S_PLYOMETRIC = 256

PRIMARY_LABELS = {
    "upper": T_UPPER,
    "lower": T_LOWER,
    "core": T_CORE,
    "cardio": T_CARDIO,
}

SECONDARY_LABELS = {
    "running": S_RUNNING,
    "one-per-side": S_ONE_PER_SIDE,
    "seconds": S_SECONDS,
    "no-equip": S_NO_EQUIP,
    "plyometric": S_PLYOMETRIC,
}

# name, primary group, secondary group, reps scale (multiply reps)
EXERCISES = [
    # Upper body
    ("Push-up", T_UPPER, [S_NO_EQUIP], 1),
    ("Plyometric Push-up", T_UPPER, [S_NO_EQUIP, S_PLYOMETRIC], 0.5),

    # Core
    ("Plank with shoulder touch", T_CORE, [S_NO_EQUIP], 1),
    ("Plank up-down", T_CORE, [S_NO_EQUIP], 1),
    ("Crunches", T_CORE, [S_NO_EQUIP], 1.5),
    ("Plank", T_CORE, [S_SECONDS, S_NO_EQUIP], 2),
    ("Side plank", T_CORE, [S_SECONDS, S_ONE_PER_SIDE, S_NO_EQUIP], 2),
    ("Leg raise", T_CORE, [S_NO_EQUIP], 1.5),
    ("Russian twist", T_CORE, [S_NO_EQUIP], 1.5),
    ("Cocoon crunches", T_CORE, [S_NO_EQUIP], 1.5),
    ("Bycicle crunch", T_CORE, [S_NO_EQUIP], 1.5),

    # Lower body
    ("Lunges", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),
    ("Squat", T_LOWER, [S_NO_EQUIP], 1.5),
    ("Squat Jumps", T_LOWER, [S_NO_EQUIP], 1),
    ("Single leg hip thrust", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),
    ("Single leg romanian deadlift", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),
    ("Single leg glute bridge", T_LOWER, [S_RUNNING, S_ONE_PER_SIDE, S_NO_EQUIP], 1),

    # Cardio
    ("Burpees", T_CARDIO, [S_NO_EQUIP], 1),
    ("High knees", T_CARDIO, [S_NO_EQUIP], 1.5),
]


