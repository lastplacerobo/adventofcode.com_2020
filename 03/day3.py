def traverse_map(tmap):
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


def main():
    f = open("input.txt", "r")
    tmap = f.read().splitlines()

    print("Part1, nr of trees:", traverse_map(tmap))


if __name__ == "__main__":
    main()
