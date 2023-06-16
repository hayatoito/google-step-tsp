#!/usr/bin/env python3

from common import format_tour, read_input

import solver_greedy_with_2opt

CHALLENGES = 7


def generate_my_output():
    for i in range(CHALLENGES):
        cities = read_input(f"input_{i}.csv")
        tour = solver_greedy_with_2opt.solve(
            cities, solver_greedy_with_2opt.solver_greedy(cities)
        )
        with open(f"output_{i}.csv", "w") as f:
            f.write(format_tour(tour) + "\n")


if __name__ == "__main__":
    generate_my_output()
