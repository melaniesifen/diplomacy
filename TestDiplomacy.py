# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_solve

# -----------
# TestDiplomacy
# -----------


class TestDiplomacy (TestCase):
    # ----
    # read
    # ----

    def test_solve(self):
        r = StringIO("A Madrid Hold\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A Madrid\n")
    

    def test_solve2(self):
        r = StringIO("A Madrid Hold\n B Barcelona Move Madrid\n C London Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\n B Mardid\n C London\n")
    

    def test_solve3(self):
        r = StringIO("A Madrid Hold\n B Barcelona Move Madrid\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\n B [dead]\n")
        
    def test_solve4(self):
        r = StringIO("A Madrid Hold\n B Barcelona Move Madrid\n C London Support B\n D Austin Move London\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\n B [dead]\n C [dead]\n D [dead]\n")
        
    def test_solve4(self):
        r = StringIO("A Madrid Hold\n B Barcelona Move Madrid\n C London Move Madrid\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\n B [dead]\n C [dead]\n")
        
    def test_solve5(self):
        r = StringIO("A Madrid Hold\n B Barcelona Move Madrid\n C London Support B\n D Paris Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\n B Madrid\n C [dead]\n D Paris\n")
        
    def test_solve6(self):
        r = StringIO("A Madrid Hold\n B Barcelona Move Madrid\n C London Move Madrid\n D Paris Support B\n E Austin Support A\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\n B [dead]\n C [dead]\n D Paris\n E Austin\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
