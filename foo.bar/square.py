def solution(area):
    res = []
    while area > 0:
        biggest_square_side = int(area ** 0.5)
        biggest_square_area = biggest_square_side ** 2
        area -= biggest_square_area
        res.append(biggest_square_area)

    return res


area = 15324
a = solution(area)
print(a)
