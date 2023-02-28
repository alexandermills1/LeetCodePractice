"""
This code defines a class Solution with a method pivotIndex that takes a list of integers nums as input and returns an integer index. The goal of the method is to find 
the index of an element in the list such that the sum of all elements to the left of it is equal to the sum of all elements to the right of it.

The method starts by initializing two variables: answer and total. answer is initialized to -1 and will be returned if no pivot index is found. total is initialized to 
the sum of all elements in nums.

Next, the method enters a loop that iterates over the indices of nums. For each index i, the method calculates the sum of all elements to the right of nums[i] by 
subtracting nums[i] and the sum of all elements to the left of nums[i] (stored in the variable left_sum) from total. If the sum of elements to the left and right of 
nums[i] are equal, the method returns i as the pivot index.

If no pivot index is found in the loop, the method returns the value of answer (-1) to indicate that no pivot index exists in the list.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        answer = -1
        total = sum(nums)

        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]

        return answer
