# https://adventofcode.com/2020/day/6

from collections import defaultdict
from collections import Counter


def split_groups(forms):
    groups = defaultdict(list)
    nr = 0
    for line in forms:

        if len(line) > 0:
            groups[nr].append(line)

        elif len(line) == 0:
            nr += 1

    return groups


def count_answers(forms):
    forms_counts = {}
    for key, group in forms.items():

        uniq_char = []

        for pers in group:

            for char in pers:

                if char not in uniq_char:
                    uniq_char.append(char)

        forms_counts[key] = len(uniq_char)

    tot_sum = 0
    for key, val in forms_counts.items():
        tot_sum = tot_sum + val

    return tot_sum


def count_answers_part2(forms):
    forms_counts = {}
    for key, group in forms.items():

        same_char = []
        counted_char = Counter("".join(group))

        for pers in group:

            for char in pers:

                # if char in group and counted_char[char] == len(group): ????
                if counted_char[char] == len(group):
                    same_char.append(char)

        forms_counts[key] = len(set(same_char))

    tot_sum = 0
    for key, val in forms_counts.items():
        tot_sum = tot_sum + val

    return tot_sum


def main():
    forms = [line.strip() for line in open("input.txt")]

    print("Part1, sum of counts:", count_answers(split_groups(forms)))

    print("Part2, sum of counts:", count_answers_part2(split_groups(forms)))


if __name__ == "__main__":
    main()
