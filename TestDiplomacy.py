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
        r = "A Madrid Hold"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A Madrid")
        )
    
    def test_solve2(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB Madrid\nC London")
        )
        
    def test_solve3(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]")
        )
        
    def test_solve4(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\n C London Support B\nD Austin Move London"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]\nC [dead]\nD [dead]")
        )
        
    def test_solve5(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]\nC [dead]")
        )
        
    def test_solve6(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB Madrid\nC [dead]\nD Paris")
        )
    def test_solve7(self):
        r = "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin")
        )
    def test_solve8(self):
        r = "A Madrid Support C\nB Barcelona Hold\nC London Move Madrid"
        w = diplomacy_solve(r)
        self.assertEqual(
            w, ("A [dead]\nB Barcelona\nC [dead]")
        )


# ----
# main
# ----

if __name__ == "__main__":
    main()
