
```python
class Solution:
    def getSecondLargest(self, arr):
        largest = second_largest = -1
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        return second_largest

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.getSecondLargest([12, 35, 1, 10, 34, 1]))  # Output: 34
    print(sol.getSecondLargest([10, 5, 10]))             # Output: 5
    print(sol.getSecondLargest([10, 10, 10]))            # Output: -1
