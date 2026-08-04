"""
Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

Examples: 

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the closest to 13, divisible by 4.

Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.
"""

def closest_number(n, m):
    lower = n - (n % m)
    upper = lower + m if n >= 0 else lower - m

    if abs(n - lower) < abs(n - upper):
        return lower
    elif abs(n - lower) > abs(n - upper):
        return upper
    else:
        return lower if abs(lower) > abs(upper) else upper

print(closest_number(13, 4))
print(closest_number(-15, 6))