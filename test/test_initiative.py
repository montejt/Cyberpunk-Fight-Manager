import unittest
from src.tools.initiative import InitiativeList

class Test(unittest.TestCase):
    def test_add(self):
        # Add 1
        initiative = InitiativeList()
        initiative.add("eight", 8)
        self.assertEqual(initiative.initiatives[0], ("eight", 8))

        # Add second after
        initiative.add("seven", 7)
        self.assertEqual(initiative.initiatives, [("eight", 8), ("seven", 7)])

        # Add third before
        initiative.add("nine", 9)
        self.assertEqual(initiative.initiatives, [("nine", 9), ("eight", 8), ("seven", 7)])

    def test_add_same(self):
        # Add same initiative twice
        initiative = InitiativeList()
        initiative.add("eight", 8)
        self.assertEqual(initiative.initiatives[0], ("eight", 8))

        initiative.add("beebus", 8)
        self.assertEqual(initiative.initiatives, [("beebus", 8), ("eight", 8)])

    def test_remove(self):
        initiative = InitiativeList()
        initiative.add("Remove", 8)
        self.assertEqual(initiative.initiatives, [("Remove", 8)])

        # Remove it
        initiative.remove("Remove")
        self.assertEqual(len(initiative.initiatives), 0)

        # Retry, but with three elements
        initiative.add("eight", 8)
        self.assertEqual(initiative.initiatives[0], ("eight", 8))
        initiative.add("seven", 7)
        self.assertEqual(initiative.initiatives, [("eight", 8), ("seven", 7)])
        initiative.add("nine", 9)
        self.assertEqual(initiative.initiatives, [("nine", 9), ("eight", 8), ("seven", 7)])

        # Remove eight
        initiative.remove("eight")
        self.assertEqual(initiative.initiatives, [("nine", 9), ("seven", 7)])

    def test_clear(self):
        # Fill a initiative and clear it
        initiative = InitiativeList()
        initiative.add("eight", 8)
        self.assertEqual(initiative.initiatives[0], ("eight", 8))
        initiative.add("seven", 7)
        self.assertEqual(initiative.initiatives, [("eight", 8), ("seven", 7)])
        initiative.add("nine", 9)
        self.assertEqual(initiative.initiatives, [("nine", 9), ("eight", 8), ("seven", 7)])
        initiative.clear()
        self.assertEqual(len(initiative.initiatives), 0)

if __name__ == '__main__':
    unittest.main()
