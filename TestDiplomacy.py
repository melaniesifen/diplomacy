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

    def test_solve1(self):
        r = StringIO("A Madrid Hold\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A Madrid\n")
        )

    def test_solve2(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A [dead]\nB Madrid\nC London\n")
        )

    def test_solve3(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A [dead]\nB [dead]\n")
        )

    def test_solve4(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\n C London Support B\nD Austin Move London\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A [dead]\nB [dead]\nC [dead]\nD [dead]\n")
        )

    def test_solve5(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A [dead]\nB [dead]\nC [dead]\n")
        )

    def test_solve6(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A [dead]\nB Madrid\nC [dead]\nD Paris\n")
        )

    def test_solve7(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")
        )

    def test_solve8(self):
        r = StringIO(
            "A Madrid Support C\nB Barcelona Hold\nC London Move Madrid\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), ("A [dead]\nB Barcelona\nC [dead]\n")
        )


if __name__ == "__main__":
    main()
