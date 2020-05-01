import unittest
from ..config import Config
import tempfile
from unittest.mock import patch
import os
import json
from ..exercises import EXERCISES


class ConfigTestCase(unittest.TestCase):
    @patch('pathlib.Path.home')
    def test_get_config_directory(self, dummy_home):
        dummy_home.return_value = 'dummy'
        self.assertEqual(os.path.join('dummy', '.workout-gen'), Config.get_config_directory())

    @patch('pathlib.Path.home')
    def test_get_exercises_path(self, dummy_home):
        dummy_home.return_value = 'dummy'
        path = Config.get_exercises_path()
        self.assertEqual(path, os.path.join('dummy', '.workout-gen', 'exercises.json'))

    @patch('pathlib.Path.home')
    def test_generate_config_directory(self, dummy_home):
        with tempfile.TemporaryDirectory() as tmp:
            dummy_home.return_value = tmp
            Config.generate_config_directory()
            self.assertTrue(os.path.isdir(os.path.join(tmp, '.workout-gen')))

    def test_generate_exercise_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            Config.generate_exercise_config(tmp)
            file_path = os.path.join(tmp, 'exercises.json')
            self.assertTrue(os.path.isfile(file_path))
            with open(file_path) as f:
                file_contents = f.read()
            self.assertEqual(json.dumps(EXERCISES), file_contents)

    @patch('pathlib.Path.home')
    def test_get_exercises(self, dummy_home):
        with tempfile.TemporaryDirectory() as tmp:
            dummy_home.return_value = tmp
            c = Config()
            e = c.get_exercises()
            self.assertEqual(json.dumps(EXERCISES), json.dumps(e))