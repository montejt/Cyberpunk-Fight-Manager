import unittest
from src.tools.npcmanager import NpcManager
from src.tools.npc import Npc
from src.tools.types.damagetype import DamageType
from src.tools.types.target import Target

class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.mng = NpcManager()
        self.mng.add(Npc("bob", 50, 11, 11, 3))
        return super().setUp()

    def test_add_remove(self):
        # Add and remove an npc
        mng = NpcManager()
        jim = Npc("jim", 30, 11, 11, 3)
        mng.add(jim)
        self.assertIn(jim, mng.npcs)
        mng.remove(jim)
        self.assertNotIn(jim, mng.npcs)

    def test_clear(self):
        # add npc and clear the manager
        mng = NpcManager()
        mng.add(Npc("jim", 30, 11, 11, 3))
        mng.clear()
        self.assertEqual(len(mng.npcs), 0)

    def test_get(self):
        # add some npcs, and get one
        mng = NpcManager()
        mng.add(Npc("jim", 30, 11, 11, 3))
        tia = Npc("tia", 30, 11, 11, 5)
        mng.add(tia)
        mng.add(Npc("henry", 30, 11, 11, 5))
        self.assertIs(tia, mng.get("tia"))
    
    def test_hurt_standard_body_blocked_fully(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 11, DamageType.STANDARD.value, Target.BODY.value, False)
        self.assertEqual([50,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_standard_body_partially_blocked(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 12, DamageType.STANDARD.value, Target.BODY.value, False)
        # One damage, one ablation
        self.assertEqual([49,11,10],[bob.hp,bob.sph,bob.spb])

    def test_hurt_standard_body_crit(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 1, DamageType.STANDARD.value, Target.BODY.value, True)
        # Five damage, no ablation
        self.assertEqual([45,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_standard_head_blocked_fully(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 11, DamageType.STANDARD.value, Target.HEAD.value, False)
        self.assertEqual([50,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_standard_head_partially_blocked(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 12, DamageType.STANDARD.value, Target.HEAD.value, False)
        # Two damage, one ablation
        self.assertEqual([48,10,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_standard_head_crit(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 1, DamageType.STANDARD.value, Target.HEAD.value, True)
        # Five damage, no ablation
        self.assertEqual([45,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_melee_body_blocked_fully(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 5, DamageType.MELEE.value, Target.BODY.value, False)
        self.assertEqual([50,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_melee_body_partially_blocked(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 6, DamageType.MELEE.value, Target.BODY.value, False)
        # One damage, one ablation
        self.assertEqual([49,11,10],[bob.hp,bob.sph,bob.spb])

    def test_hurt_straight_body(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 10, DamageType.STRAIGHT.value, Target.BODY.value, False)
        self.assertEqual([40,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_armor_breaking_body_blocked_fully(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 11, DamageType.ARMOR_BREAKING.value, Target.BODY.value, False)
        self.assertEqual([50,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_armor_breaking_body_blocked_partially(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 12, DamageType.ARMOR_BREAKING.value, Target.BODY.value, False)
        self.assertEqual([49,11,9],[bob.hp,bob.sph,bob.spb])

    def test_hurt_armor_breaking_body_fully_blocked_crit(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 1, DamageType.ARMOR_BREAKING.value, Target.BODY.value, True)
        self.assertEqual([45,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_armor_piercing_body_blocked_fully(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 7, DamageType.ARMOR_PIERCING.value, Target.BODY.value, False)
        self.assertEqual([50,11,11],[bob.hp,bob.sph,bob.spb])

    def test_hurt_armor_piercing_body_blocked_partially(self):
        bob = self.mng.get("bob")
        self.mng.hurt("bob", 8, DamageType.ARMOR_PIERCING.value, Target.BODY.value, False)
        # No damage due to 1d6 after-piercing damage reduction
        self.assertEqual([49,11,10],[bob.hp,bob.sph,bob.spb])

    def test_hurt_negative(self):
        # Test that hp and armor cannot become negative
        bob = self.mng.get("bob")
        bob.sph = 0
        bob.spb = 0
        self.mng.hurt("bob", 1000, DamageType.STANDARD.value, Target.BODY.value, False)
        self.assertEqual([bob.hp, bob.sph, bob.spb], [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
