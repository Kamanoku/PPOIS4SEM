import unittest
from military_equipment import MilitaryEquipment

class TestMilitaryEquipment(unittest.TestCase):
    def test_create_equipment_valid(self):
        equipment = MilitaryEquipment("Tank", "T-90")
        self.assertEqual(equipment.type_, "Tank")
        self.assertEqual(equipment.model, "T-90")

    def test_create_equipment_invalid_type(self):
        with self.assertRaises(ValueError):
            MilitaryEquipment("InvalidType", "ModelX")

if __name__ == "__main__":
    unittest.main()