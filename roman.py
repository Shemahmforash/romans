class Roman(object):

    equivalences = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                    ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10),
                    ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

    @staticmethod
    def to_arabic(roman):
        result = 0
        index = 0

        for numeral, integer in Roman.equivalences:
            roman_lenght = len(numeral)
            while roman[index:index + roman_lenght] == numeral:
                result += integer
                index += roman_lenght

        return result
