# https://adventofcode.com/2020/day/2


def check_valid_pass_part1(pass_db):
    # {'fq_policy_low': '11', 'fq_policy_high': '16', 'let_policy': 'l', 'pass': 'llllqllllllllflq'}

    valid_pass = 0
    for idx, value in pass_db.items():

        # Check if letter is in password
        if value["let_policy"] in value["pass"]:

            # Check if nr or occurrences of letter in password is between low or high pass policy
            if int(value["fq_policy_low"]) <= value["pass"].count(value["let_policy"]) <= int(value["fq_policy_high"]):

                valid_pass += 1
            else:
                continue
        else:
            continue

    return valid_pass


def check_valid_pass_part2(pass_db):
    # {'fq_policy_low': '11', 'fq_policy_high': '16', 'let_policy': 'l', 'pass': 'llllqllllllllflq'}

    valid_pass = 0
    for idx, value in pass_db.items():

        both_match = False

        # Check if letter is in password
        if value["let_policy"] in value["pass"]:

            # Check if fq_policy_low position in the password contains the let_policy character
            if value["pass"][value["fq_policy_low"] - 1] == value["let_policy"]:

                # Handling of string index out of range
                try:
                    # Check if fq_policy_high position in the password contains the let_policy character
                    if value["pass"][value["fq_policy_high"] - 1] == value["let_policy"]:
                        both_match = True
                except:
                    continue

                if both_match == False:
                    valid_pass += 1

            # Check if fq_policy_high position in the password contains the let_policy character
            if value["pass"][value["fq_policy_high"] - 1] == value["let_policy"]:

                # Handling of string index out of range
                try:
                    # Check if fq_policy_low position in the password contains the let_policy character
                    if value["pass"][value["fq_policy_low"] - 1] == value["let_policy"]:
                        both_match = True
                except:
                    continue

                if both_match == False:
                    valid_pass += 1

    return valid_pass


def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    pass_db = {}

    for idx, entry in enumerate(lines):
        pass_db[idx] = {}
        pass_db[idx]["fq_policy_low"] = (int(entry.split()[0].split("-")[0]))
        pass_db[idx]["fq_policy_high"] = (int(entry.split()[0].split("-")[1]))
        pass_db[idx]["let_policy"] = (entry.split()[1]).replace(':', '')
        pass_db[idx]["pass"] = (entry.split()[2])

    print("Part1. Nr of valid passwords:", check_valid_pass_part1(pass_db))

    print("Part2. Nr of valid passwords:", check_valid_pass_part2(pass_db))


if __name__ == "__main__":
    main()
