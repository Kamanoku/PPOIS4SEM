class MilitaryEquipment:
    EQUIPMENT_TYPES = {
        "BTR": 0.20,
        "Airplane": 0.15,
        "Helicopter": 0.30,
        "Tank": 0.05
    }

    def __init__(self, type_, model):
        if type_ in MilitaryEquipment.EQUIPMENT_TYPES:
            self.type_ = type_
            self.model = model
            self.break_chance = MilitaryEquipment.EQUIPMENT_TYPES[type_]
        else:
            raise ValueError(f"Invalid equipment type '{type_}'. Please choose from {list(MilitaryEquipment.EQUIPMENT_TYPES.keys())}.")

    def __repr__(self):
        return f"{self.type_} (Model: {self.model})"