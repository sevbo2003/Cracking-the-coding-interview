def binary_search(data, target) -> str:
    # data -> list[tuple[str, int]]
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (right + left) // 2
        if data[mid] <= target:
            result = mid
            left = mid + 1
        elif data[mid] > target:
            right = mid - 1
    return result


data = [10, 20]
target = 25

result = binary_search(data, target)
pass
