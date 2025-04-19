class Myway:

    def convert_to_roman(self, number: int) -> str:
        number_s = str(number)
        length = len(number_s)
        parts = [number_s[i] + "0" * (length - i - 1) for i in range(length)]
        return "".join([self._get_roman_part(part) for part in parts])

    def _get_roman_part(self, part: str) -> str:
        patterns = {
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX",
            "10": "X",
            "20": "XX",
            "30": "XXX",
            "40": "XL",
            "50": "L",
            "60": "LX",
            "70": "LXX",
            "80": "LXXX",
            "90": "XC",
            "100": "C",
            "200": "CC",
            "300": "CCC",
            "400": "CD",
            "500": "D",
            "600": "DC",
            "700": "DCC",
            "800": "DCCC",
            "900": "CM",
            "1000": "M",
            "2000": "MM",
            "3000": "MMM",
        }
        if part in patterns:
            return patterns[part]

        related_part = part[:-3]
        return patterns[related_part] + "\u0305"


class CourseWay:
    def convert_to_roman(self, number: int) -> str:
        parts = (
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        )
        for d, r in parts:
            if number >= d:
                return r + self.convert_to_roman(number - d)
        return ""


test_cases = [
    (39, "XXXIX"),
    (246, "CCXLVI"),
    (789, "DCCLXXXIX"),
    (2421, "MMCDXXI"),
    (573, "DLXXIII"),
    (4521, "IV̅DXXI"),
]

for number, expect in test_cases:
    myway = Myway()
    value = myway.convert_to_roman(number)
    assert value == expect, [number, value, expect]
print("ok")

for number, expect in test_cases:

    courseway = CourseWay()
    value = courseway.convert_to_roman(number)
    assert value == expect, [number, value, expect]
print("ok")
