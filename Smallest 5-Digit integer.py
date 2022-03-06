'''
Smallest 5-Digit Integer

The program must accept an integer S as the input. The program must print the smallest 5-digit integer
whose sum of digits is equal to S. If it is not possible to form such an integer, then the program
must print as the output.

Boundary Condition(s);1 <= <=

Input Format:
The first line contains S.

Output Format:

The first line contains the smallest 5-digit integer whose sum of digits is equal to S.

Example Input/Output:
Input:
10

Output:
10009

Explanation:

Here S = 10.

The smallest possible 5-digit integer that can be formed is 10009 (1+0+0+0+ 9 = 10).

Example Input/Output 2:

Input:
46

Output:
-1

Example Input/Output 3:
25

Output:
10699

'''
n=int(input())
i=10000
while i<100000:
    temp=i
    sum=0
    while temp:
        sum=sum+temp%10
        temp=temp//10
    if sum==n:
        print(i)
        break
    i=i+1
if i==100000:
    print(-1)
