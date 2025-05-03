### 🔁 Problem: Check if Array Is Sorted and Rotated

**Given** an array `nums`, return `True` if the array was originally sorted in non-decreasing order and then rotated some number of times (including zero).  
Otherwise, return `False`.

There **may be duplicates** in the array.

---

#### 📝 Definition of Rotation:
An array `A` rotated by `x` positions results in an array `B` such that:
`B[i] == A[(i + x) % A.length]` for every valid index `i`.

---

#### 🧾 Examples:

**Example 1:**
Input: nums = [3, 4, 5, 1, 2]
Output: true
Explanation: [1, 2, 3, 4, 5] rotated 3 times becomes [3, 4, 5, 1, 2]
