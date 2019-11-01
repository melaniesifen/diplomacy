# -------
# imports
# -------

from unittest import main, TestCase
from Diplomacy import diplomacy_read, diplomacy_separate

# -----------
# TestDiplomacy
# -----------


class TestDiplomacy (TestCase):
    # ----
    # read
    # ----

    def test_read1(self):
        r = "A Madrid Hold"
        w = diplomacy_read(r)
        self.assertEqual(
            w, ["A Madrid Hold"])
        
    def test_separate1(self):
        r = "A Madrid Hold"
        w = diplomacy_separate(r)
        self.assertEqual(
            w, ("A", "Madrid", ["Hold"]))
        
    def test_separate2(self):
        r = "B Barcelona Move Madrid"
        w = diplomacy_separate(r)
        self.assertEqual(
            w, ("B", "Barcelona", ["Move", "Madrid"]))
    
    


# ----
# main
# ----

if __name__ == "__main__":
    main()
