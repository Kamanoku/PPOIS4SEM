import unittest
from military_base import MilitaryBase
from soldier import Soldier

class TestMilitaryBase(unittest.TestCase):
    def test_add_soldier(self):
        base = MilitaryBase("Base1", "Location1")
        soldier = Soldier("John", "Private")
        base.add_soldier(soldier)
        self.assertIn(soldier, base.soldiers)

    def test_transfer_soldier(self):
        base1 = MilitaryBase("Base1", "Location1")
        base2 = MilitaryBase("Base2", "Location2")
        soldier = Soldier("John", "Private")
        base1.add_soldier(soldier)
        base1.transfer_soldier(soldier, base2)
        self.assertNotIn(soldier, base1.soldiers)
        self.assertIn(soldier, base2.soldiers)

if __name__ == "__main__":
    unittest.main()