import unittest
from soldier import Soldier

class TestSoldier(unittest.TestCase):
    def test_create_soldier_valid(self):
        soldier = Soldier("John", "Private")
        self.assertEqual(soldier.name, "John")
        self.assertEqual(soldier.rank, "Private")

    def test_create_soldier_invalid_rank(self):
        with self.assertRaises(ValueError):
            Soldier("John", "InvalidRank")

    def test_promote_soldier(self):
        soldier = Soldier("John", "Private")
        soldier.promote()
        self.assertEqual(soldier.rank, "Corporal")

if __name__ == "__main__":
    unittest.main()