class Command:
    def __init__(self, leader):
        self.leader = leader

    def __repr__(self):
        return f"Command Leader: {self.leader}"