# [3635. Smallest Divisible Digit Product II](https://leetcode.com/problems/smallest-divisible-digit-product-ii/)

**Date:** 2026-08-07  
**Difficulty:** Hard  
**Tags:** `Math, String, Backtracking, Greedy, Number Theory`

---

## Problem Description

You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return &quot;-1&quot;.

&nbsp;
Example 1:


Input: num = &quot;1234&quot;, t = 256

Output: &quot;1488&quot;

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.


Example 2:


Input: num = &quot;12355&quot;, t = 50

Output: &quot;12355&quot;

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.


Example 3:


Input: num = &quot;11111&quot;, t = 26

Output: &quot;-1&quot;

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.


&nbsp;
Constraints:


	2 &lt;= num.length &lt;= 2 * 105
	num consists only of digits in the range [&#39;0&#39;, &#39;9&#39;].
	num does not contain leading zeros.
	1 &lt;= t &lt;= 1014



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
