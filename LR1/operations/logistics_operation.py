from operations.operation import Operation

class LogisticsOperation(Operation):
    def execute(self, army):
        print("Logistics operation started...")
        # Choose source base
        print("Available Bases for Transfer:")
        for i, base in enumerate(army.bases):
            print(f"{i}. {base.name}")
        source_index = int(input("Select source base by number: "))
        source_base = army.bases[source_index]

        # Choose target base
        print("Available Bases to Receive:")
        for i, base in enumerate(army.bases):
            if base != source_base:
                print(f"{i}. {base.name}")
        target_index = int(input("Select target base by number: "))
        target_base = army.bases[target_index]

        # Choose to transfer soldier or equipment
        transfer_type = input("Transfer (S)oldier or (E)quipment? ").strip().lower()
        
        if transfer_type == 's':
            print("Available Soldiers:")
            for i, soldier in enumerate(source_base.soldiers):
                print(f"{i}. {soldier}")
            soldier_index = int(input("Select soldier to transfer by number: "))
            soldier_to_transfer = source_base.soldiers[soldier_index]
            source_base.transfer_soldier(soldier_to_transfer, target_base)
        
        elif transfer_type == 'e':
            print("Available Equipment:")
            for i, equipment in enumerate(source_base.equipment):
                print(f"{i}. {equipment}")
            equipment_index = int(input("Select equipment to transfer by number: "))
            equipment_to_transfer = source_base.equipment[equipment_index]
            source_base.transfer_equipment(equipment_to_transfer, target_base)

        print("Logistics operation completed.")