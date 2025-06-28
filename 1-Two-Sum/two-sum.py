

from typing import List # This line is often at the top of the file if not already present

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Your implementation to find the two numbers
        # For example:
        num_map = {} # Initialize an empty dictionary
        for i, num in enumerate(nums): # Iterate through the list 'nums' with both index 'i' and value 'num'
            complement = target - num # Calculate the 'complement' needed to reach the target
            if complement in num_map: # Check if the 'complement' already exists as a key in 'num_map'
                return [num_map[complement], i] # If found, return the index of the complement and the current index 'i'
            num_map[num] = i # If complement not found, add the current number 'num' and its index 'i' to 'num_map'
        return [] # This line is reached if no two numbers sum up to the target (though the problem often guarantees a solution)