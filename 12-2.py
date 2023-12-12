import functools

@functools.cache
def n_arrangements(s, groups_left, group_sz):
    """
    s = what is left of input line
    groups_left = groups left (tuple)
    group_sz = current size of group in consumed line (s)
    """
    # base case for recursion
    if len(s) == 0:
        if len(groups_left) == 0 and group_sz == 0:
            # No groups left, it's a match
            return 1
        elif len(groups_left) == 1 and group_sz == groups_left[0]:
            # 1 group left the same size as current group, match
            return 1
        else:
            # No match
            return 0

    # consumed groups larger than groups left
    if len(groups_left) > 0 and group_sz > groups_left[0]:
        return 0
    # don't expect any more groups but I am in a group
    # I need group therapy
    elif len(groups_left) == 0 and group_sz > 0:
        return 0

    # all good so far
    n = 0

    spring = s[0]

    # If ? is # or if spring is # is the same case
    if spring == '#' or spring == '?':
        n += n_arrangements(s[1:], groups_left, group_sz + 1)

    # If ? is . or if spring is . is the same case
    if spring == '.' or spring == '?':
        if len(groups_left) > 0 and group_sz == groups_left[0]:
            n += n_arrangements(s[1:], groups_left[1:], 0)
        elif group_sz == 0:
            n += n_arrangements(s[1:], groups_left, 0)

    # so above ? will recurse 2 times while . or # will recurse
    # 1 time, each case consuming one input line (s) character

    return n

r = 0

with open("12.txt", "r") as f:
    for line in f:
        s, spans = line.split(" ")
        spans = spans.replace("\n", "")
        spans = ",".join(spans for _ in range(5))
        s = "?".join([s for i in range(5)])
        arr = tuple([int(i) for i in spans.split(",")])
        r+= n_arrangements(s, arr, 0)
    print(r)