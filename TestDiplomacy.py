# -------
# imports
# -------

from unittest import main, TestCase
from Diplomacy import diplomacy_solve

# -----------
# TestDiplomacy
# -----------


class TestDiplomacy (TestCase):
    # ----
    # read
    # ----

    def test_solve1(self):
        r = "A Madrid Hold\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A Madrid\n")
        )
    
    def test_solve2(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB Madrid\nC London\n")
        )
        
    def test_solve3(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]\n")
        )
        
    def test_solve4(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\n C London Support B\nD Austin Move London\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]\nC [dead]\nD [dead]\n")
        )
        
    def test_solve5(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]\nC [dead]\n")
        )
        
    def test_solve6(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB Madrid\nC [dead]\nD Paris\n")
        )
    def test_solve7(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")
        )
    def test_solve8(self):
        r = "A Madrid Support C\nB Barcelona Hold\nC London Move Madrid\n"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB Barcelona\nC [dead]\n")
        )


# ----
# main
# ----

if __name__ == "__main__":
    main()
