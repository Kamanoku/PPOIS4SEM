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
