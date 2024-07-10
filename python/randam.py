import random

m = ["A", "B", "C", "D", "E", "F"]


def split_group(m):
    # shuffle members
    random.shuffle(m)
    # split group 3 by 3 or 2 by 4
    num = random.choice([2, 3])
    first_group = m[:num]
    second_group = m[num:]
    return first_group, second_group

first_group, second_group = split_group(m)
first_group.sort()
second_group.sort()
print(first_group)
print(second_group)
