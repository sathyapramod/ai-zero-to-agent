"""
Given a number n, check whether it is even or odd. Return true for even and false for odd.

Examples: 

Input: n = 15
Output: false
Explanation: 15 % 2 = 1, so 15 is odd .

Input: n = 44
Output: true
Explanation: 44 % 2 = 0, so 44 is even.
"""

def check_even_or_odd(n):
    rem = n % 2
    if rem == 0:
        return True
    else:
        return False

print(check_even_or_odd(15))
print(check_even_or_odd(44))