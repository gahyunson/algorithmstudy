# 6. Zigzag Conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# add the character to each row

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s

        row_idx = 1
        row_arr = [""] * numRows
        limit = True
        for c in s:
            row_arr[row_idx-1]+=c
            if row_idx == numRows:
                limit = False
            elif row_idx == 1:
                limit = True

            if limit:
                row_idx+=1
            elif not limit:
                row_idx-=1
        return "".join(row_arr)
            




        '''
           012
        0  PAY
         3  P
        4  ALI
         7  S
        8  HIR
         11 I
        12 NG
        PAY P ALI S HIR I NG
        123 2 123 2 123 2 12
        PAHN APLSIIG YIR
        1111 2222222 333
        0 4 8 12 1 3 5 7 9 11 13 2 6 10 
        0 4 8 12 (0+1) 3 (4+1) 7 (8+1) 11 (12+1) (0+1+1) (4+1+1) (8+1+1)

           0123
        0  PAYP
             A
            L
        6  ISHI
             R
            I
        12 NG
        PAYPALISHIRING
        12343212343212
        PAHNAPLSIIGYIR
        12
        0 6 12 1 5 7 11 13 2 4 8 10 3 9
        0 6 12 (0+1) 5 (6+1) 11 (12+1) (0+1+1) 4 (6+1+1) 10 3 (6+1+1+1)
        '''
        # r = len(s)//(len(s)//numRows)+1
        # for i in range(0, len(s), numRows):
        #     print(s[i:i+r])