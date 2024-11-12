
"""
Translate insertion sort pseudocode to python.
Aim to insert poker card from right hand to left hand with correct order.
"""

# Define the list A with any integer values
A = [5, 2, 4, 6, 1, 3]

for i in range(1, len(A)):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j = j - 1
    A[j + 1] = key

print(A)