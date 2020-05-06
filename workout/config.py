from pathlib import Path
import os
from .exercises import EXERCISES
import json


VERSION = 1


class InvalidConfigFormat(ValueError):
    pass


class InvalidConfigObject(ValueError):
    pass


class ConfigObject:
    def __init__(self, **kwargs):
        self.version = kwargs.get("version", None)
        self.exercises = kwargs.get("exercises", EXERCISES)

    @staticmethod
    def dump(obj, fp):
        if not isinstance(obj, ConfigObject):
            raise InvalidConfigObject()
        return json.dump({"version": obj.version, "exercises": obj.exercises}, fp)

    @staticmethod
    def load(fp):
        try:
            obj = json.load(fp)
        except json.JSONDecodeError:
            raise InvalidConfigFormat()
        if not isinstance(obj, dict):
            raise InvalidConfigFormat()
        return ConfigObject(**obj)


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
        if os.path.isfile(path):
            with open(path, 'r') as f:
                try:
                    if ConfigObject.load(f).version == VERSION:
                        return
                except InvalidConfigFormat:
                    pass

        with open(path, 'w') as f:
            ConfigObject.dump(ConfigObject(version=VERSION), f)

    def get_exercises(self):
        path = self.get_exercises_path()
        with open(path) as f:
            return ConfigObject.load(f).exercises
