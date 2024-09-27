The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Input Format

Two distinct 0-indexed interger arrays.

nums1 = [4,1,2], nums2 = [1,3,4,2]

Constraints

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
Output Format

Array containing the next greater elements [-1,3,-1]

Sample Input 0

3
4 1 2
4
1 3 4 2
Sample Output 0

[-1, 3, -1]
Explanation 0

Explanation: The next greater element for each value of nums1 is as follows:

4 is bold in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
1 is bold in nums2 = [1,3,4,2]. The next greater element is 3.
2 is bold in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Sample Input 1

2
2 4
4
1 2 3 4
Sample Output 1

[3, -1]