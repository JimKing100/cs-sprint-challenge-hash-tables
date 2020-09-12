def has_negatives(a):

    pairs = {}
    result = []

    for i in range(len(a)):
        if a[i] > 0:
            pairs[i] = a[i]

    for i in range(len(a)):
        if a[i] < 0:
            if -a[i] in pairs.values():
                result.append(-a[i])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
