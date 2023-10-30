# Average Salary

''' You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5
of the actual answer will be accepted.'''

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        if len(salary) <= 2:
            return 0.0

        min_salary = min(salary)
        max_salary = max(salary)
        total_salary = sum(salary) - min_salary - max_salary
        count = len(salary) - 2 

        return float(total_salary) / count

sol = Solution()
salary = [4000,3000,1000,2000]
result = sol.average(salary)
print("Result:", result)