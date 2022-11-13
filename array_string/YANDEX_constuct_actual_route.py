"""
input:
[
    {"from": 'C', "to": 'Minsk'},
    {"from": 'Kiev', "to": 'N'},
    {"from": 'CH', "to": 'Moscow'},
    {"from": 'Minsk', "to": 'Kiev'},
    {"from": 'Moscow', "to": 'C'},
]

output:
[
    {"from": 'CH', "to": 'Moscow'},
    {"from": 'Moscow', "to": 'C'},
    {"from": 'C', "to": 'Minsk'},
    {"from": 'Minsk', "to": 'Kiev'},
    {"from": 'Kiev', "to": 'N'},
]
"""

from itertools import permutations
from typing import List

import pytest


def restore_route(routes: List[dict]) -> List[dict]:
    def find_difference(set1: set, set2: set) -> str:
        return list(set1.difference(set2))[0]

    from_cities_dict = {route["from"]: idx for idx, route in enumerate(routes)}
    to_cities_set = {route["to"] for route in routes}

    next_city = find_difference(set(from_cities_dict.keys()), to_cities_set)

    new_routes = []  # To-do
    for i in range(len(routes)):
        starting_city_index = from_cities_dict.get(next_city)
        next_city = routes[starting_city_index]["to"]
        new_routes.append(routes[starting_city_index])

    return new_routes


@pytest.mark.parametrize("input_data", permutations([
        {"from": 'C', "to": 'Minsk'},
        {"from": 'Minsk', "to": 'Kiev'},
        {"from": 'CH', "to": 'Moscow'},
        {"from": 'Kiev', "to": 'N'},
        {"from": 'Moscow', "to": 'C'},
    ]))
def test_restore_route(input_data):
    print(">> INPUT DATA", input_data)
    expected_result = [
        {"from": 'CH', "to": 'Moscow'},
        {"from": 'Moscow', "to": 'C'},
        {"from": 'C', "to": 'Minsk'},
        {"from": 'Minsk', "to": 'Kiev'},
        {"from": 'Kiev', "to": 'N'},
    ]
    actual_result = restore_route(input_data)
    print(">> ACTUAL RESULT", actual_result)
    assert actual_result == expected_result
