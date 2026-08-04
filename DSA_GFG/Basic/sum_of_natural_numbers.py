"""
Given a positive integer n, find the sum of the first n natural numbers.

Examples : 

Input: n = 3
Output: 6
Explanation: 1 + 2 + 3 = 6

Input: n = 5
Output: 15 
Explanation:  1 + 2 + 3 + 4 + 5 = 15
"""

def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum_of_natural_numbers(3))
print(sum_of_natural_numbers(5))