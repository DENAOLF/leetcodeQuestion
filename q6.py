from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for h in hours:
            if h >= target:
                count += 1
        return count

hours = [100, 80, 90, 70, 60]
target = 80
sol = Solution()
print(sol.numberOfEmployeesWhoMetTarget(hours, target))
