# [2559. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)

**Date:** 2026-09-15  
**Difficulty:** Hard  
**Tags:** `Two Pointers, String, Dynamic Programming, Greedy`

---

## Problem Description

You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:


	The length of each substring is at least k.
	Each substring is a palindrome.


Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

&nbsp;
Example 1:


Input: s = &quot;abaccdbbd&quot;, k = 3
Output: 2
Explanation: We can select the substrings underlined in s = &quot;abaccdbbd&quot;. Both &quot;aba&quot; and &quot;dbbd&quot; are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.


Example 2:


Input: s = &quot;adbcda&quot;, k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.


&nbsp;
Constraints:


	1 &lt;= k &lt;= s.length &lt;= 2000
	s consists of lowercase English letters.



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
