class ProductOfNumbers:
    '''1st attempt: time limit exceeded'''
#     def __init__(self):
#         self.prefix = []

#     def add(self, num: int) -> None:
#         self.prefix.append(num)

#     def getProduct(self, k: int) -> int:
#         if k > len(self.prefix):
#             return 0

#         elif k == len(self.prefix):
#             product = 1
#             for element in self.prefix:
#                 product *= element
#             return product

#         else:
#             product = 1
#             for i in range(k):
#                 product *= self.prefix[-1-i]   # pop : it removes the element!
#             return product
    '''
2nd attempt: Since our objective is product the specific number of elements, try to previously multiply the input element in add function.
Input:1,2,3,4,5 => prefix:1,1,2,6,24,120
Input:2,3,0,0,5,6 => prefix:1,2,6,0,0,0,0 => prefix:1,2,6 / 1 / 1,5,30
    '''
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num:
            self.prefix.append(self.prefix[-1] * num)
        else:
            self.prefix = [1]       # Whenever you encounter 0, just initialize 

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):   # the length of self.prefix is (the number of input + 1)
                                    # if k is longer than the current array, it means that the length of k contains 0.
            return 0
        
        return int(self.prefix[-1] / self.prefix[-k-1])
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)