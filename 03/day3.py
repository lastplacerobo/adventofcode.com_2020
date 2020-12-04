# https://adventofcode.com/2020/day/3

def traverse_map_part1(tmap):
    trees = 0
    stepsr = 0
    for num, line in enumerate(tmap):

        stepsr += 3

        try:
            if tmap[num + 1][stepsr % len(line)] == "#":
                trees += 1

        except:
            continue

    return trees


def traverse_map_part2(tmap, move_row, move_col):
    trees = 0
    row, col = 0, 0

    while row + move_row < len(tmap):
        col += move_col
        row += move_row

        if tmap[row][col % len(tmap[row])] == "#":
            trees += 1

    return trees


def main():
    f = open("input.txt", "r")
    tmap = f.read().splitlines()

    print("Part1, nr of trees:", traverse_map_part1(tmap))

    slopes_p2 = {
        "1": {"col": 1, "row": 1},
        "2": {"col": 3, "row": 1},
        "3": {"col": 5, "row": 1},
        "4": {"col": 7, "row": 1},
        "5": {"col": 1, "row": 2},
    }

    ctrees = []
    trees2 = 1
    for key, value in slopes_p2.items():
        ctrees.append(traverse_map_part2(tmap, value["row"], value["col"]))

    for x in ctrees:
        trees2 *= x

    print("Part2, nr of trees:", trees2)


if __name__ == "__main__":
    main()
