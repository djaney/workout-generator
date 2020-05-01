from pathlib import Path
import os
from .exercises import EXERCISES
import json


class Config:
    def __init__(self):
        directory = self.generate_config_directory()
        self.generate_exercise_config(directory)

    @staticmethod
    def get_config_directory():
        path = os.path.join(str(Path.home()), '.workout-gen')
        return path

    @staticmethod
    def get_exercises_path():
        return os.path.join(Config.get_config_directory(), 'exercises.json')

    @staticmethod
    def generate_config_directory():
        config_path = Config.get_config_directory()
        if not os.path.isdir(config_path):
            os.makedirs(config_path, exist_ok=True)
        return config_path

    @staticmethod
    def generate_exercise_config(directory):
        path = os.path.join(directory, 'exercises.json')
        if not os.path.isfile(path):
            with open(path, 'w') as f:
                json.dump(EXERCISES, f)

    def get_exercises(self):
        path = self.get_exercises_path()
        with open(path) as f:
            return json.load(f)
