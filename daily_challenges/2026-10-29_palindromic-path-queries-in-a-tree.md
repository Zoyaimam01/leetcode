# [4209. Palindromic Path Queries in a Tree](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)

**Date:** 2026-10-29  
**Difficulty:** Hard  
**Tags:** `Array, String, Divide and Conquer, Bit Manipulation, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree`

---

## Problem Description

You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:


	&quot;update ui c&quot;: Change the character at node ui to c. Formally, update s[ui] = c.
	&quot;query ui vi&quot;: Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.


Return a boolean array answer, where answer[j] is true if the jth query of type &quot;query ui vi&quot;​​​​​​​ can be rearranged into a palindrome, and false otherwise.

&nbsp;
Example 1:


Input: n = 3, edges = [[0,1],[1,2]], s = &quot;aac&quot;, queries = [&quot;query 0 2&quot;,&quot;update 1 b&quot;,&quot;query 0 2&quot;]

Output: [true,false]

Explanation:


	&quot;query 0 2&quot;: Path 0 &rarr; 1 &rarr; 2 gives &quot;aac&quot;, which can be rearranged to form &quot;aca&quot;, a palindrome. Thus, answer[0] = true.
	&quot;update 1 b&quot;: Update node 1 to &#39;b&#39;, now s = &quot;abc&quot;.
	&quot;query 0 2&quot;: Path characters are &quot;abc&quot;, which cannot be rearranged to form a palindrome. Thus, answer[1] = false.


Thus, answer = [true, false].


Example 2:


Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = &quot;abca&quot;, queries = [&quot;query 1 2&quot;,&quot;update 0 b&quot;,&quot;query 2 3&quot;,&quot;update 3 a&quot;,&quot;query 1 3&quot;]

Output: [false,false,true]

Explanation:


	&quot;query 1 2&quot;: Path 1 &rarr; 0 &rarr; 2 gives &quot;bac&quot;, which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
	&quot;update 0 b&quot;: Update node 0 to &#39;b&#39;, now s = &quot;bbca&quot;.
	&quot;query 2 3&quot;: Path 2 &rarr; 0 &rarr; 3 gives &quot;cba&quot;, which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
	&quot;update 3 a&quot;: Update node 3 to &#39;a&#39;, s = &quot;bbca&quot;.
	&quot;query 1 3&quot;: Path 1 &rarr; 0 &rarr; 3 gives &quot;bba&quot;, which can be rearranged to form &quot;bab&quot;, a palindrome. Thus, answer[2] = true.


Thus, answer = [false, false, true].


&nbsp;
Constraints:


	1 &lt;= n == s.length &lt;= 5 * 104
	edges.length == n - 1
	edges[i] = [ui, vi]
	0 &lt;= ui, vi &lt;= n - 1
	s consists of lowercase English letters.
	The input is generated such that edges represents a valid tree.
	1 &lt;= queries.length &lt;= 5 * 104​​​​​​​
	
		queries[i] = &quot;update ui c&quot; or
		queries[i] = &quot;query ui vi&quot;
		0 &lt;= ui, vi &lt;= n - 1
		c is a lowercase English letter.
	
	



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
