# https://adventofcode.com/2020/day/1

# find the two entries that sum to 2020
def sum_of_two(vlist, xsum):
    for i in vlist:

        for y in vlist:

            if int(i) + int(y) == xsum:
                return (i, y)


# find the three entries that sum to 2020
def sum_of_three(vlist, xsum):
    for i in vlist:

        for y in vlist:

            for q in vlist:
                if int(i) + int(y) + int(q) == xsum:
                    return (i, y, q)


# multiply the entries in a list
def multiply(numList):
    result = 1
    for value in numList:
        result = result * int(value)

    return result


def main():
    f = open("input.txt", "r")
    lines = f.read().splitlines()

    ent = sum_of_two(lines, 2020)
    print("Part1:", multiply(ent))

    ent2 = sum_of_three(lines, 2020)
    print("Part2:", multiply(ent2))


if __name__ == "__main__":
    main()
