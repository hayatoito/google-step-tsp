#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


class LineSegment:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.min_x = min(point_1[0], point_2[0])
        self.min_y = min(point_1[1], point_2[1])
        self.max_x = max(point_1[0], point_2[0])
        self.max_y = max(point_1[1], point_2[1])
        (
            self.is_y_axis_parallel,
            self.slope,
            self.intercept,
        ) = self.cal_line_slope_and_intercept()

    def cal_line_slope_and_intercept(self) -> list[bool, float]:
        """
        2点が与えられた時、その2点を結ぶ直線の傾きとy切片を返す
        ただし、座標軸に並行な直線の入力はないとする

        Args:
            point_1 (list[float]): 座標
            point_2 (list[float]): 座標
            self (LineSegment):

        Returns:
            list[bool, float]: 直線が座標軸に並行かどうか,直線の傾きとy切片
            is_y_axis_parallel (bool): 直線がy軸に並行ならTrue,それ以外はFalse
            slope (float): 直線の傾き.ただしy軸に並行な場合はNoneを返す
            intercept (float): y切片.  ただし、y軸に並行な場合はx切片を返す
        """

        x_1, y_1 = self.point_1[0], self.point_1[1]
        x2, y2 = self.point_2[0], self.point_2[1]
        if x2 - x_1 == 0:
            return [True, None, x_1]
        slope = (y2 - y_1) / (x2 - x_1)
        intercept = y_1 - slope * x_1
        return [False, slope, intercept]

    # 線分同士の交差判定
    def is_cross(self, other) -> bool:
        """
        線分同士が交差するか判定

        Args:
            self (LineSegment): 線分を表すインスタンス
            other (LineSegment): 線分を表すインスタンス

        Returns:
            bool: 線分同士が交差すればTrueを、それ以外はFalseを返す
        """

        # selfがy軸に並行な場合
        if self.is_y_axis_parallel:
            x_intercept = self.intercept
            # selfの直線に関して、逆またはselfの直線と重なるかどうか
            if other.min_x > x_intercept or other.max_x < x_intercept:
                return False
            else:
                # x = intercept のyの値で交差するか判定
                # otherはy軸に並行ではない
                # 交点のy座標がself上にあるか
                cross_point_y = other.slope * x_intercept + other.intercept
                if self.min_y <= cross_point_y and cross_point_y <= self.max_y:
                    return True
                else:
                    return False

        # selfがy軸に並行でない場合
        else:
            # selfに関して、逆またはselfの直線と重なるかどうか
            if (other.point_1[1] - self.slope * other.point_1[0] - self.intercept) * (
                other.point_2[1] - self.slope * other.point_2[0] - self.intercept
            ) > 0:
                return False

            else:
                # otherがy軸に並行な場合
                if other.is_y_axis_parallel:
                    x_intercept = other.intercept
                    cross_point_y = self.slope * x_intercept + self.intercept
                    # 交点のy座標がself上にあるか
                    if cross_point_y <= self.y_max and self.y_min <= cross_point_y:
                        return True
                    else:
                        return False
                # self, otherどちらもy軸に並行でない場合
                else:
                    cross_point_x = -(self.intercept - other.intercept) / (
                        self.slope - other.slope
                    )  # 交点
                    # 交点のx座標がself上にあるか
                    if self.min_x <= cross_point_x and cross_point_x <= self.max_x:
                        return True
                    else:
                        return False


def distance(city_1, city_2):
    return math.sqrt((city_1[0] - city_2[0]) ** 2 + (city_1[1] - city_2[1]) ** 2)


def solver_greedy(cities, start_city=0, visited_cities=[]):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = start_city
    unvisited_cities = set(range(1, N))
    if start_city != 0:
        unvisited_cities.remove(start_city)
    # visited_cities[0]は0でunvisited_citiesに存在しない
    for visited_city in visited_cities[1:]:
        unvisited_cities.remove(visited_city)
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour


def count_cross(tour, cities):
    num_of_cross = 0
    for idx, city in enumerate(tour):
        if idx + 1 >= len(tour):
            # 交差ほどき完了
            break
        line = LineSegment(cities[city], cities[tour[idx + 1]])
        idx += 2

        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            line_other = LineSegment(cities[tour[idx]], cities[tour[idx + 1]])
            if line.is_cross(line_other):
                num_of_cross += 1
            idx += 1

    return num_of_cross


