Problem 1
Use a dictionary to store the values, and list to keep track of the order. When the capacity is reached, pop the oldest one.
List pop or append method, constant time complexity O(1), space is O(n).

Problem 2
Use the recursive function to go through the nest folders to find the desired file type.
Go through all the folders, thus time complexity is linear O(n). Space complexity is O(n) since a variable is allocated for the number of files in the directory

Problem 3
Use a heap data structure to order in the process of merging.
Use a nested list to represent the tree.
Encode:
	time O(nlog(n)): getFreq takes O(n) time, make the heap takes O(n) time, merge takes O(logn), getCode takes O(n). These all result in a complexity of nlogn
	space O(n):n is the size of the string. There is a linear space complexity.
Decode:
	time O(n): A for loop going through each character in the encoded_text
	space O(1) :Only one variable is allocated

Problem 4
Similar as problem 2, use a recursive function to explore the group and children groups to find the users.
Both the time and space complexity is O(n)

Problem 5
Based on the linked list. append method will add new element to the block chain
Time is O(1) and space complexity is O(n).

Problem 6
Transform the linked list to list and use the set operations of python.
Based on the time complexity of union and intersection in Python, the time complexity here is O(n) and O(n^2) for union and intersection, respectively.
Space is O(n).