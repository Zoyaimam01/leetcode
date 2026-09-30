# [1208. Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)

**Date:** 2026-09-30  
**Difficulty:** Medium  
**Tags:** `String, Stack, Bracket Sequences`

---

## Problem Description

A string is a valid parentheses string&nbsp;(denoted VPS) if and only if it consists of &quot;(&quot; and &quot;)&quot; characters only, and:


	It is the empty string, or
	It can be written as&nbsp;AB&nbsp;(A&nbsp;concatenated with&nbsp;B), where&nbsp;A&nbsp;and&nbsp;B&nbsp;are VPS&#39;s, or
	It can be written as&nbsp;(A), where&nbsp;A&nbsp;is a VPS.


We can&nbsp;similarly define the nesting depth depth(S) of any VPS S as follows:


	depth(&quot;&quot;) = 0
	depth(A + B) = max(depth(A), depth(B)), where A and B are VPS&#39;s
	depth(&quot;(&quot; + A + &quot;)&quot;) = 1 + depth(A), where A is a VPS.


For example, &quot;&quot;,&nbsp;&quot;()()&quot;, and&nbsp;&quot;()(()())&quot;&nbsp;are VPS&#39;s (with nesting depths 0, 1, and 2), and &quot;)(&quot; and &quot;(()&quot; are not VPS&#39;s.

Given a VPS seq, split it into two disjoint subsequences A and B, such that&nbsp;A and B are VPS&#39;s (and&nbsp;A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

For example, for the sequence 123456789, one possible split is:


	
	A = {1, 3, 5, 7, 9},
	
	
	B = {2, 4, 6, 8}.
	


This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0] &nbsp;where 0 indicates membership in&nbsp;A&nbsp;and 1 indicates membership in&nbsp;B.

Now choose any such A and B such that&nbsp;max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a&nbsp;choice of A and B:&nbsp; answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.&nbsp; Note that even though multiple answers may exist, you may return any of them.

&nbsp;
Example 1:


Input: seq = &quot;(()())&quot;
Output: [0,1,1,1,1,0]


Example 2:


Input: seq = &quot;()(())()&quot;
Output: [0,0,0,1,1,0,1,1]


&nbsp;
Constraints:


	1 &lt;= seq.size &lt;= 10000



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
