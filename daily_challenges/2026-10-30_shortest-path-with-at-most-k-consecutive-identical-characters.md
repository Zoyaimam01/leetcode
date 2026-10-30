# [4104. Shortest Path With At Most K Consecutive Identical Characters](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)

**Date:** 2026-10-30  
**Difficulty:** Medium  
**Tags:** `String, Graph Theory, Heap (Priority Queue), Shortest Path`

---

## Problem Description

You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

&nbsp;
Example 1:


Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = &quot;aab&quot;, k = 1

Output: 3

Explanation:

The optimal valid path from node 0 to node 2 is as follows:


	Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.

The corresponding concatenation of labels is &quot;ab&quot;, which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.

Example 2:


Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = &quot;aab&quot;, k = 2

Output: 2

Explanation:

The optimal valid path from node 0 to node 2 is as follows:


	Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
	Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.

The corresponding concatenation of labels is &quot;aab&quot;, which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.

Example 3:


Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = &quot;aaa&quot;, k = 2

Output: -1

Explanation:

There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.


&nbsp;
Constraints:


	1 &lt;= n == labels.length &lt;= 5 * 104
	0 &lt;= edges.length &lt;= 5 * 104
	edges[i] == [ui, vi, wi]
	0 &lt;= ui, vi &lt;= n - 1
	ui != vi
	1 &lt;= wi &lt;= 104
	labels consists of lowercase English letters
	1 &lt;= k &lt;= 50



---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
