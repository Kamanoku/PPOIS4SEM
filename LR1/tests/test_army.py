import unittest
from army import Army
from command import Command
from military_base import MilitaryBase

class TestArmy(unittest.TestCase):
    def test_create_army(self):
        command = Command("Leader")
        army = Army("ArmyName", command)
        self.assertEqual(army.name, "ArmyName")
        self.assertEqual(army.command.leader, "Leader")

    def test_add_base(self):
        army = Army("ArmyName", Command("Leader"))
        base = MilitaryBase("Base1", "Location1")
        army.add_base(base)
        self.assertIn(base, army.bases)

if __name__ == "__main__":
    unittest.main()