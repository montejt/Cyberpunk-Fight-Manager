import unittest
from src.tools.npc import Npc

class Test(unittest.TestCase):
    # Test npc creation
    def test_create(self):
        npc = Npc("bob", 30, 11, 12, 3)
        self.assertEqual(["bob",30,30,11,11,12,12,3,[]],
                         [npc.name,npc.hp,npc.maxhp,npc.sph,npc.maxsph,npc.spb,npc.maxspb,npc.ds,npc.modifiers])

if __name__ == '__main__':
    unittest.main()
