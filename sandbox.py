def minCost(colors: str, neededTime: list[int]) -> int:
    colors = ''.join([colors, '0'])

    def calculated_mins(array: list):
        # [2,3,1,3,5]
        return sum(array) - max(array)

    cost = 0
    index = 0
    counter = 0
    char = colors[0]

    for i in range(1, len(colors)):
        if colors[i] == char:
            counter += 1
        elif colors[i] != char and counter > 0:
            slice_ = neededTime[index:index + counter + 1]
            mins = calculated_mins(slice_)
            cost += mins
            counter = 0

        if counter == 0:
            char = colors[i]
            index = i

    return cost


# colors = "abaac"
# neededTime = [1, 2, 3, 4, 5]

colors = "aabaa"
neededTime = [1,2,3,4,1]

result = minCost(colors, neededTime)
pass
