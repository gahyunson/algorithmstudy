from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
    

import unittest

class Test(unittest.TestCase):
    def test(self):
        input = 3 
        output = ["1","2","Fizz"]
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(input), output)

if __name__=='__main__':
    unittest.main()