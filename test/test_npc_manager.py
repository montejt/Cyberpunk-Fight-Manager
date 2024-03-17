import unittest
from src.tools.npcmanager import NpcManager
from src.tools.npc import Npc

class Test(unittest.TestCase):
    def test_add_remove(self):
        # Add and remove an npc
        mng = NpcManager()
        bob = Npc("bob", 30, 11, 11, 3)
        mng.add(bob)
        self.assertIn(bob, mng.npcs)
        mng.remove(bob)
        self.assertNotIn(bob, mng.npcs)

    def test_clear(self):
        # add npc and clear the manager
        mng = NpcManager()
        mng.add(Npc("bob", 30, 11, 11, 3))
        mng.clear()
        self.assertEqual(mng.npcs.__len__(), 0)

    def test_get(self):
        # add some npcs, and get one
        mng = NpcManager()
        mng.add(Npc("bob", 30, 11, 11, 3))
        tia = Npc("tia", 30, 11, 11, 5)
        mng.add(tia)
        mng.add(Npc("henry", 30, 11, 11, 5))
        self.assertIs(tia, mng.get("tia"))


if __name__ == '__main__':
    unittest.main()
