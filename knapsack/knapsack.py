#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    value = 0
    weight = 0
    chosen = []
    # Increasing order of weight by value
    item_list = [Item(item.index, item.size,
                      float(item.value) / item.size) for item in items]
    # Sort by best value ratio
    sorted_list = sorted(
        item_list, key=lambda item: item.value, reverse=True)

    # Set base cases
    one = [[0, 0], [0, 0]]
    two = [0, 0]

    for item in sorted_list:
        # Fix edge cases
        if item.size == 1:
            one.append([item.index, item.value * item.size])
        elif weight + 1 == capacity and item.size == 2:
            two = [item.index, item.value * item.size]
        # Add best value items to knapsack
        if weight + item.size <= capacity:
            chosen.append(item.index)
            value += item.value * item.size
            weight += item.size

    # If 2 size 1 values are lower than 1 size 2 value
    # then swap the size 1 items w/ size 2 item
    if one[-1][1] + one[-2][1] < two[1]:
        chosen.remove(one[-1][0])
        chosen.remove(one[-2][0])
        chosen.append(two[0])
        value = value - one[-1][1] - one[-2][1] + two[1]

    return {'Value': value, 'Chosen': sorted(chosen)}


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
