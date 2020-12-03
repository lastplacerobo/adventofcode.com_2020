

def expand_grid(gd):

    for num, line in enumerate(gd):
        gd[num] = line + line

    return gd


def traverse_grid(gd):

    trees = 0
    stepsr = 0
    for num, line in enumerate(gd):

        if stepsr >= len(gd[num]):
            gd = expand_grid(gd)

        stepsr = stepsr + 3

        try:
            if gd[num+1][stepsr] == "#":


                x = gd[num+1]
                y = gd[num+1][stepsr-1]
                trees += 1

        except:
            continue

    return trees


def main():
    f = open("input.txt", "r")
    gd = f.read().splitlines()

    print(traverse_grid(gd))




if __name__ == "__main__":
    main()