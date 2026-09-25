# [1188. Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii/)

**Date:** 2026-09-25  
**Difficulty:** Hard  
**Tags:** `Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting`

---

## Problem Description

Under the grammar given below, strings can represent a set of lowercase words. Let&nbsp;R(expr)&nbsp;denote the set of words the expression represents.

The grammar can best be understood through simple examples:


	Single letters represent a singleton set containing that word.
	
		R(&quot;a&quot;) = {&quot;a&quot;}
		R(&quot;w&quot;) = {&quot;w&quot;}
	
	
	When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
	
		R(&quot;{a,b,c}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;}
		R(&quot;{{a,b},{b,c}}&quot;) = {&quot;a&quot;,&quot;b&quot;,&quot;c&quot;} (notice the final set only contains each word at most once)
	
	
	When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
	
		R(&quot;{a,b}{c,d}&quot;) = {&quot;ac&quot;,&quot;ad&quot;,&quot;bc&quot;,&quot;bd&quot;}
		R(&quot;a{b,c}{d,e}f{g,h}&quot;) = {&quot;abdfg&quot;, &quot;abdfh&quot;, &quot;abefg&quot;, &quot;abefh&quot;, &quot;acdfg&quot;, &quot;acdfh&quot;, &quot;acefg&quot;, &quot;acefh&quot;}
	
	


Formally, the three rules for our grammar:


	For every lowercase letter x, we have R(x) = {x}.
	For expressions e1, e2, ... , ek with k &gt;= 2, we have R({e1, e2, ...}) = R(e1) &cup; R(e2) &cup; ...
	For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) &times; R(e2)}, where + denotes concatenation, and &times; denotes the cartesian product.


Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

&nbsp;
Example 1:


Input: expression = &quot;{a,b}{c,{d,e}}&quot;
Output: [&quot;ac&quot;,&quot;ad&quot;,&quot;ae&quot;,&quot;bc&quot;,&quot;bd&quot;,&quot;be&quot;]


Example 2:


Input: expression = &quot;{{a,z},a{b,c},{ab,z}}&quot;
Output: [&quot;a&quot;,&quot;ab&quot;,&quot;ac&quot;,&quot;z&quot;]
Explanation: Each distinct word is written only once in the final answer.


&nbsp;
Constraints:


	1 &lt;= expression.length &lt;= 60
	expression[i] consists of &#39;{&#39;, &#39;}&#39;, &#39;,&#39;or lowercase English letters.
	The given&nbsp;expression&nbsp;represents a set of words based on the grammar given in the description.



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
