#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    visited_cities = [current_city]

    while unvisited_cities:
        next_city = min(
            unvisited_cities, key=lambda unvisited_city: dist[current_city][unvisited_city])
        unvisited_cities.remove(next_city)
        visited_cities.append(next_city)
        current_city = next_city
    return visited_cities


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
