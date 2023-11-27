from typing import List
class Solution:
    def is_self_dividing(self, num: int) -> bool:
        for digit in str(num):
            if int(digit) == 0 or num % int(digit) != 0:
                return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self.is_self_dividing(num):
                result.append(num)
        return result

sol = Solution()
print(sol.selfDividingNumbers(1, 22))