# 交差する点同士を交換する時に、交換してスコアがよくなるなら交換、そうでないならその交差は飛ばす
def solve(cities, tour, min_path_length=0):
    N = len(cities)
    min_path_length = sum(
        distance(cities[tour[i]], cities[tour[(i + 1) % N]]) for i in range(N)
    )
    for idx, city in enumerate(tour):
        current_city_idx = idx
        if idx + 1 >= len(tour):
            # 交差ほどき完了
            return tour
        line = LineSegment(cities[city], cities[tour[idx + 1]])
        idx += 2

        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            line_other = LineSegment(cities[tour[idx]], cities[tour[idx + 1]])
            if line.is_cross(line_other):
                # city1とcity3を,city2とcity4をつなぐ
                new_tour = (
                    tour[: current_city_idx + 1]
                    + [i for i in reversed(tour[current_city_idx + 1 : idx + 1])]
                    + tour[idx + 1 :]
                )
                path_length = sum(
                    distance(cities[new_tour[i]], cities[new_tour[(i + 1) % N]])
                    for i in range(N)
                )
                if path_length < min_path_length:
                    min_path_length = path_length
                    return solve(cities, new_tour, min_path_length)
                else:
                    break
            idx += 1


# 交差する点同士を交換する時に、交換してスコアがよくなるなら交換、そうでないならその交差は飛ばす
def two_opt_update(cities, tour, min_path_length=0):
    N = len(cities)
    min_path_length = sum(
        distance(cities[tour[i]], cities[tour[(i + 1) % N]]) for i in range(N)
    )
    for idx, city in enumerate(tour):
        current_city_idx = idx
        if idx + 1 >= len(tour):
            # 交差ほどき完了
            return tour
        line = LineSegment(cities[city], cities[tour[idx + 1]])
        idx += 2

        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            line_other = LineSegment(cities[tour[idx]], cities[tour[idx + 1]])
            if line.is_cross(line_other):
                # city1とcity3を,city2とcity4をつなぐ
                new_tour = (
                    tour[: current_city_idx + 1]
                    + [i for i in reversed(tour[current_city_idx + 1 : idx + 1])]
                    + tour[idx + 1 :]
                )
                path_length = sum(
                    distance(cities[new_tour[i]], cities[new_tour[(i + 1) % N]])
                    for i in range(N)
                )
                if path_length < min_path_length:
                    min_path_length = path_length
                    return two_opt_update(cities, new_tour, min_path_length)
            idx += 1


def two_opt_original(cities, tour):
    for idx, city in enumerate(tour):
        current_city_idx = idx
        if idx + 1 >= len(tour):
            # 交差ほどき完了
            return tour
        line = LineSegment(cities[city], cities[tour[idx + 1]])
        idx += 2

        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            line_other = LineSegment(cities[tour[idx]], cities[tour[idx + 1]])
            if line.is_cross(line_other):
                # city1とcity3を,city2とcity4をつなぐ
                new_tour = (
                    tour[: current_city_idx + 1]
                    + [i for i in reversed(tour[current_city_idx + 1 : idx + 1])]
                    + tour[idx + 1 :]
                )
                return two_opt_original(cities, new_tour)
            idx += 1


# city2以外のもっとも近いcityのうち、crossが最も少なくなるものを選ぶ
# city2以外の最も近いcいtyを近い順にk個選び、一つ前よりscoreがよくなれば入れ替えるをくり返す
def solve_2_2(cities, tour, min_cross_counts=10000000000):
    for idx, city in enumerate(tour):
        current_city = city
        current_city_idx = idx
        if idx + 1 >= len(tour):
            # 交差ほどき完了
            return tour
        line = LineSegment(cities[city], cities[tour[idx + 1]])
        idx += 2

        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            line_other = LineSegment(cities[tour[idx]], cities[tour[idx + 1]])
            if line.is_cross(line_other):
                # city_2以外の一番近い点を探す
                # 準備----------------
                # city_2までのcityを入れる
                no_cross_tour = tour[: current_city_idx + 2]
                neighbors = []
                N = len(cities)
                dist = [[0] * N for i in range(N)]
                for i in range(N):
                    for j in range(i, N):
                        dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

                unvisited_cities = set(range(0, N))
                for visited_city in no_cross_tour:
                    unvisited_cities.remove(visited_city)
                # 準備完了------------
                # city1から近いcity2以外のk個のcityを探す
                k = 10  # ここを変えると結果が変わりそう
                for _ in range(k):
                    if len(unvisited_cities) == 0:
                        break
                    next_city = min(
                        unvisited_cities, key=lambda city: dist[current_city][city]
                    )
                    neighbors.append(next_city)
                    unvisited_cities.remove(next_city)

                visited_cities = tour[: current_city_idx + 1]
                less_cross_count = 10000000
                better_city = 0
                # この中で最良のcityを訪れる
                for next_city in neighbors:
                    new_tour = solver_greedy(
                        cities, start_city=next_city, visited_cities=visited_cities
                    )
                    if count_cross(tour, cities) < less_cross_count:
                        less_cross_count = count_cross(tour, cities)
                        better_city = next_city

                new_tour = solver_greedy(
                    cities, start_city=better_city, visited_cities=visited_cities
                )

                # city_1までのcityを入れる
                greedy_with_2opt_tour = visited_cities + new_tour

                # 解ける交差の数が最大に達した場合、その時点のtourを返して終了
                if count_cross(greedy_with_2opt_tour, cities) == min_cross_counts:
                    return greedy_with_2opt_tour

                if count_cross(greedy_with_2opt_tour, cities) < min_cross_counts:
                    min_cross_counts = count_cross(greedy_with_2opt_tour, cities)

                return solve_2_2(cities, greedy_with_2opt_tour, min_cross_counts)
            idx += 1


