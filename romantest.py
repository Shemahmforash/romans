from roman import Roman
import unittest
import random
from hypothesis import given, strategies as st


ROMAN_ONES = [("I", 1), ("II", 2), ("III", 3)]
ROMAN_VS = [("V", 5), ("VI", 6), ("VII", 7), ("VIII", 8)]
ROMAN_UNITS = ROMAN_ONES + ROMAN_VS + [("IV", 4), ("IX", 9)]
ROMAN_TENS = [
    ("X", 10), ("XX", 20), ("XXX", 30), ("XL", 40), ("L", 50),
    ("LX", 60), ("LXX", 70), ("LXXX", 80), ("XC", 90)]
ROMAN_HUNDREDS = [
    ("C", 100), ("CC", 200), ("CCC", 300), ("CD", 400), ("D", 500),
    ("DC", 600), ("DCC", 700), ("DCCC", 800), ("CM", 900)]
ROMAN_THOUSANDS = [("M", 1000), ("MM", 2000), ("MMM", 3000)]


class RomanTest(unittest.TestCase):

    @unittest.skip("replaced by the ROMAN_UNITS test")
    @given(
        sample=st.sampled_from(ROMAN_ONES))
    def test_roman_I(self, sample):
        (roman, arabic) = sample

        self.assertEquals(Roman.to_arabic(roman), arabic)

    @unittest.skip("replaced by the ROMAN_UNITS test")
    @given(
        sample=st.sampled_from(ROMAN_VS))
    def test_roman_V(self, sample):
        (roman, arabic) = sample

        self.assertEquals(Roman.to_arabic(roman), arabic)

    @given(
        sample=st.sampled_from(ROMAN_UNITS))
    def test_roman_units(self, sample):
        (roman, arabic) = sample

        self.assertEquals(Roman.to_arabic(roman), arabic)

    @given(
        sample=st.sampled_from(ROMAN_TENS))
    def test_roman_tens(self, sample):
        (roman, arabic) = sample

        self.assertEquals(Roman.to_arabic(roman), arabic)

    @given(
        sample=st.sampled_from(ROMAN_HUNDREDS))
    def test_roman_hundreds(self, sample):
        (roman, arabic) = sample

        self.assertEquals(Roman.to_arabic(roman), arabic)

    @given(
        sample=st.sampled_from(ROMAN_THOUSANDS))
    def test_roman_thousands(self, sample):
        (roman, arabic) = sample

        self.assertEquals(Roman.to_arabic(roman), arabic)

    @given(
        choice=st.choices())
    def test_general_roman(self, choice):
        (roman, arabic) = self._generate_random_roman(choice)

        self.assertEquals(Roman.to_arabic(roman), arabic)

    @staticmethod
    def _generate_random_roman(choice):
        (roman, arabic) = ("", 0)

        source = [ROMAN_THOUSANDS, ROMAN_HUNDREDS, ROMAN_TENS, ROMAN_UNITS]

        for group in source:
            # randomly ignore groups
            if random.randint(0, 1):
                continue

            chosen = choice(group)
            roman += chosen[0]
            arabic += chosen[1]

        return roman, arabic


if __name__ == '__main__':
    unittest.main()
