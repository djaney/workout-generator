from .exercises import (
    T_UPPER,
    T_LOWER,
    T_CORE,
    T_CARDIO,
    S_RUNNING
)
import random


TEMPLATES = {
    "balanced": {
        "title": "Balanced",
        "exercises": [
            (T_UPPER, []),
            (T_LOWER, []),
            (T_CORE, []),
            (T_CORE, []),
            (T_CARDIO, []),
        ]
    },
    "upper": {
        "title": "Upper body",
        "exercises": [
            (T_UPPER, []),
            (T_LOWER, []),
            (T_UPPER, []),
            (T_CORE, []),
            (T_CORE, []),
            (T_CARDIO, []),
        ]
    },
    "lower": {
        "title": "Lower body",
        "exercises": [
            (T_LOWER, []),
            (T_UPPER, []),
            (T_LOWER, []),
            (T_CORE, []),
            (T_CORE, []),
            (T_CARDIO, []),
        ]
    },
    "running": {
        "title": "Running",
        "exercises": [
            (T_LOWER, [S_RUNNING]),
            (T_LOWER, [S_RUNNING]),
            (T_LOWER, [S_RUNNING]),
            (T_LOWER, [S_RUNNING]),
            (T_CORE, []),
            (T_CORE, []),
        ]
    }
}

def get_random_template():
    return random.choice(list(TEMPLATES.values()))


def get_template(key):
    return TEMPLATES[key]

