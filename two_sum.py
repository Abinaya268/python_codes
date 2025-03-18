class Solution:
    def twoSum(self, nums):
        n = len(nums)
        print(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
sol=Solution()
List=[1,2,3,4,5]
target=9
a=sol.twoSum(List)
print(a)