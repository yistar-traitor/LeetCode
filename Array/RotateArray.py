"""
题号 189 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。

参考：https://leetcode-cn.com/problems/rotate-array/solution/chao-duo-chong-fang-fa-by-powcai/

"""
from typing import List

class Solution:
    # 解法一：丑陋版
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k <= 0:
            return
        count = (k % len(nums))
        if not count:
            return
        times = len(nums) - count
        nums[:] = nums[times:]+nums[:times]

    # 解法一：优雅版
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

    # 解法二
    def rotate3(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0,nums.pop())

if __name__ == '__main__':
    nums = [1,2]
    k = 1
    solution = Solution()
    solution.rotate3(nums,k)
    print(nums)