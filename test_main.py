import unittest
from main import energyByStJeorEquation


class TestEnergyByStJeorEquation(unittest.TestCase):
    def test_male_normal_activity(self):
        self.assertAlmostEqual(
            energyByStJeorEquation(25, "male", 1.6, 175, 70), 11247.6, places=1
        )

    def test_female_normal_activity(self):
        self.assertAlmostEqual(
            energyByStJeorEquation(30, "female", 1.6, 160, 55), 8326.08, places=1
        )

    def test_divers_less_activity(self):
        self.assertAlmostEqual(
            energyByStJeorEquation(40, "divers", 1.4, 180, 80), 10143.0, places=1
        )
