class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i+1) for i in range(n)]
        for j in range(len(answer)):
            element = int(answer[j])
            if element % 3 == 0 and element % 5 == 0:
                answer[j] = "FizzBuzz"
            elif element % 3 == 0:
                answer[j] = "Fizz"
            elif element % 5 == 0:
                answer[j] = "Buzz"
                
        return answer
        