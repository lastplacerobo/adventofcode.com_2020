# https://adventofcode.com/2020/day/4

from collections import defaultdict
import re


def open_and_sort_pass():
    with open("input.txt") as f:
        data = f.readlines()

    # Remove newlines
    clean_data = []
    for line in data:
        clean_data.append(line.strip())

    # Create a dictionary with each passport in separates keys from the list
    passports = defaultdict(list)
    y = 0
    for line in clean_data:

        if len(line) > 0:
            passports[y].append(line)

        elif len(line) == 0:
            y += 1

    # Join the separate elements in the list so eatch key has one list with one element
    for key, value in passports.items():
        passports[key] = " ".join(value)

    # Create new dictionary with each passport field as key
    sorted_pass = {}
    for key, p_entry in passports.items():

        sorted_pass[key] = {}

        # sorted_pass[key][""]

        # Split string into multiple elements for each field separated by space
        p_entrylist = (p_entry.split(" "))

        # Split element in to key value pairs and save into new dictionary
        # with each field as a key
        for element in p_entrylist:
            kv = element.split(":")

            sorted_pass[key][kv[0]] = kv[1]

    return sorted_pass


def count_valid_passports_part1(passports, rfields):
    valid_passports = 0
    for passport, fields in passports.items():

        if "cid" in fields.keys():
            del fields["cid"]

        if rfields.keys() == fields.keys():
            valid_passports += 1

    return valid_passports


def count_valid_passports_part2(passports, rfields):
    valid_passports = 0

    for passport, fields in passports.items():
        valid_fields = 0

        if "cid" in fields.keys():
            del fields["cid"]

        # Only check content if all required fields are present
        if rfields.keys() == fields.keys():

            # Check Birth Year
            if rfields["byr"][0] <= int(fields["byr"]) <= rfields["byr"][1]:
                valid_fields += 1

            # Check Issue Year
            if rfields["iyr"][0] <= int(fields["iyr"]) <= rfields["iyr"][1]:
                valid_fields += 1

            # Check Expiration Year
            if rfields["eyr"][0] <= int(fields["eyr"]) <= rfields["eyr"][1]:
                valid_fields += 1

            # Check Height in cm
            if "cm" in fields["hgt"]:
                if rfields["hgt"]["cm"][0] <= int(fields["hgt"].strip("cm")) <= rfields["hgt"]["cm"][1]:
                    valid_fields += 1

            # Check Height in in
            if "in" in fields["hgt"]:
                if rfields["hgt"]["in"][0] <= int(fields["hgt"].strip("in")) <= rfields["hgt"]["in"][1]:
                    valid_fields += 1

            # Check Hair Color
            if fields["hcl"][0] == "#":
                if re.match('[a-f0-9]', fields["hcl"][1:]):
                    valid_fields += 1

            # Check Eye Color
            if fields["ecl"] in rfields["ecl"]:
                valid_fields += 1

            # Check Passport ID
            if len(fields["pid"]) == 9:

                if re.match('[0-9]', fields["pid"]):
                    valid_fields += 1

            else:
                continue

        if valid_fields == 7:
            valid_passports += 1

    return valid_passports


def main():
    req_fields = {
        "byr": [1920, 2002], "iyr": [2010, 2020], "eyr": [2020, 2030],
        "hgt": {"cm": [150, 193], "in": [59, 76]}, "hcl": "#xxxxxx",
        "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": "xxxxxxxxx"
    }

    sorted_pass = open_and_sort_pass()

    print("Part1, nr of valid passports:", count_valid_passports_part1(sorted_pass, req_fields))

    print("Part2, nr of valid passports:", count_valid_passports_part2(sorted_pass, req_fields))


if __name__ == "__main__":
    main()
