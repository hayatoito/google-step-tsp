#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def cal_line_slope_and_intercept(
    point1: list[float], point2: list[float]
) -> list[float]:
    """
    2点が与えられた時、その2点を結ぶ直線の傾きとy切片を返す

    Args:
        point1 (list[float]): 座標
        point2 (list[float]): 座標

    Returns:
        list[float]: 直線の傾きとy切片
        slope (float): 直線の傾き
        intercept (float): y切片
    """

    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept


point1 = [0, 0]
point2 = [1, 1]
point3 = [-1, 1]
point4 = [1, -1]


# 線分同士の交差判定
def is_cross(line1: list[list[float]], line2: list[list[float]]) -> bool:
    """
    線分同士が交差するか判定

    Args:
        line1 (list[list[float]]): 2点の座標をもつ配列. [[x1, y1], [x2,y2]]
        line2 (list[list[float]]): 2点の座標をもつ配列. [[x1, y1], [x2,y2]]

    Returns:
        bool: 線分同士が交差すればTrueを、それ以外はFalseを返す
    """

    point1, point2 = line1[0], line1[1]
    point3, point4 = line2[0], line2[1]
    slope1, intercept1 = cal_line_slope_and_intercept(point1, point2)

    # 直線に関して、逆または直線と重なるかどうか
    if (point3[1] - slope1 * point2[0] - intercept1) * (
        point4[1] - slope1 * point4[0] - intercept1
    ) <= 0:
        # 交点を求める
        slope2, intercept2 = cal_line_slope_and_intercept(point3, point4)
        cross_point_x = -(intercept1 - intercept2) / (slope1 - slope2)  # 交点
        # 交点のx座標が線分内であるか
        if cross_point_x >= min(point1[0], point2[0]) and cross_point_x <= max(
            point1[1], point2[1]
        ):
            return True
        else:
            return False

    else:
        # 直線に関して同じ
        return False


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solver_greedy(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour


# 交差するcity1,2とcity3,4の組みを始めて見つけたら
# city_idx = city1のインデックス
# no_cross_tour = tour[:city_idx+1]として
# citiesからno_cross_tourを引いたnew_citiesに対し、greedyを行う


def solve(cities):
    # 初めにgreedyをする
    tour = solver_greedy(cities)
    for idx, city in enumerate(tour):
        city_idx = idx
        if idx + 1 >= len(tour):
            break
        line = [cities[city], cities[tour[idx + 1]]]
        # あるcityとその次のcityを繋いだ線と交差する線があるか見ていく
        while idx < len(tour) - 2:
            idx += 1
            line_other = [cities[tour[idx]], cities[tour[idx + 1]]]
            if is_cross(line, line_other):
                # どうcity同士を交換するか
                # 交差が見つかったらcity2以外のcity1から最も近いcityを訪れる
                # そのあとは普通のgreedy
                # 交差が見つかったcityまでのcityをtourに入れる
                no_cross_tour = tour[: city_idx + 1]
                new_cities = [city for city in cities if city not in no_cross_tour]
                new_tour = solver_greedy(new_cities)
                #########注意
                # もしかしたらno_cross_tourとnew_tourを結合したらindexが2回現れるかもしれない
                # indexがどこで追加されるかわからないので一旦結果をprintする
                # new_tour[0] = indexなため
                greedy_with_2opt_tour = no_cross_tour + new_tour[1:]
                return greedy_with_2opt_tour
    return tour


if __name__ == "__main__":
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
