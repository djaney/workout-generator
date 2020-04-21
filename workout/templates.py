from .exercises import (
    T_UPPER,
    T_LOWER,
    T_CORE,
    T_CARDIO
)


def get_random_template():
    return {
        "title": "Balanced workout",
        "exercises": [
            (T_UPPER, 1),
            (T_LOWER, 1),
            (T_CORE, 1),
            (T_CARDIO, 1),
        ]
    }

