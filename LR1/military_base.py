class MilitaryBase:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.soldiers = []
        self.equipment = []

    def add_soldier(self, soldier):
        self.soldiers.append(soldier)

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def transfer_soldier(self, soldier, target_base):
        if soldier in self.soldiers:
            self.soldiers.remove(soldier)
            target_base.add_soldier(soldier)
            print(f"Transferred {soldier} from {self.name} to {target_base.name}.")
        else:
            print(f"{soldier} not found in {self.name}.")

    def transfer_equipment(self, equipment, target_base):
        if equipment in self.equipment:
            self.equipment.remove(equipment)
            target_base.add_equipment(equipment)
            print(f"Transferred {equipment} from {self.name} to {target_base.name}.")
        else:
            print(f"{equipment} not found in {self.name}.")

    def __repr__(self):
        return f"Base: {self.name}, Location: {self.location}"