from .exercises import (
    T_UPPER,
    T_LOWER,
    T_CORE,
    T_CARDIO
)
import random


TEMPLATES = {
    "balanced": {
        "title": "Balanced workout",
        "exercises": [
            (T_UPPER, 1),
            (T_LOWER, 1),
            (T_CORE, 1),
            (T_CARDIO, 1),
        ]
    },
    "upper-body": {
        "title": "Upper body focused",
        "exercises": [
            (T_UPPER, 1),
            (T_UPPER, 1),
            (T_LOWER, 1),
            (T_CORE, 1),
            (T_CORE, 1),
            (T_CARDIO, 1),
        ]
    },
    "lower-body": {
        "title": "Lower body focused",
        "exercises": [
            (T_LOWER, 1),
            (T_LOWER, 1),
            (T_UPPER, 1),
            (T_CORE, 1),
            (T_CORE, 1),
            (T_CARDIO, 1),
        ]
    }
}

def get_random_template():
    return random.choice(list(TEMPLATES.values()))


def get_template(key):
    return TEMPLATES[key]

