from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summary = {}
        for i, num in enumerate(nums):
            if num in summary:
                summary[num].append(i)
            else:
                summary[num] = [i]
        for num in summary:
            if target - num in summary:
                if target == 2 * num:
                    if len(summary[num]) == 2:
                        return summary[num]
                else:
                    return summary[num] + summary[target-num]

if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 3, 4, 2], 6, [2, 3]),
        ([230, 863, 916, 585, 981, 404, 316, 785, 88, 12, 70, 435, 384, 778, 887, 755, 740, 337, 86, 92, 325, 422, 815, 650, 920, 125, 277, 336, 221, 847, 168, 23, 677, 61, 400, 136, 874, 363, 394, 199, 863, 997, 794, 587, 124, 321, 212, 957, 764, 173, 314,
          422, 927, 783, 930, 282, 306, 506, 44, 926, 691, 568, 68, 730, 933, 737, 531, 180, 414, 751, 28, 546, 60, 371, 493, 370, 527, 387, 43, 541, 13, 457, 328, 227, 652, 365, 430, 803, 59, 858, 538, 427, 583, 368, 375, 173, 809, 896, 370, 789], 542, [28, 45])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.twoSum(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.twoSum(t[0], t[1])
