# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。


def _sum(data, target):
    hash_map = {}
    for i, value in enumerate(data):
        number = target - value
        if hash_map.get(number) is not None:
            return [hash_map[number], i]
        hash_map[value] = i
    return None


print(_sum([3, 2, 4], 6))


def _other_sum(data, target):
    lens = len(data)
    j = -1
    for i in range(1, lens):
        temp = data[:i]
        new_data = target - data[i]
        if new_data in temp:
            j = temp.index(target - data[i])
            break
    if j >= 0:
        return [j, i]


print(_other_sum([3, 2, 4], 6))
