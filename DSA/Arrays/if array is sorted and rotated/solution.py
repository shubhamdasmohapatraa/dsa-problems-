class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        
        count = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        
        return count <= 1

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.check([3, 4, 5, 1, 2]))  # True
    print(sol.check([2, 1, 3, 4]))     # False
    print(sol.check([1, 2, 3]))        # True
