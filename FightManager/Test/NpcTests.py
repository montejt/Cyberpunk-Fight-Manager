import unittest
from ..Npc import *

class MyTestCase(unittest.TestCase):
    # Test npc creation
    def test_create(self):
        npc = Npc("bob", 30, 11, 12, 3)
        self.assertEqual(["bob",30,30,11,11,12,12,3,[]],
                         [npc.name,npc.hp,npc.maxhp,npc.sph,npc.maxsph,npc.spb,npc.maxspb,npc.ds,npc.modifiers])

    def test_hurt_default(self):
        # body: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(10, "d", "b", False)
        self.assertEqual([20,11,11],[bob.hp,bob.sph,bob.spb])

        # body: Damage goes through armor
        bob.hurt(20, "d", "b", False)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[11,11,10])

        # body: crit goes through armor
        bob.hurt(1, "d", "b", True)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[6,11,10])

        # head: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(10, "d", "h", False)
        self.assertEqual([20, 11, 11], [bob.hp, bob.sph, bob.spb])

        # head: Damage goes through armor
        bob.hurt(12, "d", "h", False)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [18, 10, 11])

        # head: crit goes through armor
        bob.hurt(1, "d", "h", True)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [13, 10, 11])

    def test_hurt_melee(self):
        # body: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(5, "m", "b", False)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[20,11,11])

        # body: Damage goes through armor
        bob.hurt(6, "m", "b", False)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[19,11,10])

        # body: crit goes through armor
        bob.hurt(1, "m", "b", True)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[14,11,10])

        # head: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(5, "m", "h", False)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [20, 11, 11])

        # head: Damage goes through armor
        bob.hurt(6, "m", "h", False)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [18, 10, 11])

        # head: crit goes through armor
        bob.hurt(1, "m", "h", True)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [13, 10, 11])

    def test_hurt_straight(self):
        # body: Damage doesn't go through armor
        bob = Npc("bob", 20, 5, 5, 3)
        bob.hurt(4, "s", "b", False)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[16,5,5])

        # body: Damage goes through armor
        bob.hurt(6, "s", "b", False)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[10,5,5])

        # body: crit goes through armor
        bob.hurt(0, "s", "b", True)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[5,5,5])

        # head: Damage doesn't go through armor
        bob = Npc("bob", 20, 1, 1, 3)
        bob.hurt(1, "s", "h", False)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [18, 1, 1])

        # head: Damage goes through armor
        bob.hurt(2, "s", "h", False)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [14, 1, 1])

        # head: crit goes through armor
        bob.hurt(0, "s", "h", True)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [9, 1, 1])

    def test_hurt_ab(self):
        # body: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(10, "ab", "b", False)
        self.assertEqual([20,11,11],[bob.hp,bob.sph,bob.spb])

        # body: Damage goes through armor
        bob.hurt(20, "ab", "b", False)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[11,11,9])

        # body: crit goes through armor
        bob.hurt(1, "ab", "b", True)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[6,11,9])

        # head: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(10, "ab", "h", False)
        self.assertEqual([20, 11, 11], [bob.hp, bob.sph, bob.spb])

        # head: Damage goes through armor
        bob.hurt(12, "ab", "h", False)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [18, 9, 11])

        # head: crit goes through armor
        bob.hurt(1, "ab", "h", True)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [13, 9, 11])

    def test_hurt_ap(self):
        # body: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(7, "ap", "b", False)
        self.assertEqual([20,11,11],[bob.hp,bob.sph,bob.spb])

        # body: Damage goes through armor
        bob.hurt(8, "ap", "b", False)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[19,11,10])

        # body: crit goes through armor
        bob.hurt(1, "ap", "b", True)
        self.assertEqual([bob.hp,bob.sph,bob.spb],[14,11,10])

        # head: Damage doesn't go through armor
        bob = Npc("bob", 20, 11, 11, 3)
        bob.hurt(7, "ap", "h", False)
        self.assertEqual([20,11,11],[bob.hp,bob.sph,bob.spb])

        # head: Damage goes through armor
        bob.hurt(8, "ap", "h", False)
        self.assertEqual([bob.sph,bob.spb],[10,11])
        self.assertIn(bob.hp,[18])

        # head: crit goes through armor
        bob.hurt(1, "ap", "h", True)
        self.assertEqual([bob.sph,bob.spb],[10,11])
        self.assertIn(bob.hp,[13])

        #body: test random, runs 100 trials
        for i in range(1, 100):
            bob = Npc("bob", 20, 11, 11, 3)
            bob.hurt(20, "ap", "b")
            self.assertEqual([bob.spb,bob.sph],[10,11])
            self.assertIn(bob.hp,range(8,14))

        # head: test random, runs 100 trials
        for i in range(1, 100):
            bob = Npc("bob", 20, 11, 11, 3)
            bob.hurt(15, "ap", "h")
            self.assertEqual([bob.spb,bob.sph],[11,10])
            self.assertIn(bob.hp,range(6,17))


    def test_hurt_negative(self):
        # Test that hp and armor cannot become negative
        bob = Npc("bob", 30, 0, 0, 3)
        bob.hurt(1000)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
