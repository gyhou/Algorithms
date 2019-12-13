#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    weight = 0
    value = 0
    chosen = []
    item_dict = {}
    for i in items:
        item_dict[i[0]] = {'size': i[1], 'value': i[2], 'ratio': i[2]/i[1]}

    sorted_items = sorted(item_dict, key=lambda x: (
        item_dict[x]['ratio']), reverse=True)

    one = [[0, 0], [0, 0]]
    two = [0, 0]

    for i in sorted_items:
        if item_dict[i]['size'] == 1:
            one.append([i, item_dict[i]['value']])
        elif weight + 1 == capacity and item_dict[i]['size'] == 2:
            two = [i, item_dict[i]['value']]
        if item_dict[i]['size'] + weight <= capacity:
            weight += item_dict[i]['size']
            value += item_dict[i]['value']
            chosen.append(i)

    if one[-1][1] + one[-2][1] < two[1]:
        chosen.remove(one[-1][0])
        chosen.remove(one[-2][0])
        chosen.append(two[0])
        value = value - one[-1][1] - one[-2][1] + two[1]
    chosen.sort()
    return {'Value': value, 'Chosen': chosen}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
