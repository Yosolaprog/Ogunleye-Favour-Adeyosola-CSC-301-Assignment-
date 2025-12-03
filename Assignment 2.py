# NAME:OGUNLEYE FAVOUR ADEYOSALA
# MATRIC NO: 230502041

#Recursion to sum the first 10 numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(10))

#Program to get Fibonacci series of 8 terms
def Fibonacci_n(n):
    a, b = 1, 0
    for i in range(n):
        a, b = a+b

        Fibonacci_n(8)

#Insert the following values into a Dynamic Array of size 2:

#Values to insert:
#10, 30, 40, 50
#Starting capacity = 2
#We will insert step-by-step:

#Step 1: Insert 10
#Array: [10, _]
#Size = 1, Capacity = 2

#Step 2: Insert 30
#Array: [10, 30]
#Size = 2, Capacity = 2 → FULL

#Step 3: Insert 40 → RESIZE
#Resize rule: capacity doubles → 2 → 4
#New array: [10, 30, _, _]

#Insert 40:
#Array becomes: [10, 30, 40, _]
#Size = 3, Capacity = 4

#Step 4: Insert 50
#Array: [10, 30, 40, 50]
#Size = 4, Capacity = 4

#FINAL ANSWER:
#Dynamic array after all insertions:
#[10, 30, 40, 50]
#Final capacity: 4

#4. Perform a Linear Search on array:

#Array: [2, 5, 7, 10, 14, 20]
#Target = 10

#Tracing:
#Index	Value	Match?
#0	      2	      No
#1	      5       No
#2	      7	      No
#3	     10	      YES
#4	     14	       —
#5	     20	       —
#Result:
#10 is found at index 3

#5. Trace the Binary Search

#Sorted array:
#[1, 3, 5, 7, 9, 11, 13]
#Target = 9

#Let’s trace:
#Step 1

#low = 0
#high = 6
#mid = (0+6)//2 = 3
#value at mid = 7
#7 < 9 → search right half

#Step 2
#low = 4
#high = 6
#mid = (4+6)//2 = 5
#value at mid = 11
#11 > 9 → search left half

#Step 3
#low = 4
# high = 4
#mid = (4+4)//2 = 4
#value at mid = 9
#MATCH FOUND

#ANSWER:
#Binary search finds 9 at index 4.

#Time & Space Complexity

#Linear Search
#Time: O(n)

#Space: O(1)
#Binary Search

#Time: O(log n)
#Space:

#Iterative: O(1)
#Recursive: O(log n) (because of call stack)