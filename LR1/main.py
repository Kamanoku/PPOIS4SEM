from army import Army
from soldier import Soldier
from military_base import MilitaryBase
from military_equipment import MilitaryEquipment
from command import Command
from operations.training_operation import TrainingOperation
from operations.logistics_operation import LogisticsOperation
from operations.combat_operation import CombatOperation
from operations.security_operation import SecurityOperation

def menu():
    print("\nMenu:")
    print("1. Create Army")
    print("2. Create Base")
    print("3. Add Soldier to Base")
    print("4. Add Equipment to Base")
    print("5. Execute Operations")
    print("6. Show Army Info")
    print("0. Exit")

def operation_menu():
    print("\nOperations Menu:")
    print("1. Training Operation")
    print("2. Logistics Operation")
    print("3. Combat Operation")
    print("4. Security and Defense Operation")
    print("0. Back to Main Menu")

def get_base_index(max_index):
    while True:
        try:
            index = int(input(f"Select base (0 to {max_index}): "))
            if 0 <= index <= max_index:
                return index
            else:
                print(f"Invalid input. Please enter a number between 0 and {max_index}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def choose_rank():
    print("Available Ranks:")
    for i, rank in enumerate(Soldier.RANKS):
        print(f"{i}. {rank[0]}")
    while True:
        try:
            rank_index = int(input("Select a rank by number: "))
            if 0 <= rank_index < len(Soldier.RANKS):
                return Soldier.RANKS[rank_index][0]
            else:
                print("Invalid input. Please select a valid rank number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def choose_equipment_type():
    print("Available Equipment Types:")
    for i, (eq_type, _) in enumerate(MilitaryEquipment.EQUIPMENT_TYPES.items()):
        print(f"{i}. {eq_type}")
    while True:
        try:
            equipment_index = int(input("Select an equipment type by number: "))
            if 0 <= equipment_index < len(MilitaryEquipment.EQUIPMENT_TYPES):
                return list(MilitaryEquipment.EQUIPMENT_TYPES.keys())[equipment_index]
            else:
                print("Invalid input. Please select a valid equipment type number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    army = None

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            army_name = input("Enter army name: ")
            leader_name = input("Enter command leader name: ")
            command = Command(leader_name)
            army = Army(army_name, command)
            print(f"Army '{army_name}' created with leader '{leader_name}'.")

        elif choice == '2' and army:
            base_name = input("Enter base name: ")
            base_location = input("Enter base location: ")
            base = MilitaryBase(base_name, base_location)
            army.add_base(base)
            print(f"Base '{base_name}' added to the army.")

        elif choice == '3' and army:
            if not army.bases:
                print("No bases available. Please create a base first.")
                continue
            base_index = get_base_index(len(army.bases) - 1)
            soldier_name = input("Enter soldier name: ")
            soldier_rank = choose_rank()  # Get rank from user
            army.bases[base_index].add_soldier(Soldier(soldier_name, soldier_rank))
            print(f"Soldier '{soldier_name}' added to base '{army.bases[base_index].name}'.")

        elif choice == '4' and army:
            if not army.bases:
                print("No bases available. Please create a base first.")
                continue
            base_index = get_base_index(len(army.bases) - 1)
            equipment_type = choose_equipment_type()  # Get equipment type from user
            equipment_model = input("Enter equipment model: ")
            army.bases[base_index].add_equipment(MilitaryEquipment(equipment_type, equipment_model))
            print(f"Equipment '{equipment_type}' added to base '{army.bases[base_index].name}'.")

        elif choice == '5' and army:
            while True:
                operation_menu()
                operation_choice = input("Choose an operation: ")
                if operation_choice == '1':
                    TrainingOperation("Training").execute(army)
                elif operation_choice == '2':
                    LogisticsOperation("Logistics").execute(army)
                elif operation_choice == '3':
                    CombatOperation("Combat").execute(army)
                elif operation_choice == '4':
                    SecurityOperation("Security and Defense").execute(army)
                elif operation_choice == '0':
                    break
                else:
                    print("Invalid option. Please try again.")

        elif choice == '6' and army:
            print(army)
            for base in army.bases:
                print(base)
                print(f"Soldiers: {base.soldiers}")
                print(f"Equipment: {base.equipment}")

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid option or no army created yet.")

if __name__ == "__main__":
    main()