def determine_order(notes):
    if notes == list(range(1, 9)):
        return "ascending"
    elif notes == list(range(8, 0, -1)):
        return "descending"
    else:
        return "mixed"


notes = list(map(int, input().split()))


print(determine_order(notes))