import unittest
from ..exercises import (
    EXERCISES,
    T_UPPER,
    T_LOWER,
    T_CORE,
    T_CARDIO,
    S_PLYOMETRIC,
    S_NO_EQUIP
)
from ..generator import Generator


class ChoicesTestCase(unittest.TestCase):

    def test_get_simple(self):
        choices = Generator._get_choices(EXERCISES, T_UPPER)
        self.assertListEqual(EXERCISES[0:2], choices)

        choices = Generator._get_choices(EXERCISES, T_CORE)
        self.assertListEqual(EXERCISES[2:11], choices)

        choices = Generator._get_choices(EXERCISES, T_LOWER)
        self.assertListEqual(EXERCISES[11:17], choices)

        choices = Generator._get_choices(EXERCISES, T_CARDIO)
        self.assertListEqual(EXERCISES[17:19], choices)

    def test_exclude(self):
        choices = Generator._get_choices(EXERCISES, T_UPPER, exclude=['Plyometric Push-up'])
        self.assertListEqual(EXERCISES[0:1], choices)

    def test_secondary_tag(self):
        choices = Generator._get_choices(EXERCISES, T_UPPER, secondary=[S_PLYOMETRIC])
        self.assertListEqual(EXERCISES[1:2], choices)

    def test_equipment(self):
        choices = Generator._get_choices(EXERCISES, T_UPPER, equipment=[S_NO_EQUIP])
        self.assertListEqual(EXERCISES[0:2], choices)


class SetCalculatorTestCase(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(6, Generator._calculate_sets(5, 300, 10))
        self.assertEqual(6, Generator._calculate_sets(5, 300, 9))
