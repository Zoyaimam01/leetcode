# [3811. Reverse Degree of a String](https://leetcode.com/problems/reverse-degree-of-a-string/)

**Date:** 2026-09-20  
**Difficulty:** Easy  
**Tags:** `String, Simulation`

---

## Problem Description

Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:


	For each character, multiply its position in the reversed alphabet (&#39;a&#39; = 26, &#39;b&#39; = 25, ..., &#39;z&#39; = 1) with its position in the string (1-indexed).
	Sum these products for all characters in the string.


Return the reverse degree of s.

&nbsp;
Example 1:


Input: s = &quot;abc&quot;

Output: 148

Explanation:


	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			&#39;a&#39;
			26
			1
			26
		
		
			&#39;b&#39;
			25
			2
			50
		
		
			&#39;c&#39;
			24
			3
			72
		
	


The reversed degree is 26 + 50 + 72 = 148.


Example 2:


Input: s = &quot;zaza&quot;

Output: 160

Explanation:


	
		
			Letter
			Index in Reversed Alphabet
			Index in String
			Product
		
		
			&#39;z&#39;
			1
			1
			1
		
		
			&#39;a&#39;
			26
			2
			52
		
		
			&#39;z&#39;
			1
			3
			3
		
		
			&#39;a&#39;
			26
			4
			104
		
	


The reverse degree is 1 + 52 + 3 + 104 = 160.


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 1000
	s contains only lowercase English letters.



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
