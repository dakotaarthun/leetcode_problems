class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target

        for i in nums:
            for j in nums[nums.index(i)+1:]:
                if i + j == target:
                    return [nums.index(i),nums.index(j, nums.index(i)+1)]
                    
Solution.twoSum
