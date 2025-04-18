from operations.operation import Operation

class TrainingOperation(Operation):
    def execute(self, army):
        print("Training operation started...")
        for base in army.bases:
            for soldier in base.soldiers:
                soldier.promote()  # Promote each soldier
        print("Training operation completed.")