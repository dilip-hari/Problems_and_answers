'''
Merge Digits - Sort Integers

The program must accept the The program must accept N three-digit integers as the input. The value of
N is always even. The program ers by merging must form N/2 integers by merging every two
integers (X, Y) among the given N integers based on the following condition.

- The order of digits in the resulting integer from merging X and Y must be as follows.

Largest digit in hundreds place, Smallest digit in hundreds place, Largest digit in tens place,
Smallest digit in tens place, Largest digit in ones place, Smallest digit in ones place.

Finally, the program must print the N/2 integers in sorted order.

Boundary Condition(s):

2 <= N <= 100

Input Format:

The first line contains N.

The second line contains N integers separated by a Space.

Output Format:

The first line contains the N/2 integers in sorted order separated by a space.

Example Input/Output 1:

4
123 654 237 195

Output:

219375 615243

Explanation:

123 and 654 can be merged as 615243.

237 and 195 can be merged as 219375.

So the resulting two integers are printed in sorted order.

Example Input/Output 2:

Input:
6
856 202 100 504 250 712

Output:
510040 725120 825062

'''
n=int(input())
s=input().split()
a=[]
i=0
while i<n:
    num=0
    j=0
    while j<len(s[i]):
        if s[i][j]>s[i+1][j]:
            num=num*10+int(s[i][j])
            num=num*10+int(s[i+1][j])
        else:
            num=num*10+int(s[i+1][j])
            num=num*10+int(s[i][j])
        j=j+1
    a.append(num)
    i=i+2
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i]=a[i]+a[j]
            a[j]=a[i]-a[j]
            a[i]=a[i]-a[j]
for i in a:
    print(i,end=' ')
        
    
