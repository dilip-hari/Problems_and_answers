'''Smallest Binary Number Sum

The program must accept N integers as the input.For each integer X among the N integers, the program
must find the smallest positive integer whose binary representation B is divisible by X (Consider B
as a decimal number while performing division operation). Then the program must print the sum of the
N resulting smallest integers as the output.

Boundary Condition(s):

1 <= N , Each integer value <=100

input Format: 

The first line contains N.
The second line co second line contains N integers separated by a space.

Output Format:
The first line contains an integer representing the sum of the N resulting smallest integers.

Example Input/Output 1:

Input:
4
12 8 23 19

Output:
114

Explanation:

1(st) integer 12:28->11100(11100 is divisible by 12)

2(nd) integer 8:8->1000(1000 is divisible by 8)

3(rd) integer 23:53->110101(110101 is divisible by 23)

4(th) integer 19:25->11001 (11001 is divisible by 19)

28 + 8 + 53 + 25 = 114
Hence 114 is printed as the output.

Example Input/Output 2:

Input:
3
54 63 50

Output:
2785
'''
n=int(input())
s=input().split()
a=[]
sum=0
for i in range(n):
    a.append(int(s[i]))
for i in range(n):
    j=1
    while 1:
        count=0
        #setting value to temp variable
        temp=j;
        #count to find the binary
        while temp:
            count=count+1
            temp=temp//2
        temp=j 
        rev=0
        k=1
        while k<=count :
            rem=(temp//(2**(count-k)))%2
            rev=rev*10+rem
            k=k+1
        if rev%a[i]==0:
            l=rev
            k=0
            sum1=0
            while l:
                power=2**k 
                rem=(l%10)*power
                sum1=sum1+rem
                l=l//10
                k=k+1 
            sum=sum+sum1
            break
        j=j+1
print(sum)
