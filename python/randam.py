import random

m = ["A", "B", "C", "D", "E", "F"]


def split_group(m):
    # shuffle members
    random.shuffle(m)
    # split group 3 by 3 or 2 by 4
    if random.choice([0, 1]) == 0:
        first_group = m[:3]
        second_group = m[3:]
        return first_group, second_group
    else:
        first_group = m[:2]
        second_group = m[2:]
        return first_group, second_group

first_group, second_group = split_group(m)
first_group.sort()
second_group.sort()
print(first_group)
print(second_group)
