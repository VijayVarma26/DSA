def array_pair_sum(arr, target):
    seen = set()
    output = set()
    for i in arr:
        diff = target-i
        if diff in seen:
            output.add((min(diff, i), max(diff, i)))
        else:
            seen.add(i)

    if seen:
        return output
    return None  

print(array_pair_sum([1, 2, 3, 4, 5], 6))              

