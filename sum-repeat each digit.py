'''
Sum - Repeat Each Digit

The program must accept an integer N as the input. For each digit D in the integer N, the program must
repeat the digit D times to form a new integer value. Then the program must print the sum S of all the
resulting integers as the output.

Boundary Condition(s):

1<=N<=10^6

Input Format:

The first line contains N

Output Format:

The first line contains S.

Example Input/Output 1:

Input:
243

Output:

271019

Explanation:

1st digit: 2243

2nd digit: 244443

3rd digit: 24333

2243 +244443 +24333 = 271019.

Example Input/Output 2:

Input:

9081

Output:

1090888898024

Explanation:

1st digit: 999999999081

2nd digit: 981

3rd digit: 90888888881

4th digit: 9081

999999999081 + 981 + 90888888881 + 9081 = 1090888898024.
'''
num=int(input())
temp=num
sum=0
count=0
while temp:
    count=count+1
    temp=temp//10
temp=num
def num_total(d):
    rev=0
    i=1
    while i<=d:
        rev=rev*10+d
        i=i+1
    return rev
i=count
while i>0:
    d=(temp//(10**(i-1)))%10
    total=num_total(d)
    temp_num=num
    j=count
    sum1=0
    while (j>0):
        digit=(temp//(10**(j-1)))%10
        if(digit==d):
            sum1=sum1*(10**d)+total
        else:
            sum1=sum1*10+digit
        j=j-1
    print(sum1)
    sum=sum+sum1
    i=i-1
print(sum)
