#!/usr/bin/env python3

from common import format_tour, read_input

import solver_greedy_with_2opt

CHALLENGES = 7


def generate_my_output():
    for i in range(CHALLENGES):
        cities = read_input(f"input_{i}.csv")
        # cities = read_input("input_0.csv")
        # cities = read_input("input_" + str(i) + ".csv")
        tour = solver_greedy_with_2opt.solve(cities)
        with open(f"output_{i}.csv", "w") as f:
            f.write(format_tour(tour) + "\n")


if __name__ == "__main__":
    generate_my_output()
