def pairs_of_tribes(pairs):
    tribe_boys = {}
    tribe_girls = {}
    count = 0

    for tribe in pairs[1:]:
        tribe_id = tribe[0]
        boys = tribe[1::2]
        girls = tribe[2::2]

        if tribe_id not in tribe_boys:
            tribe_boys[tribe_id] = set()
        if tribe_id not in tribe_girls:
            tribe_girls[tribe_id] = set()

        tribe_boys[tribe_id].update(set(boys))
        tribe_girls[tribe_id].update(set(girls))

    for boys_set in tribe_boys.values():
        for girls_set in tribe_girls.values():
            count += len(boys_set) * len(girls_set)

    return count

pairs = [[3], [1, 2], [2, 3], [3, 4]]

result = pairs_of_tribes(pairs)

print(result)