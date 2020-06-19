Problem 1
To solve to problem, I use the BST to find the int of square root by updating the head and tail.

Time Complexity: O(log(n))
Space Complexity: O(1)

===================================
Problem 2
To solve to problem, I first focus on find the pivot using binary search method. Then I apply the standard binary search idea on both parts which are separated by the pivot.
Time Complexity: O(log(n))
Space Complexity: O(1)

===================================
Problem 3
To solve to problem, I first use the divide-and-conquer idea for sorting. Then I allocate the number one by one from the sorted array to each of the two outputs, to ensure:
(1) Larger number in higher digits;
(2) The difference of number of digits between two outputs is not bigger than 1.
Time Complexity: O(nlog(n))
Space Complexity: O(n)

===================================
Problem 4
To solve to problem, I only count the number of the occurences of 0 and 1 in one traversal, then the rest will be 2.
Time Complexity: O(n)
Space Complexity: O(n)

===================================
Problem 5
To implement the trie data structure, I use a dictionary to store all the children.

Insert
	Time Complexity: O(n)
	Traverse the input once
	Space Complexity: O(1)
	In worst case, need to create new nodes in each iteration.
Find
	Time Complexity: O(n)
	Traverse the input once
	Space Complexity: O(1)
	No addtional memory needed, move the pointer.
Suffixes
	Time Complexity: O(n*m)
	Here, n is the number of inputs and m is the length of average input.
	Space Complexity: O(1)
	No addtional memory needed, move the pointer only.
===================================
Problem 6
To solve to problem, I traverse the input once and update the min/max
Time Complexity: O(n) 
One time traversal.
Space Complexity: O(1)
Only keep track of the max and min.
===================================
Problem 7
The logic here is similar as problem 5
Add handler:
	Time Complexity: O(n*m)
	Traverse the length n list split by input, each node is assumed to have m children.
	Space Complexity: O(n)
	In worst case, need to create new nodes in each iteration.
Lookup:
	Time Complexity: O(n*m)
	Traverse the length n list split by input, each node is assumed to have m children.
	Space Complexity: O(1)
	No addtional memory needed.