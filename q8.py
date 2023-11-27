class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]
number = 13
sol = Solution()
print(sol.isPalindrome(number))
