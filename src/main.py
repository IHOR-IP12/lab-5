def pairs_of_tribes(pairs):
    boys = set()
    girls = set()
    count = 0

    for pair in pairs[1:]:
        boy, girl = pair
        if boy % 2 == 1:
            boys.add(boy)
        if girl % 2 == 0:
            girls.add(girl)

    count = len(boys) * len(girls)
    return count


pairs = [[3], [1, 2], [2, 4], [3, 5]]

result = pairs_of_tribes(pairs)

print(result)
