print('Triangular(n)')
# This takes a nonnegative integer n, and returns
# an integer, the sum of the first n positive integers. 
def triangular(n):
    return (n*(n+1))//2
print(triangular(5))
print('')

print('isTri(s, t, u)')
# This takes three float values representing the lengths of the sides
# of a triangle, and returns True if such a triangle exists and False otherwise.
def isTri(s, t, u):
    return True if s + t + u > 0 and s + t > u else False
print(isTri(3, 4, 5))
print(isTri(-3, -4, -5))
print('')

print('XOR(a, b)')
# This computes the exclusive-or of two boolean values a and b.
def XOR(a, b):
    return ((a and not b) or (not a and b))
print(XOR(True, True))
print(XOR(False, False))
print(XOR(False, True))
print('')

print('getIntheFromEnd(n, i)')
# This takes a positive integer n and a non-negative int i,
# and returns the ith digit of n, starting from 0, counting from the right.
def getIthFromEnd (n, i):
    return (n // 10**i) % 10
print(getIthFromEnd(456,0))
print('')

print('iOverlap(a1, a2, b1, b2)')
# takes four integers a1, a2, b1, b2, defining two closed intervals 
# [a1, a2] and [b1, b2] of the real number line, and returns True if these two
# closed intervals overlap (even if at only one value) and False otherwise
def iOverlap(a1, a2, b1, b2):
    return a1 <= b2 and a2 >= b1 
print(iOverlap(-54.23, -17.67, 29.46, 64.48))
