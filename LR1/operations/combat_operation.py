from operations.operation import Operation
from soldier import Soldier
import random

class CombatOperation(Operation):
    def execute(self, army):
        print("Combat operation started...")
        for base in army.bases:
            # Check soldier casualties
            for soldier in base.soldiers[:]:  # Create a copy to modify the list during iteration
                death_chance = next(rank[1] for rank in Soldier.RANKS if rank[0] == soldier.rank)
                if random.random() < death_chance:  # Check if soldier dies
                    print(f"{soldier} has died in battle!")
                    base.soldiers.remove(soldier)  # Remove soldier from base
                else:
                    print(f"{soldier} survived the battle.")

            # Check for equipment damage
            for equipment in base.equipment[:]:
                if random.random() < equipment.break_chance:  # Use equipment's break chance
                    print(f"{equipment} has been damaged in battle!")
                    base.equipment.remove(equipment)  # Remove damaged equipment

        print("Combat operation completed.")