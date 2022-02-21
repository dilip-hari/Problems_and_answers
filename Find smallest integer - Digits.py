'''Find Smallest Integer - Digits

The program must accept N integers and an integer K as the input. For each digit D in K, the program
must find the smallest integer that contains the digit D. If there is no integer with the digit D,
then consider for that digit. Finally, the program must print the sum of resulting integers as the
output.

Boundary Condition(s):

1 <= N <= 100

 1<=Each integer value, K<=10^7

input Format:

The first line contains N.

The second line contains N integers separated by a space. The third 2111710600hd line contains K

Output Format:

The first line contains an integer representing the sum of resulting integers based on the given
conditions.

Example Input/Output 1:

Input:

7

909 880 283 205 790 495 922

248

Output:

983

Here K = 248

1st digit is 2: The smallest integer having the digit 2 is 205

2nd digit is 4: The smallest integer having the digit 4 is 495

3rd digit is 8: The smallest integer having the digit 8 is 283

205 + 495 + 283 = 983

Hence 983 is printed as the output. '''

n=int(input())
s=input().split()
k=input()
a=[]
for i in s:
    a.append(int(i))
sum=0
for i in k:
    d=int(i)
    flag1=0
    flag2=0
    j=0
    while j<n:
        temp=a[j]
        while temp:
            rem=temp%10
            if d==rem:
                flag1=1
                break
            temp=temp//10
        if flag1==1 and d==rem and flag2==0:
            mini=a[j]
            flag2=1
        elif flag2==1 and a[j]<mini and d==rem:
            mini=a[j]
        j=j+1
    if flag1==1:
        sum=sum+mini
print(sum)















