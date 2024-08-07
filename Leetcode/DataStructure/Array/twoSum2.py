# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1-indexed  array : index start with 1 not 0
        

        numbers.insert(0, float('inf'))
        print(numbers)

        for i in range(1, len(numbers)):
            rest = target-numbers[i]
            if rest in numbers[i+1:]:
                return [i, numbers[i+1:].index(rest)+i+1]