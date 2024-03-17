import unittest
from src.tools.initiative import InitiativeQueue

class Test(unittest.TestCase):
    def test_add(self):
        # Add 1
        queue = InitiativeQueue()
        queue.add("eight", 8)
        self.assertEqual(queue.queue[0], ("eight", 8))

        # Add second after
        queue.add("seven", 7)
        self.assertEqual(queue.queue, [("eight", 8), ("seven", 7)])

        # Add third before
        queue.add("nine", 9)
        self.assertEqual(queue.queue, [("nine", 9), ("eight", 8), ("seven", 7)])

    def test_add_same(self):
        # Add same initiative twice
        queue = InitiativeQueue()
        queue.add("eight", 8)
        self.assertEqual(queue.queue[0], ("eight", 8))

        # Attempt to add second with same initiative
        queue.add("beebus", 8)
        self.assertEqual(queue.queue, [("eight", 8)])

    def test_remove(self):
        queue = InitiativeQueue()
        queue.add("Remove", 8)
        self.assertEqual(queue.queue, [("Remove", 8)])

        # Remove it
        queue.remove("Remove")
        self.assertEqual(len(queue.queue), 0)

        # Retry, but with three elements
        queue.add("eight", 8)
        self.assertEqual(queue.queue[0], ("eight", 8))
        queue.add("seven", 7)
        self.assertEqual(queue.queue, [("eight", 8), ("seven", 7)])
        queue.add("nine", 9)
        self.assertEqual(queue.queue, [("nine", 9), ("eight", 8), ("seven", 7)])

        # Remove eight
        queue.remove("eight")
        self.assertEqual(queue.queue, [("nine", 9), ("seven", 7)])

    def test_clear(self):
        # Fill a queue and clear it
        queue = InitiativeQueue()
        queue.add("eight", 8)
        self.assertEqual(queue.queue[0], ("eight", 8))
        queue.add("seven", 7)
        self.assertEqual(queue.queue, [("eight", 8), ("seven", 7)])
        queue.add("nine", 9)
        self.assertEqual(queue.queue, [("nine", 9), ("eight", 8), ("seven", 7)])
        queue.clear()
        self.assertEqual(len(queue.queue), 0)

if __name__ == '__main__':
    unittest.main()
