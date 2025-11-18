import re

RE_PASSPORT_ITEM = re.compile(r"([a-z]+):(\S+)")

REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def parse_input(input_string: str):
    for passport_str in input_string.split("\n\n"):
        yield {key: value for key, value in RE_PASSPORT_ITEM.findall(passport_str)}


def validate_passport(passport: dict[str, str]):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.

    try:
        birth_year = int(passport["byr"])
        issue_year = int(passport["iyr"])
        expiration_year = int(passport["eyr"])
        height = passport["hgt"]
        hair_color = passport["hcl"]
        eye_color = passport["ecl"]
        passport_id = passport["pid"]

        if not (1920 <= birth_year <= 2002):
            return False

        if not (2010 <= issue_year <= 2020):
            return False

        if not (2020 <= expiration_year <= 2030):
            return False

        value, unit = re.search(r"^(\d+)(cm|in)$", height).groups()

        match unit:
            case "cm":
                if not (150 <= int(value) <= 193):
                    return False
            case "in":
                if not (59 <= int(value) <= 76):
                    return False

        if not re.match(r"^#[0-9a-f]{6}$", hair_color):
            return False

        if eye_color not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        if not re.match(r"^\d{9}$", passport_id):
            return False
    except:
        return False
    else:
        return True


def solve_a(input_string: str):
    return sum(
        all(key in passport for key in REQUIRED_KEYS)
        for passport in parse_input(input_string)
    )


def solve_b(input_string: str):
    return sum(validate_passport(passport) for passport in parse_input(input_string))
