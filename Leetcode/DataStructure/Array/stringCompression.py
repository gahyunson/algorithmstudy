# 443. String Compression

# Given an array of characters `chars`, compress it using the following algorithm:

# Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`.

# If the group's length is 1, append the character to s.

# Otherwise, append the character followed by the group's length.

# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0
        while i < len(chars):
            letter = chars[i]
            cnt = 0
            while i <len(chars) and chars[i] == letter:
                cnt += 1
                i += 1
            
            chars[ans] = letter 
            ans += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[ans] = c 
                    ans += 1
        return ans