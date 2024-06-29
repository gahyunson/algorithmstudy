class Solution2:
    def romanToInt(self, s: str) -> int:
        # make dictionary
        # if s == dic.values - 1:
        # convert process
        # elif 
        # [0]*10**len(s) + ... + [len(s)-1]*10**(len(s)-len(s))

        dict = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }

        if s in dict:
            return dict[s]
        
        nums = 0
        for i in range(1,len(s)):
            if dict[s[i-1]] < dict[s[i]]:
                nums -= dict[s[i-1]]
                # print('-', dict[s[i-1]])
            else:
                nums += dict[s[i-1]]
                print('+', dict[s[i-1]])
            # print(dict[s[i-1]], 'and', dict[s[i]])
        nums += dict[s[-1]]
        return nums

class Solution:
    def romanToInt(self, s: str) -> int:
        # make dictionary
        # if s == dic.values - 1:
        # convert process
        # elif 
        # [0]*10**len(s) + ... + [len(s)-1]*10**(len(s)-len(s))

        dict = {
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        
        nums = 0
        for i in range(len(s)):
            # if 'i' was less than len(s)-1,
            # it will not excute/compare with index i and i+1
            # and then there is no indexerror.
            # len(s)-1 보다 작아야한다는 조건을 충족하지 못하면, 
            # 뒤의 i와 i+1 인덱스 값 비교도 하지 않기 때문에 indexerror도 일어나지 않는다.
            if i < len(s)-1 and dict[s[i]] < dict[s[i+1]]:
                nums -= dict[s[i]]
            else:
                nums += dict[s[i]]
        return nums
