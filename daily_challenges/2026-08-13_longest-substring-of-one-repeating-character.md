# [2319. Longest Substring of One Repeating Character](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)

**Date:** 2026-08-13  
**Difficulty:** Hard  
**Tags:** `Array, String, Segment Tree, Ordered Set`

---

## Problem Description

You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

&nbsp;
Example 1:


Input: s = &quot;babacc&quot;, queryCharacters = &quot;bcb&quot;, queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = &quot;bbbacc&quot;. The longest substring consisting of one repeating character is &quot;bbb&quot; with length 3.
- 2nd query updates s = &quot;bbbccc&quot;. 
  The longest substring consisting of one repeating character can be &quot;bbb&quot; or &quot;ccc&quot; with length 3.
- 3rd query updates s = &quot;bbbbcc&quot;. The longest substring consisting of one repeating character is &quot;bbbb&quot; with length 4.
Thus, we return [3,3,4].


Example 2:


Input: s = &quot;abyzz&quot;, queryCharacters = &quot;aa&quot;, queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = &quot;abazz&quot;. The longest substring consisting of one repeating character is &quot;zz&quot; with length 2.
- 2nd query updates s = &quot;aaazz&quot;. The longest substring consisting of one repeating character is &quot;aaa&quot; with length 3.
Thus, we return [2,3].


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 105
	s consists of lowercase English letters.
	k == queryCharacters.length == queryIndices.length
	1 &lt;= k &lt;= 105
	queryCharacters consists of lowercase English letters.
	0 &lt;= queryIndices[i] &lt; s.length



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
