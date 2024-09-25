You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers. If k < 0, replace the ith number with the sum of the previous k numbers. If k == 0, replace the ith number with 0. As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Input Format

code = [5,7,1,4] k = 3

Constraints:

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
Output Format

[12,10,16,13]

Sample Input 0

5 7 1 4
3
Sample Output 0

[12, 10, 16, 13]
Explanation 0

With k = 3, replace each number with the sum of the next 3 numbers (circularly).

Calculations:

Index 0: 7 + 1 + 4 = 12

Index 1: 1 + 4 + 5 = 10

Index 2: 4 + 5 + 7 = 16

Index 3: 5 + 7 + 1 = 13

Decrypted Code: [12, 10, 16, 13]