#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_price = prices[0]
    max = prices[1] - min_price
    for x in range(1, len(prices)):
        if prices[x] < min_price:
            min_price = prices[x]
        elif prices[x] - min_price > max:
            max = prices[x] - min_price
    return max


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
