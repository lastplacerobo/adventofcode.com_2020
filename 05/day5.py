# https://adventofcode.com/2020/day/5

def find_row(boarding_data):
    boarding_with_row = {}
    for entry in boarding_data:

        boarding_with_row[entry] = {}

        front = 0
        back = 127

        for i in range(7):

            middle = (front + back) // 2

            if entry[i] == "F":
                back = middle

            elif entry[i] == "B":
                front = middle

        boarding_with_row[entry]["row"] = back

    return boarding_with_row


def find_seat(boarding_data):
    for entry in boarding_data:

        left = 0
        right = 7

        for i in range(7, 10):

            middle = (left + right) // 2

            if entry[i] == "L":
                right = middle

            elif entry[i] == "R":
                left = middle

        boarding_data[entry]["seat"] = right

    return boarding_data


def get_seat_id(boarding_data):
    for key, value in boarding_data.items():
        seat_id = boarding_data[key]["row"] * 8 + boarding_data[key]["seat"]

        boarding_data[key]["id"] = seat_id

    return boarding_data


def get_highest_seat_id(boarding_data):
    highest_seat_id = 0
    for key, value in boarding_data.items():

        if boarding_data[key]["id"] > highest_seat_id:
            highest_seat_id = boarding_data[key]["id"]

    return highest_seat_id


def find_my_seat(boarding_data):
    seat_ids = []

    for key, value in boarding_data.items():
        seat_ids.append(boarding_data[key]["id"])

    for id in seat_ids:
        if id + 1 not in seat_ids and id + 2 in seat_ids:
            my_seat = id + 1

    return my_seat


def main():
    boarding_pass = [line.strip() for line in open("input.txt")]

    complete_boarding = get_seat_id(find_seat(find_row(boarding_pass)))

    highest_seat_id = get_highest_seat_id(complete_boarding)

    print("Part1, highest seat ID:", highest_seat_id)

    print("Part2, my seat ID is:", find_my_seat(complete_boarding))


if __name__ == "__main__":
    main()
