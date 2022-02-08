# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element twice. 
# You can return the answer in any order. 

 

class Solution(object): 
    def twoSum(self, nums, target): 
        """ 
        :type nums: List[int] 
        :type target: int 
        :rtype: List[int] 
        """ 
        solution_dictionary = {} 

        for index, value in enumerate(nums): 
            solution = target - value 

            # See if solution exists in solution_dictionary 

            if solution in solution_dictionary: 
                return [index, solution_dictionary[solution]] 

            # Otherwise add to solution_dictionary 
            solution_dictionary[value] = index 

 

 