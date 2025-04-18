import unittest
from command import Command

class TestCommand(unittest.TestCase):
    def test_create_command(self):
        command = Command("Leader")
        self.assertEqual(command.leader, "Leader")

if __name__ == "__main__":
    unittest.main()