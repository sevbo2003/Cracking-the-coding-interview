def permute(nums: list[int]) -> list[list[int]]:
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        res.extend(perms)

        nums.append(n)

    return res


nums = [1, 2, 3]
ans = permute(nums)
pass
