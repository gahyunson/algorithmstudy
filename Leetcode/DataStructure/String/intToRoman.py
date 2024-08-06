# 12. Integer to Roman

def intToRoman(self, num: int) -> str:
	ones = ['I', 'X', 'C', 'M']
	fives = ['V', 'L', 'D']
	i = 0
	ans = []

	while num > 0:
		n = num % 10
		if 1 <= n <= 3:
			ans.append(ones[i] * n) 
		elif n == 4:
			ans.append(ones[i] + fives[i])
		elif 5 <= n <= 8:
			ans.append(fives[i] + ones[i] * (n - 5))
		elif n == 9:
			ans.append(ones[i] + ones[i+1])

		i += 1
		num //= 10

	return "".join(ans[::-1])

class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 500, 100, 50, 10, 5, 1]
        symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

        result = ""
        i = 0
        while i != len(values):
            cnt = num // values[i]
            print(num, '/', values[i], '=', cnt, '...', num%values[i], i)
            if num >= values[i]:
                result += symbols[i] * (cnt)
                num = num%values[i]
            else:
                if num // values[i+1] == 4:
                    result = result + symbols[i+1] + symbols[i]
                    num = num%values[i+1]
                elif num // values[i+2] == 9:
                    result = result + symbols[i+2] + symbols[i]
                    num = num%values[i+2]
            if num == 0:
                return result
            i += 1
                



