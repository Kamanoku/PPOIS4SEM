class Operation:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Executing operation: {self.name}")