"""
Given a positive integer n, we have to find the sum of squares of first n natural numbers. 
Examples : 

Input : n = 2
Output: 5
Explanation: 1^2+2^2 = 5

Input : n = 8
Output: 204
Explanation :  1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 = 204 
"""

def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum

print(sum_of_squares(2))
print(sum_of_squares(8))

def summation(n):
    return sum([i**2 for i in range(1, n+1)])

print(summation(2))
print(summation(8))