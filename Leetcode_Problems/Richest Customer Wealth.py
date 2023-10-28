#  Richest Customer Wealth

''' You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the 
i-th customer has in the j-th bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer 
is the customer that has the maximum wealth.'''

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)
        
        return max_wealth
            
sol = Solution()
accounts = [[1,2,3],[3,2,1]]
result = sol.maximumWealth(accounts)
print("Result:", result)