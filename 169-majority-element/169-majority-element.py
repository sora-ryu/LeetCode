class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        print(dictionary)
        for value in sorted(dictionary.values())[::-1]:  # Traverse starting from biggest value
            print(value)
            if value > len(nums)/2:
                return list(dictionary.keys())[list(dictionary.values()).index(value)]