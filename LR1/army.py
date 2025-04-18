class Army:
    def __init__(self, name, command):
        self.name = name
        self.bases = []
        self.command = command

    def add_base(self, base):
        self.bases.append(base)

    def __repr__(self):
        command_info = f"Command Leader: {self.command.leader}" if self.command else "Command Leader: Not Assigned"
        return f"Army: {self.name}, Bases: {len(self.bases)}, {command_info}"