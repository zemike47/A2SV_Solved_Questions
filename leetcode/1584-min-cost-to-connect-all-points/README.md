# 1584. Min-Cost-to-Connect-All-Points

**Difficulty:** Medium

**Problem:** [Min-Cost-to-Connect-All-Points](https://leetcode.com/problems/min-cost-to-connect-all-points)

---

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x i , y i ]`.

The cost of connecting two points `[x i , y i ]` and `[x j , y j ]` is the **manhattan distance** between them: `|x i - x j | + |y i - y j |`, where `|val|` denotes the absolute value of `val`.

Return the minimum cost to make all points connected. All points are connected if there is **exactly one** simple path between any two points.

Example 1:

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)

```
Input:  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output:  20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

Example 2:

```
Input:  points = [[3,12],[-2,5],[-4,1]]
Output:  18
```

**Constraints:**

- `1 <= points.length <= 1000`

- `-10⁶ <= x i , y i <= 10⁶`

- All pairs `(x i , y i )` are distinct.