# 71. Simplify Path
# Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

# In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

# The simplified canonical path should adhere to the following rules:

# It must start with a single slash '/'.
# Directories within the path should be separated by only one slash '/'.
# It should not end with a slash '/', unless it's the root directory.
# It should exclude any single or double periods used to denote current or parent directories.
# Return the new path.

'''
How to approah?

I ignored the specific characters and appended the rest of characters to a new Array.
and I return the result that was transformed to the string type from the new array.

Time complexcity : O(n)
Space somplexcity : O(n)

문자열을 배열로 바꾸어서 특정 문자인 경우 무시하고, 그 외는 배열에 추가하도록 하였다.
그리고 그 배열을 문자열로 변환하여 반환하였다.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[-1] == '/':
            path = path[:-1]

        path_list = path.split('/')

        result = []
        for cur in path_list:
            if cur in ['', '.']:
                continue
            elif cur == '..':
                result = result[:-1]
                continue
            result.append(cur)

        result = '/' + '/'.join(result)
        return result