# city2以外のもっとも近いcityに行く
def solve_2_1(cities, tour, min_cross_counts=10000000000):
    for idx, city in enumerate(tour):
        current_city = city
        current_city_idx = idx
        if idx + 1 >= len(tour):
            # 交差ほどき完了
            return tour
        line = LineSegment(cities[city], cities[tour[idx + 1]])
        idx += 2

        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            line_other = LineSegment(cities[tour[idx]], cities[tour[idx + 1]])
            if line.is_cross(line_other):
                # city_2以外の一番近い点を探す
                # city_2までのcityを入れる
                no_cross_tour = tour[: current_city_idx + 2]
                N = len(cities)
                dist = [[0] * N for i in range(N)]
                for i in range(N):
                    for j in range(i, N):
                        dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
                unvisited_cities = set(range(0, N))
                for visited_city in no_cross_tour:
                    unvisited_cities.remove(visited_city)
                next_city = min(
                    unvisited_cities, key=lambda city: dist[current_city][city]
                )
                # city_1までのcityを入れる
                visited_cities = tour[: current_city_idx + 1]
                new_tour = solver_greedy(
                    cities, start_city=next_city, visited_cities=visited_cities
                )
                greedy_with_2opt_tour = visited_cities + new_tour

                # 解ける交差の数が最大に達した場合、その時点のtourを返して終了
                if count_cross(greedy_with_2opt_tour, cities) == min_cross_counts:
                    return greedy_with_2opt_tour

                if count_cross(greedy_with_2opt_tour, cities) < min_cross_counts:
                    min_cross_counts = count_cross(greedy_with_2opt_tour, cities)
                return solve_2_1(cities, greedy_with_2opt_tour, min_cross_counts)
            idx += 1


# 交差するcity_1,2とcity3,4の組を初めて見つけたら
# city1の次にcity3を訪れる
# そのあとの経路のたどり方は貪欲法に任せる
def solve_1(cities, tour, max_no_cross_tour=0):
    for idx, city in enumerate(tour):
        current_city_idx = idx
        if idx + 1 >= len(tour):
            # 交差ほどき完了
            return tour
        line = LineSegment(cities[city], cities[tour[idx + 1]])
        idx += 2

        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            line_other = LineSegment(cities[tour[idx]], cities[tour[idx + 1]])
            if line.is_cross(line_other):
                # city_1の次にcity3を訪れる
                next_city = tour[idx]
                # 交差が見つかったcityまでのcityをtourに入れる
                no_cross_tour = tour[: current_city_idx + 1]

                new_tour = solver_greedy(
                    cities, start_city=next_city, visited_cities=no_cross_tour
                )
                greedy_with_2opt_tour = no_cross_tour + new_tour

                # 解ける交差の数が最大に達した場合、その時点のtourを返して終了
                if len(no_cross_tour) == max_no_cross_tour:
                    return greedy_with_2opt_tour

                if len(no_cross_tour) > max_no_cross_tour:
                    max_no_cross_tour = len(no_cross_tour)
                return solve_1(cities, greedy_with_2opt_tour, max_no_cross_tour)
            idx += 1


if __name__ == "__main__":
    assert len(sys.argv) > 1
    cities = read_input(sys.argv[1])
    tour = solve(cities, solver_greedy(cities))
    print_tour(tour)
