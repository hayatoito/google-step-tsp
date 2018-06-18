#!/usr/bin/env python3

import sys

from common import print_tour, read_input


def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.
    return list(range(len(cities)))


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
