# [1396. Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/)

**Date:** 2026-11-08  
**Difficulty:** Medium  
**Tags:** `Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting`

---

## Problem Description

You are given a map of a server center, represented as a m * n integer matrix&nbsp;grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers&nbsp;that communicate with any other server.

&nbsp;
Example 1:




Input: grid = [[1,0],[0,1]]
Output: 0
Explanation:&nbsp;No servers can communicate with others.

Example 2:




Input: grid = [[1,0],[1,1]]
Output: 3
Explanation:&nbsp;All three servers can communicate with at least one other server.


Example 3:




Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation:&nbsp;The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can&#39;t communicate with any other server.


&nbsp;
Constraints:


	m == grid.length
	n == grid[i].length
	1 &lt;= m &lt;= 250
	1 &lt;= n &lt;= 250
	grid[i][j] == 0 or 1



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
