import unittest
from unittest.mock import patch
from operations.training_operation import TrainingOperation
from operations.logistics_operation import LogisticsOperation
from operations.combat_operation import CombatOperation
from operations.security_operation import SecurityOperation
from army import Army
from command import Command
from military_base import MilitaryBase
from soldier import Soldier
from military_equipment import MilitaryEquipment

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.army = Army("ArmyName", Command("Leader"))
        self.base1 = MilitaryBase("Base1", "Location1")
        self.base2 = MilitaryBase("Base2", "Location2")
        self.army.add_base(self.base1)
        self.army.add_base(self.base2)
        
        # Добавление солдата и техники на базу
        self.soldier = Soldier("John", "Private")
        self.base1.add_soldier(self.soldier)
        
        self.equipment = MilitaryEquipment("Tank", "T-90")
        self.base1.add_equipment(self.equipment)

    def test_training_operation(self):
        operation = TrainingOperation("Training")
        operation.execute(self.army)
        self.assertEqual(self.soldier.rank, "Corporal")  # Предполагается, что после тренировки ранг повышается

    @patch('builtins.input', side_effect=['0', '1', 's', '0'])
    def test_logistics_operation(self, mock_input):
        operation = LogisticsOperation("Logistics")
        
        # Выполняем логистическую операцию
        operation.execute(self.army)
        
        # Проверяем, что солдат перемещен на целевую базу
        self.assertNotIn(self.soldier, self.base1.soldiers)
        self.assertIn(self.soldier, self.base2.soldiers)

    @patch('builtins.input', side_effect=['0', '1', 'e', '0'])
    def test_transfer_equipment(self, mock_input):
        operation = LogisticsOperation("Logistics")
        
        # Выполняем логистическую операцию
        operation.execute(self.army)
        
        # Проверяем, что техника перемещена на целевую базу
        self.assertNotIn(self.equipment, self.base1.equipment)
        self.assertIn(self.equipment, self.base2.equipment)

    @patch('random.random', return_value=0.1)  # 10% шанс на успех
    def test_combat_operation(self, mock_random):
        operation = CombatOperation("Combat")
        initial_soldier_count = len(self.base1.soldiers)
        
        # Выполняем боевую операцию
        operation.execute(self.army)
        
        # Проверяем, что количество солдат изменилось
        new_soldier_count = len(self.base1.soldiers)
        
        # Проверяем, что солдат мог быть потерян
        self.assertNotEqual(initial_soldier_count, new_soldier_count)

    @patch('random.random', return_value=0.2)  # 20% шанс на успех
    def test_security_operation(self, mock_random):
        operation = SecurityOperation("Security")
        initial_soldier_count = len(self.base1.soldiers)
        
        # Выполняем операцию охраны
        operation.execute(self.army)
        
        # Проверяем, что количество солдат изменилось
        new_soldier_count = len(self.base1.soldiers)
        
        # Проверяем, что солдат мог быть потерян
        self.assertNotEqual(initial_soldier_count, new_soldier_count)

if __name__ == "__main__":
    unittest.main()