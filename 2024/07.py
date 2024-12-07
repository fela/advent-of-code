import re

data = open('d/07').read().strip()

def has_solution(result, nums, part):
    if nums[0] > result:
        return False
    if len(nums) == 1:
        return nums[0] == result
    if has_solution(result-nums[-1], nums[:-1], part):
        return True
    if result % nums[-1] == 0 and has_solution(result//nums[-1], nums[:-1], part):
        return True
    if part == 2 and str(result).endswith(str(nums[-1])):
        return has_solution(int(str(result)[:-len(str(nums[-1]))]), nums[:-1], part)
    return False

def solve(part=1):
    tot = 0
    for res, nums in re.findall(r'(\d+):\s+([\d ]+)', data):
        res = int(res)
        nums = [int(n) for n in nums.split()]
        if has_solution(res, nums, part):
            tot += res
    return tot

print(solve(part=1), solve(part=2))
