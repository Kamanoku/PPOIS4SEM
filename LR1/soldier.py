class Soldier:
    RANKS = [
        ("Private", 0.50),
        ("Corporal", 0.25),
        ("Sergeant", 0.125),
        ("Lieutenant", 0.10),
        ("Captain", 0.075),
        ("Major", 0.05),
        ("Colonel", 0.025),
        ("General", 0.01)
    ]

    def __init__(self, name, rank):
        self.name = name
        if rank in [r[0] for r in Soldier.RANKS]:
            self.rank = rank
        else:
            raise ValueError(f"Invalid rank '{rank}'. Please choose from {[r[0] for r in Soldier.RANKS]}.")

    def __repr__(self):
        return f"{self.rank} {self.name}"

    def promote(self):
        current_rank_index = next(i for i, r in enumerate(Soldier.RANKS) if r[0] == self.rank)
        if current_rank_index < len(Soldier.RANKS) - 1:
            self.rank = Soldier.RANKS[current_rank_index + 1][0]
            print(f"{self.name} has been promoted to {self.rank}!")
        else:
            print(f"{self.name} is already at the highest rank: {self.rank}.")