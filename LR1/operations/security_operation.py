from operations.operation import Operation
from soldier import Soldier
import random

class SecurityOperation(Operation):
    def execute(self, army):
        print("Security and Defense operation started...")
        for base in army.bases:
            if random.random() < 0.30:  # 30% chance of success
                print(f"Security operation at {base.name} was successful.")
                if base.soldiers:
                    ranks = [rank[0] for rank in Soldier.RANKS]
                    highest_ranked_soldier = max(base.soldiers, key=lambda s: ranks.index(s.rank))
                    base.soldiers.remove(highest_ranked_soldier)
                    print(f"{highest_ranked_soldier} has died in the security operation.")
            else:
                print(f"Security operation at {base.name} failed. No casualties.")
        print("Security and Defense operation completed.")